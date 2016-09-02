# -*- coding: utf-8 -*-
"""Module for content resource."""

from proxmoxapi.resource import Resource
from proxmoxapi.nodes.storage.content.volume import Volume


class Content(Resource):
    """Class for content resource."""

    def __init__(self, api, node_id, storage_id):
        """
        :param api: :class:`ProxmoxAPI <proxmoxapi.api.ProxmoxAPI>`.
        :param str node_id: The cluster node name.
        :param str storage_id: The storage identifier.
        """
        super(Content, self).__init__(api)
        self.node_id = node_id
        self.storage_id = storage_id
        self.url = "nodes/%s/storage/%s/content" % (self.node_id, self.storage_id)

    def _get(self):
        """
        List storage content.

        :returns: :class:`requests.Response`.
        """
        return self.send_request("GET")

    def volume(self, volume_id):
        """
        Method to get volume resource.

        :param str volume_id: The volume identifier.

        :returns: The instanse of
            :class:`Volume <proxmoxapi.nodes.storage.content.volume.Volume>`.
        """
        return Volume(self.api, self.node_id, self.storage_id, volume_id)

    def get_all_contents(self):
        """
        Method to get all contents.

        :return: The list of contents.
        """
        response = self._get()
        data = response.json()["data"]
        return [self.volume(volume["volid"]) for volume in data]
