#!/usr/bin/env python3
# Copyright 2020-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

import argparse
import csv
import io
import os
import shutil

from getpass import getpass

from nestbox_confd_client import Client as ConfdClient
from wazo_auth_client import Client as AuthClient
from wazo_deployd_client import Client as DeploydClient


def _extract_verify_certificate(value: str) -> bool | str:
    if value.lower() == 'true':
        return True
    if value.lower() == 'false':
        return False
    return value


def main():
    args = parse_args()
    verify_certificate = _extract_verify_certificate(args.verify_certificate)

    password = os.getenv('PORTAL_PASSWORD', None)
    if not password:
        password = getpass()

    auth_client = AuthClient(
        args.host,
        port=443,
        prefix='/api/auth',
        verify_certificate=verify_certificate,
        username=args.username,
        password=password,
    )
    token = auth_client.token.new()['token']

    confd_client = ConfdClient(
        args.host,
        port=443,
        prefix='/api/confd',
        verify_certificate=verify_certificate,
        token=token,
    )
    deployd_client = DeploydClient(
        args.host,
        port=443,
        prefix='/api/deployd',
        verify_certificate=verify_certificate,
        token=token,
    )

    instances = confd_client.instances.list(recurse=True)['items']

    result = io.StringIO()
    fieldnames = [
        'reseller_name',
        'reseller_uuid',
        'instance_name',
        'instance_uuid',
        'synchronization_at',
    ]
    writer = csv.DictWriter(result, fieldnames=fieldnames)
    writer.writeheader()
    for instance in instances:
        full_instance = deployd_client.instances.get(instance['uuid'])
        reseller = confd_client.resellers.get(instance['tenant_uuid'])
        row = {
            'reseller_name': reseller['name'],
            'reseller_uuid': reseller['uuid'],
            'instance_name': full_instance['name'],
            'instance_uuid': instance['uuid'],
            'synchronization_at': instance['synchronization_at'],
        }
        writer.writerow(row)

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
