"""Module for storage resource."""

from proxmoxapi.resource import Resource
from proxmoxapi.nodes.storage.storage import Storage


class Storages(Resource):
    """Class for storage resource."""
    # pylint: disable=too-few-public-methods

    def __init__(self, api, node_id):
        """
        :param api: The instance of :class:`ProxmoxAPI
            <proxmoxapi.api.ProxmoxAPI>`.
        :param str node_id: The cluster node name.
        """
        super(Storages, self).__init__(api)
        self.node_id = node_id
        self.url = "nodes/{node_id}/storage".format(
            node_id=self.node_id)

    def _get(self):
        """Get status for all datastores.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.send_request("GET")

    def storage(self, storage_id):
        """Method to get storage resource.

        :param str storage_id: The storage identifier.

        :returns: The instance of :class:`Storage
            <proxmoxapi.nodes.storage.storage.Storage>`.
        """
        return Storage(self.api, self.node_id, storage_id)
