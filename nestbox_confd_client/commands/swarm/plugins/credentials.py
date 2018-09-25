# Copyright 2018 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from nestbox_confd_client.commands.swarm.command import ConfdSwarmCommand


class CredentialsCommand(ConfdSwarmCommand):

    resource = 'credentials'
    _ro_headers = {'Accept': 'application/json'}
    _rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def __init__(self, client):
        super().__init__(client)

    def list(self, **params):
        url = self.base_url
        response = self.session.get(url, headers=self._ro_headers, params=params)
        self.raise_from_response(response)
        return response.json()

    def create(self, credential):
        url = self.base_url
        response = self.session.post(url, json=credential, headers=self._rw_headers)
        self.raise_from_response(response)
        return response.json()

    def get(self, credential_uuid):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=credential_uuid)
        response = self.session.get(url, headers=self._ro_headers)
        self.raise_from_response(response)
        return response.json()

    def update(self, credential_uuid, credential):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=credential_uuid)
        response = self.session.put(url, json=credential, headers=self._rw_headers)
        self.raise_from_response(response)

    def delete(self, credential_uuid):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=credential_uuid)
        response = self.session.delete(url, headers=self._ro_headers)
        self.raise_from_response(response)
