# -*- coding: utf-8 -*-
"""Module for storage resource."""

from proxmoxapi.resource import Resource


class Storage(Resource):
    """Class for storage resource."""

    def __init__(self, api, storage_id):
        """
        :param api: :class:`ProxmoxAPI <proxmoxapi.api.ProxmoxAPI>`.
        :param str storage_id: The storage identifier.
        """
        super(Storage, self).__init__(api)
        self.storage_id = storage_id
        self.url = "storage/%s" % self.storage_id

    def _get(self):
        """
        Read storage configuration.

        :returns: :class:`requests.Response`.
        """
        return self.send_request("GET")
