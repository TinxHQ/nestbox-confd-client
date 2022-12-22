# Copyright 2018-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from nestbox_confd_client.command import ConfdCommand


class ResellersCommand(ConfdCommand):

    resource = 'resellers'

    def create(self, reseller):
        headers = self._get_headers()
        r = self.session.post(self.base_url, json=reseller, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def list(self):
        headers = self._get_headers()
        r = self.session.get(self.base_url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def get(self, reseller_uuid):
        headers = self._get_headers()
        url = f'{self.base_url}/{reseller_uuid}'
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, reseller_uuid):
        headers = self._get_headers()
        url = f'{self.base_url}/{reseller_uuid}'
        r = self.session.delete(url, headers=headers)
        self.raise_from_response(r)

    def update(self, reseller_uuid, reseller):
        headers = self._get_headers()
        url = f'{self.base_url}/{reseller_uuid}'
        r = self.session.put(url, json=reseller, headers=headers)
        self.raise_from_response(r)
