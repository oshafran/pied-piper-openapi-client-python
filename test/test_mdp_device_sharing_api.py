"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.mdp_device_sharing_api import MDPDeviceSharingApi  # noqa: E501


class TestMDPDeviceSharingApi(unittest.TestCase):
    """MDPDeviceSharingApi unit test stubs"""

    def setUp(self):
        self.api = MDPDeviceSharingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_attach_devices(self):
        """Test case for attach_devices

        """
        pass

    def test_detach_devices(self):
        """Test case for detach_devices

        """
        pass

    def test_edit_attached_devices(self):
        """Test case for edit_attached_devices

        """
        pass

    def test_retrieve_mdp_attached_devices(self):
        """Test case for retrieve_mdp_attached_devices

        """
        pass

    def test_retrieve_mdp_supported_devices_(self):
        """Test case for retrieve_mdp_supported_devices_

        """
        pass


if __name__ == '__main__':
    unittest.main()
