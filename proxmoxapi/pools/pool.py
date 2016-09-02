# -*- coding: utf-8 -*-
"""Module for pool resource."""

from .resource import Resource


class Pool(Resource):
    """Class for pool resource."""

    def __init__(self, api, pool_id):
        """
        :param api: :class:`ProxmoxAPI <.api.ProxmoxAPI>`.
        :param str pool_id: The pool identifier.
        """
        super(Pool, self).__init__(api)
        self.pool_id = pool_id
        self.url = "pools/%s" % self.pool_id

    def _get(self):
        """
        Get pool configuration.

        :returns: :class:`requests.Response`.
        """
        return self.send_request("GET")
