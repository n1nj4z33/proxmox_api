# -*- coding: utf-8 -*-
"""
Module for stop resource.
"""

from proxmoxapi.resource import Resource


class Stop(Resource):
    """
    Class for stop resource.
    """

    def __init__(self, api, node_id, vm_id):
        """
        :param api: :class:`ProxmoxAPI <.api.ProxmoxAPI>`.
        :param str node_id: The cluster node name.
        :param int vm_id: The (unique) ID of the VM.
        """
        super(Stop, self).__init__(api)
        self.node_id = node_id
        self.vm_id = vm_id
        self.url = "nodes/{node_id}/qemu/{vm_id}/status/stop".format(
            node_id=self.node_id,
            vm_id=self.vm_id)

    def _post(self):
        """
        Stop virtual machine.

        :returns: :class:`requests.Response`.
        """
        return self.send_request("POST")

    def __call__(self):
        """
        Stop virtual machine.

        :returns: :class:`UPID <proxmoxapi.nodes.tasks.upid.UPID>`.
        """
        response = self._post()
        task_id = response.json()["data"]
        return self.api.nodes.node(self.node_id).tasks.get_task_by_task_id(task_id)
