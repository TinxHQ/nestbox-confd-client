# Copyright 2018 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from nestbox_confd_client.commands.swarm.command import ConfdSwarmCommand


class CredentialsCommand(ConfdSwarmCommand):

    resource = 'credentials'

    def __init__(self, client):
        super().__init__(client)

    def list(self, **params):
        url = self.base_url
        headers = self._get_headers(**params)
        response = self.session.get(url, headers=headers, params=params)
        self.raise_from_response(response)
        return response.json()

    def create(self, credential, **kwargs):
        url = self.base_url
        headers = self._get_headers(write=True, **kwargs)
        response = self.session.post(url, json=credential, headers=headers)
        self.raise_from_response(response)
        return response.json()

    def get(self, credential_uuid, **kwargs):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=credential_uuid)
        headers = self._get_headers(**kwargs)
        response = self.session.get(url, headers=headers)
        self.raise_from_response(response)
        return response.json()

    def update(self, credential_uuid, credential, **kwargs):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=credential_uuid)
        headers = self._get_headers(write=True, **kwargs)
        response = self.session.put(url, json=credential, headers=headers)
        self.raise_from_response(response)

    def delete(self, credential_uuid, **kwargs):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=credential_uuid)
        headers = self._get_headers(**kwargs)
        response = self.session.delete(url, headers=headers)
        self.raise_from_response(response)
