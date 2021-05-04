# Copyright 2018-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from nestbox_confd_client.command import ConfdCommand


class EnginesCommand(ConfdCommand):

    resource = 'engines'
    _ro_headers = {'Accept': 'application/json'}
    _rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def create_account_event(self, instance_uuid, event):
        url = f'{self.base_url}/instances/{instance_uuid}/accounts/events'
        r = self.session.post(url, json=event, headers=self._rw_headers)
        self.raise_from_response(r)

    def check_accounts_hash(self, instance_uuid, hash_):
        url = f'{self.base_url}/instances/{instance_uuid}/synchronize'
        params = {'hash': hash_}
        r = self.session.head(url, params=params, headers=self._ro_headers)
        if r.status_code in (204, 409):
            return r.status_code == 204
        self.raise_from_response(r)

    def synchronize_accounts(self, instance_uuid, accounts):
        url = f'{self.base_url}/instances/{instance_uuid}/synchronize'
        body = {'accounts': accounts}
        r = self.session.post(url, json=body, headers=self._rw_headers)
        self.raise_from_response(r)
