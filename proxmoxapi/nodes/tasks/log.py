"""Module for log resource."""

from proxmoxapi.resource import Resource


class Log(Resource):
    """Class for log resource."""
    # pylint: disable=too-few-public-methods

    def __init__(self, api, node_id, task_id):
        """
        :param api: The instance of :class:`ProxmoxAPI
            <proxmoxapi.api.ProxmoxAPI>`.
        :param str node_id: The cluster node name.
        :param str task_id: The task UPID.
        """
        super(Log, self).__init__(api)
        self.node_id = node_id
        self.task_id = task_id
        self.url = "nodes/{node_id}/tasks/{task_id}/log".format(
            node_id=self.node_id,
            task_id=self.task_id)

    def _get(self):
        """Read task log.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.send_request("GET")
