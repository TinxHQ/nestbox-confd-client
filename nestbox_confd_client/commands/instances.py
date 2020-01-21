# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from nestbox_confd_client.command import ConfdCommand


class InstancesCommand(ConfdCommand):

    resource = 'instances'
    _ro_headers = {'Accept': 'application/json'}

    def list(self, tenant_uuid=None, **params):
        headers = dict(self._ro_headers)
        tenant_uuid = tenant_uuid or self._client.tenant()
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid

        r = self.session.get(self.base_url, headers=headers, params=params)
        self.raise_from_response(r)
        return r.json()
