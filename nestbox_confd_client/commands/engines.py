# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from nestbox_confd_client.command import ConfdCommand


class EnginesCommand(ConfdCommand):

    resource = 'engines'
    _ro_headers = {'Accept': 'application/json'}
    _rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def create_account_event(self, instance_uuid, event):
        url = '{base}/instances/{uuid}/accounts/events'.format(base=self.base_url, uuid=instance_uuid)
        r = self.session.post(url, json=event, headers=self._rw_headers)
        self.raise_from_response(r)

    def check_accounts_hash(self, instance_uuid, hash_):
        url = '{base}/instances/{uuid}/accounts/synchronize'.format(base=self.base_url, uuid=instance_uuid)
        params = {'hash': hash_}
        r = self.session.head(url, params=params, headers=self._ro_headers)
        if r.status_code in (204, 409):
            return r.status_code == 204
        self.raise_from_response(r)

    def synchronize_accounts(self, instance_uuid, accounts):
        url = '{base}/instances/{uuid}/accounts/synchronize'.format(base=self.base_url, uuid=instance_uuid)
        body = {'accounts': accounts}
        r = self.session.post(url, json=body, headers=self._rw_headers)
        self.raise_from_response(r)
