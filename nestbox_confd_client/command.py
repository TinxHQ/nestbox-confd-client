# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_lib_rest_client.command import RESTCommand

from .exceptions import (
    ConfdError,
    ConfdServiceUnavailable,
    InvalidConfdError,
)


class ConfdCommand(RESTCommand):

    @staticmethod
    def raise_from_response(response):
        if response.status_code == 503:
            raise ConfdServiceUnavailable(response)

        try:
            raise ConfdError(response)
        except InvalidConfdError:
            RESTCommand.raise_from_response(response)
