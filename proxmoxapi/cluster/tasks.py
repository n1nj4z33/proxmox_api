# -*- coding: utf-8 -*-
"""Module for tasks resource."""

from proxmoxapi.resource import Resource


class Tasks(Resource):
    """Class for tasks resource."""

    url = "cluster/tasks"

    def _get(self):
        """
        List recent tasks (cluster wide).

        :returns: :class:`requests.Response`.
        """
        return self.send_request("GET")
