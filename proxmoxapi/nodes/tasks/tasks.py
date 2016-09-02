# -*- coding: utf-8 -*-
"""Module for tasks resource."""

from .resource import Resource
from .nodes.tasks.upid import UPID


class Tasks(Resource):
    """Class for tasks resource."""

    def __init__(self, api, node_id):
        """
        :param api: :class:`ProxmoxAPI <.api.ProxmoxAPI>`.
        :param str node_id: The cluster node name.
        """
        super(Tasks, self).__init__(api)
        self.node_id = node_id
        self.url = "nodes/%s/tasks" % self.node_id

    def _get(self):
        """
        Read task list for one node (finished tasks).

        :returns: :class:`requests.Response`.
        """
        return self.send_request("GET")

    def upid(self, task_id):
        """
        Method to get task by task_id.

        :param str task_id: The task UPID.
        :returns: :class:`UPID <.nodes.tasks.upid.UPID>`.
        """
        return UPID(self.api, self.node_id, task_id)

    def get_task_by_task_id(self, task_id):
        """Get task object by task identifier."""
        node = self.api.nodes.get_node_by_task_id(task_id)
        return node.tasks.upid(task_id)
