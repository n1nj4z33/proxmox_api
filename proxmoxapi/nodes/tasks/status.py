"""Module for status resource."""

from proxmoxapi.resource import Resource


class Status(Resource):
    """Class for status resource."""

    def __init__(self, api, node_id, task_id):
        """
        :param api: The instance of :class:`ProxmoxAPI
            <proxmoxapi.api.ProxmoxAPI>`.
        :param str node_id: The cluster node name.
        :param str task_id: The task UPID.
        """
        super(Status, self).__init__(api)
        self.node_id = node_id
        self.task_id = task_id
        self.url = "nodes/{node_id}/tasks/{task_id}/status".format(
            node_id=self.node_id,
            task_id=self.task_id)

    def _get(self):
        """Read task status.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.send_request("GET")

    def get_status(self):
        """Read task status.

        :returns: Task status by UPID.
        """
        response = self._get()
        return response.json()["data"]["status"]

    def get_exitstatus(self):
        """Read task exitstatus.

        :returns: Task exitstatus by UPID.
        """
        response = self._get()
        return response.json()["data"]["exitstatus"]
