#!/usr/bin/env python3
# Copyright 2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import argparse
import csv
import sys

from nestbox_confd_client import Client as ConfdClient
from wazo_auth_client import Client as AuthClient


def _extract_verify_certificate(value):
    if value.lower() == 'true':
        return True
    if value.lower() == 'false':
        return False
    return value


def main():
    args = parse_args()
    verify_certificate = _extract_verify_certificate(args.verify_certificate)

    auth_client = AuthClient(
        args.host,
        port=443,
        prefix='/api/auth',
        verify_certificate=verify_certificate,
        username=args.username,
        password=args.password,
    )
    token = auth_client.token.new()['token']
    auth_client.set_token(token)

    confd_client = ConfdClient(
        args.host,
        port=443,
        prefix='/api/confd',
        verify_certificate=verify_certificate,
        token=token,
    )
    rcl = []
    if args.rcl:
        rcl = detect_desync_rcl(auth_client, confd_client)

    users = []
    if args.users:
        users = detect_desync_users(auth_client, confd_client)

    if args.delete_orphan_users:
        delete_desync_users(confd_client, users)

    if not rcl and not users:
        sys.exit(0)

    if args.output:
        output_file = open(args.output, "w")
    else:
        output_file = sys.stdout

    fieldnames = ['uuid', 'type', 'name']
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in rcl + users:
        writer.writerow(row)

    if args.output:
        output_file.close()

    sys.exit(1)


def delete_desync_users(confd_client, users):
    for user in users:
        confd_client.users.delete(user['uuid'])


def detect_desync_users(auth_client, confd_client):
    result = []
    response = auth_client.users.list(recurse=True)
    user_uuids = set(user['uuid'] for user in response['items'])

    confd_users = confd_client.users.list()['items']
    for confd_user in confd_users:
        if confd_user['uuid'] not in user_uuids:
            result.append({
                'uuid': confd_user['uuid'],
                'type': 'user',
                'name': '',
            })
    return result


def detect_desync_rcl(auth_client, confd_client):
    result = []
    response = auth_client.tenants.list()
    tenants = {tenant['uuid']: tenant for tenant in response['items']}

    resellers = confd_client.resellers.list()['items']
    for reseller in resellers:
        tenant = tenants.get(reseller['uuid'])
        if not tenant:
            result.append({
                'uuid': reseller['uuid'],
                'type': 'reseller',
                'name': reseller['name'],
            })

    customers = confd_client.customers.list()['items']
    for customer in customers:
        tenant = tenants.get(customer['uuid'])
        if not tenant:
            result.append({
                'uuid': customer['uuid'],
                'type': 'customer',
                'name': customer['name'],
            })

    locations = confd_client.locations.list()['items']
    for location in locations:
        tenant = tenants.get(location['uuid'])
        if not tenant:
            result.append({
                'uuid': location['uuid'],
                'type': 'location',
                'name': location['name'],
            })
    return result


def parse_args():
    parser = argparse.ArgumentParser(
        description="""
        Detect desynchronizations between wazo-auth and nestbox-confd.

        Only users can be removed automatically from nestbox-confd because impacts are minimal.
        Any other destructive operation must be done manually
        """
    )
    parser.add_argument(
        'host',
        help="The nestbox hostname",
    )
    parser.add_argument(
        '-u',
        '--username',
        required=True,
    )
    parser.add_argument(
        '-p',
        '--password',
        required=True,
    )
    parser.add_argument(
        '--verify_certificate',
        default='True',
        help="Boolean or path to verify certificate. Default: true",
    )
    parser.add_argument(
        '--rcl',
        action='store_true',
        default=False,
        help="Detect resellers/customers/locations desynchronization",
    )
    parser.add_argument(
        '--users',
        action='store_true',
        default=False,
        help="Detect users desynchronization",
    )
    parser.add_argument(
        '--delete-orphan-users',
        action='store_true',
        help="Delete all orphan users from nestbox-confd.",
    )
    parser.add_argument(
        '-o',
        '--output',
        help="Output file to write the csv. Default: stdout",
    )
    return parser.parse_args()


if __name__ == '__main__':
    main()
