# Copyright 2019-2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from nestbox_confd_client.command import ConfdCommand


class AccountsCommand(ConfdCommand):
    resource = 'accounts'

    def list(self, tenant_uuid=None, **kwargs):
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.get(self.base_url, headers=headers, params=kwargs)
        self.raise_from_response(r)
        return r.json()

    def get_summaries(self, tenant_uuid=None):
        url = f'{self.base_url}/summary'
        headers = self._get_headers(tenant_uuid=tenant_uuid)
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()
