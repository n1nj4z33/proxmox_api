# -*- coding: utf-8 -*-
"""Module for virtual machine device."""

import .nodes.qemu.constants as constants


class QEMUVirtualMachineDevice(object):
    """Class for virtual machine device."""

    def __init__(self, storage, media):
        """
        :param str storage: The storage name.
        :param str media: The media type.
        """
        self.media = media
        self.storage = storage

    @property
    def media_format(self):
        """Property ot get formated media."""
        return "media={media}".format(media=self.media)


class QEMUVirtualMachineCDROM(QEMUVirtualMachineDevice):
    """Class for virtual machine CDROM device."""

    def __init__(self, storage, iso_path):
        """
        :param str storage: The storage name.
        :param iso_path: The ISO file path.
        """
        super(QEMUVirtualMachineCDROM, self).__init__(storage, constants.MEDIA_CDROM)
        self.iso_path = iso_path
        self.content_type = constants.CONTENT_TYPE_ISO

    def format_string(self):
        """Property to get proxmox CDROM device format string."""
        if self.iso_path:
            format_string = "{storage}:{content_type}/{iso_path},{media}".format(
                storage=self.storage, content_type=self.content_type,
                iso_path=self.iso_path, media=self.media_format
                )
        else:
            format_string = "{storage}:none,{media}".format(storage=self.storage,
                                                            media=self.media_format)
        return format_string

class QEMUVirtualMachineHDD(QEMUVirtualMachineDevice):
    """Class for virtual machine HDD device."""

    def __init__(self, storage, size):
        """
        :param str storage: The storage name.
        :param size: The HDD drive size in GB.
        """
        super(QEMUVirtualMachineHDD, self).__init__(storage, constants.MEDIA_HDD)
        self.size = size
        self.format = constants.HDD_FORMAT_VMDK

    @property
    def hdd_format(self):
        """Property ot get formated hdd format."""
        return "format={format}".format(format=self.format)

    def format_string(self):
        """Property to get proxmox HDD device format string."""
        return "{storage}:{size},{media},{format}".format(storage=self.storage,
                                                          size=self.size,
                                                          media=self.media_format,
                                                          format=self.hdd_format)


class QEMUVirtualMachineNET(object):
    """Class for virtual machine NET device."""

    def __init__(self):
        self.net_model = constants.NET_MODEL_E1000
        self.net_bridge = constants.NET_BRIDGE

    @property
    def bridge_format(self):
        """Property ot get formated bridge."""
        return "bridge={bridge}".format(bridge=self.net_bridge)

    def format_string(self):
        """Property to get proxmox NET device format string."""
        return "{net_model},{bridge}".format(net_model=self.net_model,
                                             bridge=self.bridge_format)
