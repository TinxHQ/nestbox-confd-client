#!/usr/bin/env python3
# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+


from setuptools import setup
from setuptools import find_packages


setup(
    name='nestbox_confd_client',
    version='0.1',
    description='a simple client library for the nestbox confd HTTP interface',
    author='Wazo Authors',
    author_email='dev@wazo.io',
    url='http://wazo.io',
    packages=find_packages(),
    entry_points={
        'nestbox_confd_client.commands': [
            'config = nestbox_confd_client.commands.config:ConfigCommand',
            'customers = nestbox_confd_client.commands.customers:CustomersCommand',
            'engines = nestbox_confd_client.commands.engines:EnginesCommand',
            'init = nestbox_confd_client.commands.init:InitCommand',
            'locations = nestbox_confd_client.commands.locations:LocationsCommand',
            'resellers = nestbox_confd_client.commands.resellers:ResellersCommand',
            'tenants = nestbox_confd_client.commands.tenants:TenantsCommand',
            'users = nestbox_confd_client.commands.users:UsersCommand',
            'swarm = nestbox_confd_client.commands.swarm:Swarm',
        ],
        'nestbox_confd_client.commands.swarm.plugins': [
            'credentials = nestbox_confd_client.commands.swarm.plugins.credentials:CredentialsCommand',
            'token = nestbox_confd_client.commands.swarm.plugins.token:TokenCommand',
        ],
    }
)
