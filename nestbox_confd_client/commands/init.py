# Copyright 2018-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from nestbox_confd_client.command import ConfdCommand


class InitCommand(ConfdCommand):
    resource = 'init'

    def run(self, init):
        headers = self._get_headers()
        r = self.session.post(self.base_url, json=init, headers=headers)
        self.raise_from_response(r)
