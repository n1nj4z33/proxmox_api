"""Module for volume resource."""

from proxmoxapi.resource import Resource


class Volume(Resource):
    """Class for volume resource."""
    # pylint: disable=too-few-public-methods

    def __init__(self, api, node_id, storage_id, volume_id):
        """
        :param api: The instance of :class:`ProxmoxAPI
            <proxmoxapi.api.ProxmoxAPI>`.
        :param str node_id: The cluster node name.
        :param str storage_id: The storage identifier.
        :param str volume_id: The volume identifier.
        """
        super(Volume, self).__init__(api)
        self.node_id = node_id
        self.storage_id = storage_id
        self.volume_id = volume_id
        self.url = "nodes/{node_id}/storage/{storage_id}/content/{volume_id}".format( # pylint: disable=line-too-long
            node_id=self.node_id,
            storage_id=self.storage_id,
            volume_id=self.volume_id)

    def _get(self):
        """Get volume attributes.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.send_request("GET")
