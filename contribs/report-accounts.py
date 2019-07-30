#!/usr/bin/env python3
# Copyright 2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import argparse
import csv
import io
import shutil

from wazo_auth_client import Client as AuthClient
from nestbox_confd_client import Client as ConfdClient


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
        verify_certificate=verify_certificate,
        username=args.username,
        password=args.password,
    )
    token = auth_client.token.new()['token']

    confd_client = ConfdClient(
        args.host,
        verify_certificate=verify_certificate,
        token=token
    )
    resellers = confd_client.resellers.list()['items']

    result = io.StringIO()
    fieldnames = [
        'reseller_name',
        'reseller_uuid',
        'customer_name',
        'customer_uuid',
        'user_uuid',
        'tenant_uuid',
        'subscription',
        'created_at',
        'modified_at'
    ]
    writer = csv.DictWriter(result, fieldnames=fieldnames)
    writer.writeheader()
    for reseller in resellers:
        accounts = confd_client.accounts.list(tenant_uuid=reseller['uuid'])['items']
        for account in accounts:
            account['reseller_name'] = reseller['name']
            account['reseller_uuid'] = reseller['uuid']
            account['customer_name'] = account['customer']['name']
            account['customer_uuid'] = account['customer']['uuid']
            account.pop('customer')
            account['user_uuid'] = account.pop('uuid')
            writer.writerow(account)

    if args.output:
        with open(args.output, 'w') as fobj:
            result.seek(0)
            shutil.copyfileobj(result, fobj)
    else:
        print(result.getvalue())


def parse_args():
    parser = argparse.ArgumentParser()
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
        '-o',
        '--output',
        help="Output file to write the csv. Default: stdout",
    )
    return parser.parse_args()


if __name__ == '__main__':
    main()
