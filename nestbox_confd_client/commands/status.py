# Copyright 2020-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from nestbox_confd_client.command import ConfdCommand


class StatusCommand(ConfdCommand):
    resource = 'status'

    def check(self):
        headers = self._get_headers()
        r = self.session.head(self.base_url, headers=headers)
        self.raise_from_response(r)
