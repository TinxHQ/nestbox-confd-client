# Copyright 2023-2024 The Wazo Authors  (see the AUTHORS file)
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

    def list_customer_installs(self, plugin_uuid, tenant_uuid=None, **kwargs):
        return self._list_installs(
            'customers', plugin_uuid, tenant_uuid=tenant_uuid, **kwargs
        )

    def list_location_installs(self, plugin_uuid, tenant_uuid=None, **kwargs):
        return self._list_installs(
            'locations', plugin_uuid, tenant_uuid=tenant_uuid, **kwargs
        )

    def list_reseller_installs(self, plugin_uuid, tenant_uuid=None, **kwargs):
        return self._list_installs(
            'resellers', plugin_uuid, tenant_uuid=tenant_uuid, **kwargs
        )

    def install_for_customer(self, plugin_uuid, customer_uuid, tenant_uuid=None):
        return self._install_for(
            'customers',
            plugin_uuid,
            {'customer_uuid': customer_uuid},
            tenant_uuid=tenant_uuid,
        )

    def install_for_location(self, plugin_uuid, location_uuid, tenant_uuid=None):
        return self._install_for(
            'locations',
            plugin_uuid,
            {'location_uuid': location_uuid},
            tenant_uuid=tenant_uuid,
        )

    def install_for_reseller(self, plugin_uuid, reseller_uuid, tenant_uuid=None):
        return self._install_for(
            'resellers',
            plugin_uuid,
            {'reseller_uuid': reseller_uuid},
            tenant_uuid=tenant_uuid,
        )

    def update(self, plugin_uuid, plugin, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{plugin_uuid}'
        r = self.session.put(url, json=plugin, headers=headers)
        self.raise_from_response(r)

    def _list_installs(self, resource_type, plugin_uuid, tenant_uuid=None, **kwargs):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{plugin_uuid}/installs/{resource_type}'
        params = dict(kwargs)
        if uuids := kwargs.get('uuids'):
            params['uuids'] = ','.join(uuids)

        r = self.session.get(url, headers=headers, params=params)
        self.raise_from_response(r)
        return r.json()

    def _install_for(self, resource_type, plugin_uuid, body, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{plugin_uuid}/installs/{resource_type}'
        r = self.session.post(url, headers=headers, json=body)
        self.raise_from_response(r)
        return r.json()
