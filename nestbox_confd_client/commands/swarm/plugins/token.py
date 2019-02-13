# Copyright 2018 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from nestbox_confd_client.commands.swarm.command import ConfdSwarmCommand


class TokenCommand(ConfdSwarmCommand):

    resource = 'token'

    def get(self, **params):
        url = self.base_url
        headers = self._get_headers(**params)
        response = self.session.get(url, headers=headers, params=params)
        self.raise_from_response(response)
        return response.json()
