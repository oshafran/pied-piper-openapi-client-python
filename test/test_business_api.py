"""
    Cisco-Reservable-SD-WAN

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.business_api import BusinessApi  # noqa: E501


class TestBusinessApi(unittest.TestCase):
    """BusinessApi unit test stubs"""

    def setUp(self):
        self.api = BusinessApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_dataservice_system_device_vedges_get(self):
        """Test case for dataservice_system_device_vedges_get

        Get Device VEdges  # noqa: E501
        """
        pass

    def test_dataservice_template_policy_list_site_delete(self):
        """Test case for dataservice_template_policy_list_site_delete

        Delete VPN Template List  # noqa: E501
        """
        pass

    def test_dataservice_template_policy_list_site_get(self):
        """Test case for dataservice_template_policy_list_site_get

        Get Prefix Template List  # noqa: E501
        """
        pass

    def test_dataservice_template_policy_list_site_id_delete(self):
        """Test case for dataservice_template_policy_list_site_id_delete

        Delete Site Template List  # noqa: E501
        """
        pass

    def test_dataservice_template_policy_list_site_post(self):
        """Test case for dataservice_template_policy_list_site_post

        Create Site Template List  # noqa: E501
        """
        pass

    def test_dataservice_template_policy_list_vpn_post(self):
        """Test case for dataservice_template_policy_list_vpn_post

        Create VPN Template List  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
