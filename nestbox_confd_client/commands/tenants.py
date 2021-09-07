# Copyright 2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from nestbox_confd_client.command import ConfdCommand


class TenantsCommand(ConfdCommand):

    resource = 'tenants'
    _ro_headers = {'Accept': 'application/json'}

    def get(self, tenant_uuid):
        url = f'{self.base_url}/{tenant_uuid}'
        r = self.session.get(url, headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()
