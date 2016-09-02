# -*- coding: utf-8 -*-
"""The Proxmox API package setup."""
from setuptools import (setup, find_packages)

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setup(
    name="proxmoxapi",
    version="0.1",
    description="The Proxmox API.",
    url="https://github.com/n1nj4z33/proxmoxapi",
    author="n1nj4z33",
    author_email="n1nj4z33@gmail.com",
    packages=find_packages(),
    include_package_data = True,
    install_requires=install_requires,
    zip_safe=False
)