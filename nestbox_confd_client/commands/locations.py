# Copyright 2018-2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from nestbox_confd_client.command import ConfdCommand


class LocationsCommand(ConfdCommand):
    resource = 'locations'

    def create(self, location, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.post(self.base_url, json=location, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def list(self, tenant_uuid=None, **kwargs):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.get(self.base_url, headers=headers, params=kwargs)
        self.raise_from_response(r)
        return r.json()

    def get(self, location_uuid, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{location_uuid}'
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, location_uuid, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{location_uuid}'
        r = self.session.delete(url, headers=headers)
        self.raise_from_response(r)

    def update(self, location_uuid, location, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{location_uuid}'
        r = self.session.put(url, json=location, headers=headers)
        self.raise_from_response(r)

    def update_wazo_tenants(self, location_uuid, wazo_tenants, tenant_uuid=None):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        url = f'{self.base_url}/{location_uuid}/wazo/tenants'
        body = {
            'wazo_tenants': [
                {
                    'uuid': wazo_tenant['uuid'],
                    'instance_uuid': wazo_tenant['instance_uuid'],
                    'credential_uuid': wazo_tenant['credential_uuid'],
                }
                for wazo_tenant in wazo_tenants
            ]
        }
        r = self.session.put(url, json=body, headers=headers)
        self.raise_from_response(r)
