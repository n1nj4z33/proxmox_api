# -*- coding: utf-8 -*-
"""Module for config resource."""

from proxmox_api.resource import Resource


class Config(Resource):
    """
    Class for config resource.
    """

    def __init__(self, api, node_id, vm_id):
        """
        :param api: :class:`ProxmoxAPI <proxmox_api.api.ProxmoxAPI>`.
        :param str node_id: The cluster node name.
        :param int vm_id: The (unique) ID of the VM.
        """
        super(Config, self).__init__(api)
        self.node_id = node_id
        self.vm_id = vm_id
        self.url = "nodes/%s/qemu/%s/config" % (self.node_id, self.vm_id)

    def _get(self):
        """
        Get current virtual machine configuration.
        This does not include pending configuration changes.

        :returns: :class:`requests.Response`
        """
        return self.send_request("GET")

    def _put(self, name=None):
        """
        Set virtual machine options (synchrounous API).

        :returns: :class:`requests.Response`.
        """
        params = dict(name=name)
        return self.send_request("PUT", params=params)

    def edit(self, options):
        """
        Edit virtual machine.

        :param options: The instance of
            :class:`QemuVirtualMachineOptions
            <proxmox_api.nodes.qemu.options.QemuVirtualMachineOptions>`.

        :returns: :class:`requests.Response`.
        """
        return self._put(name=options.name)
