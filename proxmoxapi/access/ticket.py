# -*- coding: utf-8 -*-
"""Module for ticket resource."""

from proxmoxapi.resource import Resource


class Ticket(Resource):
    """Class for ticket resource."""
    # pylint: disable=too-few-public-methods

    url = "access/ticket"

    def _get(self):
        """
        Dummy. Useful for formaters which want to provide a login page.

        :returns: :class:`requests.Response`.
        """
        return self.send_request("GET")

    def _post(self, username, password, realm=None):
        """
        Create or verify authentication ticket.

        :param str username: The username.
        :param str password: The secret password. This can also be a valid ticket.
        :param str realm: (optional) You can optionally pass the realm using this parameter.
                          Normally the realm is simply added to the username <username>@<realm>.
        :returns: :class:`requests.Response`.
        """
        data = dict(username=username,
                    password=password,
                    realm=realm)
        return self.send_request("POST", data=data)

    def login(self, username, password, realm=None):
        """
        Create or verify authentication ticket.

        :param str username: The username.
        :param str password: The secret password. This can also be a valid ticket.
        :param str realm: (optional) You can optionally pass the realm using this parameter.
                          Normally the realm is simply added to the username <username>@<realm>.
        :returns tuple: The PVEAuthCookie and CSRFPreventionToken tuple.
        """
        response = self._post(username, password, realm)
        data = response.json()["data"]
        ticket = data["ticket"]
        token = data["CSRFPreventionToken"]
        return ticket, token
