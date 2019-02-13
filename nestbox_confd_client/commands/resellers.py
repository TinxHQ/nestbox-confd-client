# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from nestbox_confd_client.command import ConfdCommand


class ResellersCommand(ConfdCommand):

    resource = 'resellers'
    _ro_headers = {'Accept': 'application/json'}
    _rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def create(self, reseller):
        r = self.session.post(self.base_url, json=reseller, headers=self._rw_headers)
        self.raise_from_response(r)
        return r.json()

    def list(self):
        r = self.session.get(self.base_url, headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()

    def get(self, reseller_uuid):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=reseller_uuid)
        r = self.session.get(url, headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, reseller_uuid):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=reseller_uuid)
        r = self.session.delete(url, headers=self._ro_headers)
        self.raise_from_response(r)

    def update(self, reseller_uuid, reseller):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=reseller_uuid)
        r = self.session.put(url, json=reseller, headers=self._rw_headers)
        self.raise_from_response(r)
