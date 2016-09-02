# -*- coding: utf-8 -*-
"""Module for storage resource."""

from .resource import Resource
from .nodes.storage.storage import Storage


class Storages(Resource):
    """Class for storage resource."""

    def __init__(self, api, node_id):
        """
        :param api: :class:`ProxmoxAPI <.api.ProxmoxAPI>`.
        :param str node_id: The cluster node name.
        """
        super(Storages, self).__init__(api)
        self.node_id = node_id
        self.url = "nodes/%s/storage" % self.node_id

    def _get(self):
        """
        Get status for all datastores.

        :returns: :class:`requests.Response`.
        """
        return self.send_request("GET")

    def storage(self, storage_id):
        """
        Method to get storage resource.

        :param str storage_id: The storage identifier.

        :returns: :class:`Storage <.nodes.storage.storage.Storage>`.
        """
        return Storage(self.api, self.node_id, storage_id)
