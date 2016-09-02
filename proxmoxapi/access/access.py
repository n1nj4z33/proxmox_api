# -*- coding: utf-8 -*-
"""Module for access resource."""

from .resource import Resource
from .access.ticket import Ticket


class Access(Resource):
    """Class for access resource."""

    url = "access"

    def _get(self):
        """
        Directory index.

        :returns: :class:`requests.Response`.
        """
        return self.send_request("GET")

    @property
    def ticket(self):
        """
        Property to get ticket resource.

        :returns: :class:`Ticket <.access.ticket.Ticket>`.
        """
        return Ticket(self.api)
