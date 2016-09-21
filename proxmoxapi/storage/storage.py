"""Module for storage resource."""

from proxmoxapi.resource import Resource


class Storage(Resource):
    """Class for storage resource."""
    # pylint: disable=too-few-public-methods

    def __init__(self, api, storage_id):
        """
        :param api: The instance of :class:`ProxmoxAPI
            <proxmoxapi.api.ProxmoxAPI>`.
        :param str storage_id: The storage identifier.
        """
        super(Storage, self).__init__(api)
        self.storage_id = storage_id
        self.url = "storage/{storage_id}".format(
            storage_id=self.storage_id)

    def _get(self):
        """Read storage configuration.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.send_request("GET")
