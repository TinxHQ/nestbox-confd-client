# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from nestbox_confd_client.command import ConfdCommand


class EnginesCommand(ConfdCommand):

    resource = 'engines'
    _rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def create_account_event(self, instance_uuid, event):
        url = '{base}/instances/{uuid}/accounts/events'.format(base=self.base_url, uuid=instance_uuid)
        r = self.session.post(url, json=event, headers=self._rw_headers)
        self.raise_from_response(r)
