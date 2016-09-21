"""Module for access resource."""

from proxmoxapi.resource import Resource
from proxmoxapi.access.ticket import Ticket


class Access(Resource):
    """Class for access resource."""
    # pylint: disable=too-few-public-methods

    url = "access"

    def _get(self):
        """Directory index.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.send_request("GET")

    @property
    def ticket(self):
        """Property to get ticket resource.

        :returns: The instance of :class:`Ticket
            <proxmoxapi.access.ticket.Ticket>`.
        """
        return Ticket(self.api)
