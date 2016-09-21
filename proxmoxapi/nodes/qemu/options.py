"""Module for qemu virtual machine options."""

_MEMORY_BALLOON = 8192
_NUMA = 0
_OSTYPE = "l26"


class QemuVirtualMachineOptions(object):
    """Class for qemu virtual machine options."""
    # pylint: disable=too-few-public-methods, too-many-instance-attributes

    def __init__(self, vm_id, name, node, pool, storage): # pylint: disable=too-many-arguments
        """
        :param int vm_id: The (unique) ID of the VM.
        :param str name: The name of a virtual machine.
        :param str node: The node of a virtual machine.
        :param str pool: The pool of a virtual machine.
        :param str storage: The storage of a virtual machine.
        """
        self.vm_id = vm_id
        self.balloon = _MEMORY_BALLOON
        self.numa = _NUMA
        self.ostype = _OSTYPE
        self.name = name
        self.node = node
        self.pool = pool
        self.storage = storage
        self.cores = None
        self.sockets = None
        self.memory = None
        self.description = None
        self.hdds = []
        self.cdroms = []
        self.nets = []
