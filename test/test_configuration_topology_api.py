"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.configuration_topology_api import ConfigurationTopologyApi  # noqa: E501


class TestConfigurationTopologyApi(unittest.TestCase):
    """ConfigurationTopologyApi unit test stubs"""

    def setUp(self):
        self.api = ConfigurationTopologyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_device_topology(self):
        """Test case for create_device_topology

        """
        pass

    def test_create_full_topology(self):
        """Test case for create_full_topology

        """
        pass

    def test_create_physical_topology(self):
        """Test case for create_physical_topology

        """
        pass

    def test_get_site_topology(self):
        """Test case for get_site_topology

        """
        pass


if __name__ == '__main__':
    unittest.main()
