# -*- coding: utf-8 -*-
"""Module for storages resource."""

from .resource import Resource
from .storage.storage import Storage


class Storages(Resource):
    """Class for storages resource."""

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

        :returns: :class:`Storage <.storage.storage.Storage>`.
        """
        return Storage(self.api, storage_id)
