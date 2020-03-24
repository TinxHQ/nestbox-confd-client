# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from nestbox_confd_client.command import ConfdCommand


class StatusCommand(ConfdCommand):

    resource = 'status'

    def check(self):
        r = self.session.head(self.base_url, headers=self._ro_headers)
        self.raise_from_response(r)
