# -*- coding: utf-8 -*-
"""Module for cluster nextid resource."""

from .resource import Resource


class NextID(Resource):
    """Class for cluster nextid resource."""

    url = "cluster/nextid"

    def _get(self):
        """
        Get next free VMID.
        If you pass an VMID it will raise an error if the ID is already used.

        :returns: :class:`requests.Response`.
        """
        return self.send_request("GET")

    def get_vmid(self):
        """
        Get next free VMID.
        If you pass an VMID it will raise an error if the ID is already used.

        :returns: The next VMID of cluster.
        """
        response = self._get()
        return response.json()["data"]
