"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "pied-piper-sdwan-sdk"
VERSION = "1.0.47"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="Cisco SD-WAN vManage API",
    author="OpenAPI Generator community",
    author_email="vmanage@cisco.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Cisco SD-WAN vManage API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Commercial License",
    long_description="""\
    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501
    """
)
