# Copyright 2018 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging

from stevedore import extension

logger = logging.getLogger(__name__)

plugin_names = set()


class Swarm(object):
    """Proxy class for calling resources that need swarm infos"""

    namespace = 'nestbox_confd_client.commands.swarm.plugins'

    def __init__(self, client):
        self._client = client
        self._load_plugins()

    def __getattribute__(self, name):
        attribute = super(Swarm, self).__getattribute__(name)
        if name in plugin_names:
            return attribute(self._client)
        return attribute

    def _load_plugins(self):

        def set_extension_instance_as_attribute(extension_):
            setattr(self, extension_.name, extension_.plugin)
            plugin_names.add(extension_.name)

        extension_manager = extension.ExtensionManager(
            self.namespace,
        )
        try:
            extension_manager.map(set_extension_instance_as_attribute)
        except RuntimeError:
            logger.warning('No commands found')
