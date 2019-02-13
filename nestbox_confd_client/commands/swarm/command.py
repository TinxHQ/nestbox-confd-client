# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from nestbox_confd_client.command import ConfdCommand


class ConfdSwarmCommand(ConfdCommand):

    namespace = 'swarm'

    def __init__(self, client):
        super(ConfdSwarmCommand, self).__init__(client)
        self.base_url = self._client.url(self.namespace, self.resource)
