"""Module for version resource."""

from proxmoxapi.resource import Resource


class Version(Resource):
    """Class for version resource."""
    # pylint: disable=too-few-public-methods

    url = "version"

    def _get(self):
        """API version details.
        The result also includes the global datacenter confguration.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.send_request("GET")
