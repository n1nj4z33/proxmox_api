"""Module for storage_id resource."""

from proxmoxapi.resource import Resource
from proxmoxapi.nodes.storage.content.content import Content
from proxmoxapi.nodes.storage.upload import Upload


class Storage(Resource):
    """Class for storage_id resource."""

    def __init__(self, api, node_id, storage_id):
        """
        :param api: The instance of :class:`ProxmoxAPI
            <proxmoxapi.api.ProxmoxAPI>`.
        :param str node_id: The cluster node name.
        :param str storage_id: The storage identifier.
        """
        super(Storage, self).__init__(api)
        self.node_id = node_id
        self.storage_id = storage_id
        self.url = "nodes/{node_id}/storage/{storage_id}".format(
            node_id=self.node_id,
            storage_id=self.storage_id)

    def _get(self):
        """Get node storage configuration.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.send_request("GET")

    @property
    def content(self):
        """Property to get content resource.

        :returns: The instance of :class:`Content
            <proxmoxapi.nodes.storage.content.Content>`.
        """
        return Content(self.api, self.node_id, self.storage_id)

    @property
    def upload(self):
        """Property to get upload resource.

        :returns: The instance of :class:`Upload
            <proxmoxapi.nodes.storage.upload.Upload>`.
        """
        return Upload(self.api, self.node_id, self.storage_id)
