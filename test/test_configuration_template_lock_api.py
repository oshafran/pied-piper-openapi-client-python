"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.configuration_template_lock_api import ConfigurationTemplateLockApi  # noqa: E501


class TestConfigurationTemplateLockApi(unittest.TestCase):
    """ConfigurationTemplateLockApi unit test stubs"""

    def setUp(self):
        self.api = ConfigurationTemplateLockApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_remove_lock(self):
        """Test case for remove_lock

        """
        pass

    def test_update_lease_time(self):
        """Test case for update_lease_time

        """
        pass


if __name__ == '__main__':
    unittest.main()
