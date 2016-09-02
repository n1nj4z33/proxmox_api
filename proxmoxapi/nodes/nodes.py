# -*- coding: utf-8 -*-
"""Module for nodes resource."""

from proxmox_api.resource import Resource
from proxmox_api.nodes.node import Node


class Nodes(Resource):
    """Class for nodes resource."""

    url = "nodes"

    def _get(self):
        """
        Cluster node index.

        :returns: :class:`requests.Response`.
        """
        return self.send_request("GET")

    def node(self, node_id):
        """
        Method to get node resource.

        :param str node_id: The cluster node name.

        :returns: :class:`Node <proxmox_api.nodes.node.Node>`.
        """
        return Node(self.api, node_id)

    def get_all_nodes(self):
        """
        Method to get all nodes.

        :returns: The list of nodes.
        """
        response = self._get()
        data = response.json()["data"]
        return [self.node(node["node"]) for node in data]

    def get_node_by_task_id(self, task_id):
        """
        Method to get node by task_id.

        :param task_id: The UPID of task.

        :returns: :class:`Node <proxmox_api.nodes.node.Node>`.
        """
        node_id = task_id.split(":")[1]
        return self.node(node_id)

