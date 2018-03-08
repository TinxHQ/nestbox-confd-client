# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from requests import HTTPError


class ConfdError(HTTPError):

    def __init__(self, response):
        try:
            body = response.json()
        except ValueError:
            raise InvalidConfdError()

        self.status_code = response.status_code
        try:
            # TODO test is correct
            self.message = body['message']
            self.error_id = body['error_id']
            self.details = body['details']
            self.timestamp = body['timestamp']
            if body.get('resource', None):
                self.resource = body['resource']
        except KeyError:
            raise InvalidConfdError()

        exception_message = '{e.message}: {e.details}'.format(e=self)
        super(ConfdError, self).__init__(exception_message, response=response)


class ConfdServiceUnavailable(ConfdError):
    pass


class InvalidConfdError(Exception):
    pass
