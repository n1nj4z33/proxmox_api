# -*- coding: utf-8 -*-
"""Module for start resource."""

from proxmoxapi.resource import Resource


class Start(Resource):
    """Class for start resource."""

    def __init__(self, api, node_id, vm_id):
        """
        :param api: :class:`ProxmoxAPI <.api.ProxmoxAPI>`.
        :param str node_id: The cluster node name.
        :param int vm_id: The (unique) ID of the VM.
        """
        super(Start, self).__init__(api)
        self.node_id = node_id
        self.vm_id = vm_id
        self.url = "nodes/{node_id}/qemu/{vm_id}/status/start".format(
            node_id=self.node_id,
            vm_id=self.vm_id)

    def _post(self):
        """
        Start virtual machine.

        :returns: :class:`requests.Response`.
        """
        return self.send_request("POST")

    def __call__(self):
        """
        Start virtual machine.

        :returns: :class:`UPID <proxmoxapi.nodes.tasks.upid.UPID>`.
        """
        response = self._post()
        task_id = response.json()["data"]
        return self.api.nodes.node(self.node_id).tasks.get_task_by_task_id(task_id)
