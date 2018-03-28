# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from nestbox_confd_client.command import ConfdCommand


class UsersCommand(ConfdCommand):

    resource = 'users'
    _ro_headers = {'Accept': 'application/json'}
    _rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def create(self, user):
        r = self.session.post(self.base_url, json=user, headers=self._rw_headers)
        self.raise_from_response(r)
        return r.json()

    def list(self):
        r = self.session.get(self.base_url, headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()

    def get(self, user_uuid):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=user_uuid)
        r = self.session.get(url, headers=self._ro_headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, user_uuid):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=user_uuid)
        r = self.session.delete(url, headers=self._ro_headers)
        self.raise_from_response(r)

    def update(self, user_uuid, user):
        url = '{base}/{uuid}'.format(base=self.base_url, uuid=user_uuid)
        r = self.session.put(url, json=user, headers=self._rw_headers)
        self.raise_from_response(r)
