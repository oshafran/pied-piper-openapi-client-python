"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.mdp_policy_management_api import MDPPolicyManagementApi  # noqa: E501


class TestMDPPolicyManagementApi(unittest.TestCase):
    """MDPPolicyManagementApi unit test stubs"""

    def setUp(self):
        self.api = MDPPolicyManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_retrieve_mdp_policies(self):
        """Test case for retrieve_mdp_policies

        """
        pass

    def test_update_policy_status(self):
        """Test case for update_policy_status

        """
        pass


if __name__ == '__main__':
    unittest.main()