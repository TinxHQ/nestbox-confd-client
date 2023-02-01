# Copyright 2018-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from nestbox_confd_client.command import ConfdCommand


class UsersCommand(ConfdCommand):
    resource = 'users'

    def create(self, user):
        headers = self._get_headers()
        r = self.session.post(self.base_url, json=user, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def list(self):
        headers = self._get_headers()
        r = self.session.get(self.base_url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def get(self, user_uuid):
        headers = self._get_headers()
        url = f'{self.base_url}/{user_uuid}'
        r = self.session.get(url, headers=headers)
        self.raise_from_response(r)
        return r.json()

    def delete(self, user_uuid):
        headers = self._get_headers()
        url = f'{self.base_url}/{user_uuid}'
        r = self.session.delete(url, headers=headers)
        self.raise_from_response(r)

    def update(self, user_uuid, user):
        headers = self._get_headers()
        url = f'{self.base_url}/{user_uuid}'
        r = self.session.put(url, json=user, headers=headers)
        self.raise_from_response(r)
