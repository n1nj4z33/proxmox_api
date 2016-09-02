# -*- coding: utf-8 -*-
"""Module for cluster resource."""

from proxmox_api.resource import Resource
from proxmox_api.cluster.nextid import NextID
from proxmox_api.cluster.tasks import Tasks


class Cluster(Resource):
    """Class for cluster resource."""

    url = "cluster"

    def _get(self):
        """
        Cluster index.

        :returns: :class:`requests.Response`
        """
        return self.send_request("GET")

    @property
    def nextid(self):
        """
        Property to get nextid resource.

        :returns: :class:`NextID <proxmox_api.cluster.nextid.NextID>`.
        """
        return NextID(self.api)

    @property
    def tasks(self):
        """
        Property to get tasks resource.

        :returns: :class:`Tasks <proxmox_api.cluster.tasks.Tasks>`.
        """
        return Tasks(self.api)
