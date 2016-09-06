# -*- coding: utf-8 -*-
"""Module for storages resource."""

from proxmoxapi.resource import Resource
from proxmoxapi.storage.storage import Storage


class Storages(Resource):
    """Class for storages resource."""
    # pylint: disable=too-few-public-methods

    url = "storage"

    def _get(self):
        """
        Storage index.

        :returns: :class:`requests.Response`.
        """
        return self.send_request("GET")

    def storage(self, storage_id):
        """
        Method to get storage resource.

        :param str storage_id: The storage identifier.

        :returns: :class:`Storage <proxmoxapi.storage.storage.Storage>`.
        """
        return Storage(self.api, storage_id)
