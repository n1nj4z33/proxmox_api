# -*- coding: utf-8 -*-
"""Module for qemu resource."""

from requests.exceptions import HTTPError

from .resource import Resource
from .nodes.qemu.vmid import VMID


class QEMU(Resource):
    """Class for qemu resource."""

    def __init__(self, api, node_id):
        """
        :param api: :class:`ProxmoxAPI <.api.ProxmoxAPI>`.
        :param str node_id: The cluster node name.
        """
        super(QEMU, self).__init__(api)
        self.node_id = node_id
        self.url = "nodes/%s/qemu" % self.node_id

    def _get(self):
        """
        Qemu virtual machine index (per node).

        :returns: :class:`requests.Response`.
        """
        return self.send_request("GET")

    #pylint: disable=too-many-arguments
    #pylint: disable=too-many-locals
    def _post(self, vm_id, name=None, description=None, sockets=None,
              cores=None, ide=(), net=(), memory=None, balloon=None,
              numa=None, ostype=None, pool=None):
        """
        Create or restore a virtual machine.

        :param int vm_id: The (unique) ID of the VM.
        :param str name: (optional) Set a name for the VM.
                         Only used on the configuration web interface.
        :param str description: (optional) Description for the VM.
                                Only used on the configuration web interface.
                                This is saved as comment inside the configuration file.
        :param int sockets: (optional) The number of CPU sockets.
        :param int cores: (optional) The number of cores per socket.
        :param tuple ide: (optional) The tuple of IDE devices.
        :param tuple net: (optional) The tuple of NET devices.
        :param int memory: (optional) Amount of RAM for the VM in MB.
                           This is the maximum available memory when you use the balloon device.
        :param int balloon: (optional) Amount of target RAM for the VM in MB.
                            Using zero disables the ballon driver.
        :param bool numa: (optional) Enable/disable Numa.
        :param str ostype: (optional) Used to enable special optimization,
                           features for specific operating systems.
        :param str pool: (optional) Add the VM to the specified pool.

        :returns: :class:`requests.Response`.
        """
        params = dict(vmid=vm_id,
                      name=name,
                      description=description,
                      sockets=sockets,
                      cores=cores,
                      memory=memory,
                      balloon=balloon,
                      numa=numa,
                      ostype=ostype,
                      pool=pool)
        for index, device in enumerate(ide):
            params["ide%d" % index] = device
        for index, device in enumerate(net):
            params["net%d" % index] = device
        return self.send_request("POST", params=params)

    def create(self, options):
        """
        Create or restore a virtual machine.

        :param options: The instance of
            :class:`QemuVirtualMachineOptions
            <.nodes.qemu.options.QemuVirtualMachineOptions>`.

        :raises AlreadyExistError: if virtual machine exists.
        :raises HTTPError: if other http error occurred.

        :returns: :class:`UPID <.nodes.tasks.upid.UPID>`.
        """
        ide = [ide_device.format_string() for ide_device in options.hdds + options.cdroms]
        net = [net_device.format_string() for net_device in options.nets]
        try:
            response = self._post(options.vm_id, name=options.name, description=options.description,
                                  sockets=options.sockets, cores=options.cores, ide=ide,
                                  net=net, memory=options.memory, balloon=options.balloon,
                                  numa=options.numa, ostype=options.ostype, pool=options.pool)
        except HTTPError as exc:
            if "already exist" in exc.message:
                raise AlreadyExistError("Virtual machine with id %s already exists." %
                                        options.vm_id)
        task_id = response.json()["data"]
        return self.api.nodes.node(self.node_id).tasks.get_task_by_task_id(task_id)

    def vmid(self, vm_id):
        """
        Method to get vmid resource.

        :param int vm_id: The (unique) ID of the VM.

        :returns: :class:`VMID <.nodes.qemu.vmid.VMID>`.
        """
        return VMID(self.api, self.node_id, vm_id)

class AlreadyExistError(Exception):
    """Class for error when create virtual machine with an existing id."""
