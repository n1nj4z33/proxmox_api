# -*- coding: utf-8 -*-
"""Module for vmid resource."""

from proxmox_api.resource import Resource
from proxmox_api.nodes.qemu.status.status import Status
from proxmox_api.nodes.qemu.sendkey import SendKey
from proxmox_api.nodes.qemu.config import Config


class VMID(Resource):
    """Class for vmid resource."""

    def __init__(self, api, node_id, vm_id):
        """
        :param api: :class:`ProxmoxAPI <proxmox_api.api.ProxmoxAPI>`.
        :param str node_id: The cluster node name.
        :param int vm_id: The (unique) ID of the VM.
        """
        super(VMID, self).__init__(api)
        self.node_id = node_id
        self.vm_id = vm_id
        self.url = "nodes/%s/qemu/%s" % (self.node_id, self.vm_id)

    def _get(self):
        """
        Qemu virtual machine index (per node).

        :returns: :class:`requests.Response`.
        """
        return self.send_request("GET")

    def _delete(self):
        """
        Destroy the vm (also delete all used/owned volumes).

        :returns: :class:`requests.Response`.
        """
        return self.send_request("DELETE")

    def delete(self):
        """
        Destroy the vm (also delete all used/owned volumes).

        :returns: :class:`UPID <proxmox_api.nodes.tasks.upid.UPID>`.
        """
        response = self._delete()
        task_id = response.json()["data"]
        return self.api.nodes.node(self.node_id).tasks.get_task_by_task_id(task_id)

    @property
    def status(self):
        """
        Property to get status resource.

        :returns: :class:`Status <proxmox_api.nodes.qemu.status.status.Status>`.
        """
        return Status(self.api, self.node_id, self.vm_id)

    @property
    def sendkey(self):
        """
        Property to get sendkey resource.

        :returns: :class:`SendKey <proxmox_api.nodes.qemu.sendkey.SendKey>`.
        """
        return SendKey(self.api, self.node_id, self.vm_id)

    @property
    def config(self):
        """
        Property to get config resource.

        :returns: :class:`Config <proxmox_api.nodes.qemu.config.Config>`.
        """
        return Config(self.api, self.node_id, self.vm_id)
