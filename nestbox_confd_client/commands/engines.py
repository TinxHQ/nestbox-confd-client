# Copyright 2018-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from nestbox_confd_client.command import ConfdCommand


class EnginesCommand(ConfdCommand):

    resource = 'engines'

    def create_account_event(self, instance_uuid, event):
        headers = self._get_headers()
        url = f'{self.base_url}/instances/{instance_uuid}/accounts/events'
        r = self.session.post(url, json=event, headers=headers)
        self.raise_from_response(r)

    def check_accounts_hash(self, instance_uuid, hash_):
        headers = self._get_headers()
        url = f'{self.base_url}/instances/{instance_uuid}/accounts/synchronize'
        params = {'hash': hash_}
        r = self.session.head(url, params=params, headers=headers)
        if r.status_code in (204, 409):
            return r.status_code == 204
        self.raise_from_response(r)

    def synchronize_accounts(self, instance_uuid, accounts):
        headers = self._get_headers()
        url = f'{self.base_url}/instances/{instance_uuid}/accounts/synchronize'
        body = {'accounts': accounts}
        r = self.session.post(url, json=body, headers=headers)
        self.raise_from_response(r)
