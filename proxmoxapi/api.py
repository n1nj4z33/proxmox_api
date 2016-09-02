# -*- coding: utf-8 -*-
"""Module for ProxmoxAPI."""

import requests

from proxmox_api.version.version import Version
from proxmox_api.access.access import Access
from proxmox_api.cluster.cluster import Cluster
from proxmox_api.nodes.nodes import Nodes
from proxmox_api.pools.pools import Pools
from proxmox_api.storage.storages import Storages


# InsecureRequestWarning: Unverified HTTPS request is being made.
# Adding certificate verification is strongly advised.
# See: https://urllib3.readthedocs.org/en/latest/security.html
requests.packages.urllib3.disable_warnings()


class ProxmoxAPI(object):
    """Class for communication with proxmox."""

    def __init__(self, host, username, password, port=8006):
        """
        :param str host: The hostname or ip address of a proxmox server.
        :param str username: The username of a proxmox server.
        :param str password: The password of a proxmox server.
        :param int port: (optional) The port of a proxmox server.
        """
        self.base_url = "https://%s:%d/api2/json" % (host, port)
        self.session = requests.Session()
        self.session.verify = False
        self.session.trust_env = False
        self.username = username
        self.password = password

    def login(self):
        """
        Method for authtorization.
        Update session cookies.
        """
        ticket, token = self.access.ticket.login(self.username, self.password)
        self.session.cookies.update(dict(PVEAuthCookie=ticket))
        self.session.headers.update(dict(CSRFPreventionToken=token))

    def prepare_url(self, resource):
        """
        Construct url from resource url.

        :param resource: :class:`Resource <proxmox_api.resource.Resource>`.

        :returns: The full url to proxmox resource.
        """
        return '/'.join((self.base_url, resource.url))

    def send_request(self, resource, method, data=None, params=None, headers=None):
        #pylint: disable=too-many-arguments
        """
        Send request to proxmox server.

        :param resource: :class:`Resource <proxmox_api.resource.Resource>`.
        :param str method: The HTTP request method.
        :param dict data: (optional) The HTTP request data.
        :param dict params: (optional) The HTTP request params.
        :param dict headers: (optional) The HTTP request headers.

        :returns: :class:`Response <requests.Response>`.
        """
        url = self.prepare_url(resource)

        response = self.session.request(method=method,
                                        url=url,
                                        data=data,
                                        params=params,
                                        headers=headers)
        # Try to relogin and send request if authorization error.
        if response.status_code == 401:
            self.login()
            response = self.session.request(method=method,
                                            url=url,
                                            data=data,
                                            params=params,
                                            headers=headers)
        response.raise_for_status()
        return response

    @property
    def version(self):
        """
        Property for get version resource.

        :returns: :class:`Version <proxmox_api.version.version.Version>`.
        """
        return Version(self)

    @property
    def access(self):
        """
        Property for get access resource.

        :returns: :class:`Access <proxmox_api.access.access.Access>`.
        """
        return Access(self)

    @property
    def cluster(self):
        """
        Property for get cluster resource.

        :returns: :class:`Cluster <proxmox_api.cluster.cluster.Cluster>`.
        """
        return Cluster(self)

    @property
    def nodes(self):
        """
        Property for get nodes resource.

        :returns: :class:`Nodes <proxmox_api.nodes.nodes.Nodes>`.
        """
        return Nodes(self)

    @property
    def pools(self):
        """
        Property for get pools resource.

        :returns: :class:`Pools <proxmox_api.pools.pools.Pools>`.
        """
        return Pools(self)

    @property
    def storages(self):
        """
        Property for get storage resource.

        :returns: :class:`Storages <proxmox_api.storage.storages.Storages>`.
        """
        return Storages(self)
