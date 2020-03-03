#!/usr/bin/env python
# --------------------------------------------------------------------
# Program by Batura A.
# Version           Date                Info
#   1.0             2020           Initial version
# --------------------------------------------------------------------
import setuptools

setuptools.setup(
    name="snapshot",
    packages=setuptools.find_packages(),
    scripts=["snapshot"],
    version="1.0",
    author="Andrei Batura",
    author_email="andrei_batura@epam.com",
    description="Snapshot application",
    licence="MIT",
    platform="CentOS7"
)
