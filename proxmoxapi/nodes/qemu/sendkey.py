# -*- coding: utf-8 -*-
"""Module for sendkey resource."""

from proxmox_api.resource import Resource


class SendKey(Resource):
    """Class for sendkey resource."""

    def __init__(self, api, node_id, vm_id):
        """
        :param api: :class:`ProxmoxAPI <proxmox_api.api.ProxmoxAPI>`.
        :param str node_id: The cluster node name.
        :param int vm_id: The (unique) ID of the VM.
        """
        super(SendKey, self).__init__(api)
        self.node_id = node_id
        self.vm_id = vm_id
        self.url = "nodes/%s/qemu/%s/sendkey" % (self.node_id, self.vm_id)

    def _put(self, key):
        """
        Send key event to virtual machine.

        :param str key: The key (qemu monitor encoding).

        :returns: :class:`requests.Response`.
        """
        params = dict(key=key)
        return self.send_request("PUT", params=params)

    def __call__(self, key):
        """
        Send key event to virtual machine.

        :param str key: The key (qemu monitor encoding).
        """
        self._put(key)
