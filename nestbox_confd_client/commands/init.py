# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from nestbox_confd_client.command import ConfdCommand


class InitCommand(ConfdCommand):

    resource = 'init'
    _rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def run(self, init):
        r = self.session.post(self.base_url, json=init, headers=self._rw_headers)
        self.raise_from_response(r)
