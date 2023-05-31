# Copyright 2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from nestbox_confd_client.command import ConfdCommand


class PluginsCommand(ConfdCommand):
    resource = 'plugins'

    def create(self, plugin, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.post(self.base_url, json=plugin, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, plugin_uuid, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{plugin_uuid}'
        r = self.session.delete(url, headers=headers)
        self.raise_from_response(r)

    def get(self, plugin_uuid, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{plugin_uuid}'
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def list(self, tenant_uuid=None, **kwargs):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.get(self.base_url, headers=headers, params=kwargs)
        self.raise_from_response(r)
        return r.json()

    def update(self, plugin_uuid, plugin, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{plugin_uuid}'
        r = self.session.put(url, json=plugin, headers=headers)
        self.raise_from_response(r)
