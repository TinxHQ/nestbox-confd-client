# Copyright 2018-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from nestbox_confd_client.command import ConfdCommand


class CustomersCommand(ConfdCommand):

    resource = 'customers'

    def create(self, customer):
        headers = self._get_headers()
        r = self.session.post(self.base_url, json=customer, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def list(self, **kwargs):
        headers = self._get_headers(**kwargs)
        r = self.session.get(self.base_url, headers=headers, params=kwargs)
        self.raise_from_response(r)
        return r.json()

    def get(self, customer_uuid):
        headers = self._get_headers()
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=customer_uuid)
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, customer_uuid):
        headers = self._get_headers()
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=customer_uuid)
        r = self.session.delete(url, headers=headers)
        self.raise_from_response(r)

    def update(self, customer_uuid, customer):
        headers = self._get_headers()
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=customer_uuid)
        r = self.session.put(url, json=customer, headers=headers)
        self.raise_from_response(r)
