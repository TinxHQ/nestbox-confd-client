# Copyright 2021-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from nestbox_confd_client.command import ConfdCommand


class TenantsCommand(ConfdCommand):
    resource = 'tenants'

    def get(self, tenant_uuid):
        headers = self._get_headers()
        url = f'{self.base_url}/{tenant_uuid}'
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()
