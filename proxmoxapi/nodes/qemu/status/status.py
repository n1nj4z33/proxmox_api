# -*- coding: utf-8 -*-
"""Module for status resource."""

from proxmoxapi.resource import Resource
from proxmoxapi.nodes.qemu.status.start import Start
from proxmoxapi.nodes.qemu.status.stop import Stop


class Status(Resource):
    """Class for status resource."""

    def __init__(self, api, node_id, vm_id):
        """
        :param api: :class:`ProxmoxAPI <.api.ProxmoxAPI>.`
        :param str node_id: The cluster node name.
        :param int vm_id: The (unique) ID of the VM.
        """
        super(Status, self).__init__(api)
        self.node_id = node_id
        self.vm_id = vm_id
        self.url = "nodes/%s/qemu/%s/status" % (self.node_id, self.vm_id)

    def _get(self):
        """
        Directory index.

        :returns: :class:`requests.Response`.
        """
        return self.send_request("GET")

    @property
    def start(self):
        """
        Property to get start resource.

        :returns: :class:`Start <proxmoxapi.nodes.qemu.status.start.Start>`.
        """
        return Start(self.api, self.node_id, self.vm_id)

    @property
    def stop(self):
        """
        Property to get stop resource.

        :returns: :class:`Stop <proxmoxapi.nodes.qemu.status.stop.Stop>`.
        """
        return Stop(self.api, self.node_id, self.vm_id)
