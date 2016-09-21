"""Module for tasks resource."""

from proxmoxapi.resource import Resource


class Tasks(Resource):
    """Class for tasks resource."""
    # pylint: disable=too-few-public-methods

    url = "cluster/tasks"

    def _get(self):
        """List recent tasks (cluster wide).

        :returns: The instance of :class:`requests.Response`.
        """
        return self.send_request("GET")
