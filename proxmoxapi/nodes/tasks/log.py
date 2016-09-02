# -*- coding: utf-8 -*-
"""Module for log resource."""

from .resource import Resource


class Log(Resource):
    """Class for log resource."""

    def __init__(self, api, node_id, task_id):
        """
        :param api: :class:`ProxmoxAPI <.api.ProxmoxAPI>`.
        :param str node_id: The cluster node name.
        :param str task_id: The task UPID.
        """
        super(Log, self).__init__(api)
        self.node_id = node_id
        self.task_id = task_id
        self.url = "nodes/%s/tasks/%s/log" % (self.node_id, self.task_id)

    def _get(self):
        """
        Read task log.

        :returns: :class:`requests.Response`.
        """
        return self.send_request("GET")
