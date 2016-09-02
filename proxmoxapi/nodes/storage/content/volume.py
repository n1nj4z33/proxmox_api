# -*- coding: utf-8 -*-
"""Module for volume resource."""

from .resource import Resource


class Volume(Resource):
    """Class for volume resource."""

    def __init__(self, api, node_id, storage_id, volume_id):
        """
        :param api: :class:`ProxmoxAPI <.api.ProxmoxAPI>`.
        :param str node_id: The cluster node name.
        :param str storage_id: The storage identifier.
        :param str volume_id: The volume identifier.
        """
        super(Volume, self).__init__(api)
        self.node_id = node_id
        self.storage_id = storage_id
        self.volume_id = volume_id
        self.url = "nodes/%s/storage/%s/content/%s" % (self.node_id,
                                                       self.storage_id,
                                                       self.volume_id)

    def _get(self):
        """
        Get volume attributes.

        :returns: :class:`requests.Response`.
        """
        return self.send_request("GET")
