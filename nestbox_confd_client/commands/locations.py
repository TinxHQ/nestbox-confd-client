# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from nestbox_confd_client.command import ConfdCommand


class LocationsCommand(ConfdCommand):

    resource = 'locations'
    _ro_headers = {'Accept': 'application/json'}
    _rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def create(self, location):
        r = self.session.post(self.base_url, json=location, headers=self._rw_headers)
        self.raise_from_response(r)
        return r.json()

    def list(self):
        r = self.session.get(self.base_url, headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()

    def get(self, location_uuid):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=location_uuid)
        r = self.session.get(url, headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, location_uuid):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=location_uuid)
        r = self.session.delete(url, headers=self._ro_headers)
        self.raise_from_response(r)

    def update(self, location_uuid, location):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=location_uuid)
        r = self.session.put(url, json=location, headers=self._rw_headers)
        self.raise_from_response(r)

    def update_wazo_tenants(self, location_uuid, wazo_tenants):
        url = '{base}/{uuid}/wazo/tenants'.format(base=self.base_url, uuid=location_uuid)
        body = {
            'wazo_tenants': [{'uuid': wazo_tenant['uuid'],
                              'instance_uuid': wazo_tenant['instance_uuid'],
                              'credential_uuid': wazo_tenant['credential_uuid']}
                             for wazo_tenant in wazo_tenants]
        }
        r = self.session.put(url, json=body, headers=self._rw_headers)
        self.raise_from_response(r)
