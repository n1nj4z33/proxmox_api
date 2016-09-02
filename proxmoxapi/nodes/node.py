# -*- coding: utf-8 -*-
"""Module for node resource."""

from proxmoxapi.resource import Resource
from proxmoxapi.nodes.storage.storages import Storages
from proxmoxapi.nodes.qemu.qemu import QEMU
from proxmoxapi.nodes.tasks.tasks import Tasks


class Node(Resource):
    """Class for node resource."""

    def __init__(self, api, node_id):
        """
        :param api: :class:`ProxmoxAPI <proxmoxapi.api.ProxmoxAPI>`.
        :param str node_id: The cluster node name.
        """
        super(Node, self).__init__(api)
        self.node_id = node_id
        self.url = "nodes/%s" % self.node_id

    def _get(self):
        """
        Get node index.

        :returns: :class:`requests.Response`.
        """
        return self.send_request("GET")

    @property
    def storages(self):
        """
        Property to get storages resource.

        :returns: :class:`Storages <proxmoxapi.nodes.node_id.storages.Storages>`.
        """
        return Storages(self.api, self.node_id)

    @property
    def qemu(self):
        """
        Property to get qemu resource.

        :returns: :class:`QEMU <proxmoxapi.nodes.qemu.qemu.QEMU>`.
        """
        return QEMU(self.api, self.node_id)

    @property
    def tasks(self):
        """
        Property to get tasks resource.

        :returns: :class:`Tasks <proxmoxapi.nodes.tasks.tasks.Tasks>`.
        """
        return Tasks(self.api, self.node_id)
