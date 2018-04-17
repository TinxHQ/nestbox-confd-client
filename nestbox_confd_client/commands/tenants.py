# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from nestbox_confd_client.command import ConfdCommand


class TenantsCommand(ConfdCommand):

    resource = 'tenants'
    _ro_headers = {'Accept': 'application/json'}

    def get_account_summaries(self, tenant_uuid):
        url = '{base}/{uuid}/summary/accounts'.format(base=self.base_url, uuid=tenant_uuid)
        r = self.session.get(url, headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()
