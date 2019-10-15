# Copyright 2018-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client.command import RESTCommand

from .exceptions import (
    ConfdError,
    ConfdServiceUnavailable,
    InvalidConfdError,
)


class ConfdCommand(RESTCommand):

    _ro_headers = {'Accept': 'application/json'}
    _rw_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    @staticmethod
    def raise_from_response(response):
        if response.status_code == 503:
            raise ConfdServiceUnavailable(response)

        try:
            raise ConfdError(response)
        except InvalidConfdError:
            RESTCommand.raise_from_response(response)

    def _get_headers(self, write=False, **kwargs):
        headers = dict(self._rw_headers) if write else dict(self._ro_headers)
        tenant_uuid = kwargs.pop('tenant_uuid', self._client.tenant())
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid
        return headers
