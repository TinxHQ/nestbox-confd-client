# Copyright 2018-2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from nestbox_confd_client.command import ConfdCommand


class ResellersCommand(ConfdCommand):
    resource = 'resellers'

    def create(self, reseller, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.post(self.base_url, json=reseller, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def list(self, tenant_uuid=None, **kwargs):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.get(self.base_url, headers=headers, params=kwargs)
        self.raise_from_response(r)
        return r.json()

    def get(self, reseller_uuid, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{reseller_uuid}'
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, reseller_uuid, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{reseller_uuid}'
        r = self.session.delete(url, headers=headers)
        self.raise_from_response(r)

    def update(self, reseller_uuid, reseller, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{reseller_uuid}'
        r = self.session.put(url, json=reseller, headers=headers)
        self.raise_from_response(r)
