# -*- coding: utf-8 -*-
"""Module for base proxmox resource."""


class Resource(object):
    """Class for base proxmox resource."""

    def __init__(self, api):
        """
        :param api: :class:`ProxmoxAPI <proxmox_api.api.ProxmoxAPI>`.
        """
        self.api = api

    @property
    def session(self):
        """Property to get session."""
        return self.api.get_session()

    def send_request(self, method, data=None, params=None, headers=None):
        """
        Send request to proxmox server.

        :param str method: The HTTP request method.
        :param dict data: (optional) The HTTP request data.
        :param dict params: (optional) The HTTP request params.
        :param dict headers: (optional) The HTTP request headers.

        :returns: :class:`requests.Response`.
        """
        return self.api.send_request(self, method, data=data, params=params, headers=headers)
