"""
A python wrapper for the Proxmox 2.x API
For more information see http://pve.proxmox.com/pve2-api-doc/
"""

import logging


def _prepare_logging():
    """Prepare logger for module."""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.NullHandler())

_prepare_logging()
