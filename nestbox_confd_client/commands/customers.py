# Copyright 2018-2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from nestbox_confd_client.command import ConfdCommand


class CustomersCommand(ConfdCommand):

    resource = 'customers'
    _ro_headers = {'Accept': 'application/json'}
    _rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def create(self, customer):
        r = self.session.post(self.base_url, json=customer, headers=self._rw_headers)
        self.raise_from_response(r)
        return r.json()

    def list(self, **kwargs):
        r = self.session.get(self.base_url, headers=self._ro_headers, params=kwargs)
        self.raise_from_response(r)
        return r.json()

    def get(self, customer_uuid):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=customer_uuid)
        r = self.session.get(url, headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, customer_uuid):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=customer_uuid)
        r = self.session.delete(url, headers=self._ro_headers)
        self.raise_from_response(r)

    def update(self, customer_uuid, customer):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=customer_uuid)
        r = self.session.put(url, json=customer, headers=self._rw_headers)
        self.raise_from_response(r)
