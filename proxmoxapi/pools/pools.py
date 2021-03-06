"""Module for pools resource."""

from proxmoxapi.resource import Resource
from proxmoxapi.pools.pool import Pool


class Pools(Resource):
    """Class for pools resource."""
    # pylint: disable=too-few-public-methods

    url = "pools"

    def _get(self):
        """Pool index.

        :returns: The instance of :class:`requests.Response`.
        """
        return self.send_request("GET")

    def pool(self, pool_id):
        """Method to get pool_id resource.

        :param str pool_id: The pool identifier.

        :returns: The instance of :class:`Pool
            <proxmoxapi.pools.pool.Pool>`.
        """
        return Pool(self.api, pool_id)
