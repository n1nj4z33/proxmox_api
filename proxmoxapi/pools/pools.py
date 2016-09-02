# -*- coding: utf-8 -*-
"""Module for pools resource."""

from proxmox_api.resource import Resource
from proxmox_api.pools.pool import Pool


class Pools(Resource):
    """Class for pools resource."""

    url = "pools"

    def _get(self):
        """
        Pool index.

        :returns: :class:`requests.Response`.
        """
        return self.send_request("GET")

    def pool(self, pool_id):
        """
        Method to get pool_id resource.

        :param str pool_id: The pool identifier.

        :returns: :class:`Pool <proxmox_api.pools.pool.Pool>`.
        """
        return Pool(self.api, pool_id)
