from setuptools import find_packages, setup

"""
:author: abuztrade
:license: MIT License, see LICENSE file.
:copyright: (c) 2022 by abuztrade.
"""

setup(
    packages=["pymexc"],
    include_package_data=True,  # for MANIFEST.in
    package_data={
        package: [
            "py.typed",
            "*.pyi",
            "**/*.pyi",
            "web/*",
            "_async/*",
            "proto/*",
        ]
        for package in find_packages()
    },
    zip_safe=False,
)
