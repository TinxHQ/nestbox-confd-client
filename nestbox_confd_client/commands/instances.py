# Copyright 2020-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from nestbox_confd_client.command import ConfdCommand


class InstancesCommand(ConfdCommand):
    resource = 'instances'

    def list(self, tenant_uuid=None, **params):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.get(self.base_url, headers=headers, params=params)
        self.raise_from_response(r)
        return r.json()
