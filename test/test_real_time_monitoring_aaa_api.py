"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.real_time_monitoring_aaa_api import RealTimeMonitoringAAAApi  # noqa: E501


class TestRealTimeMonitoringAAAApi(unittest.TestCase):
    """RealTimeMonitoringAAAApi unit test stubs"""

    def setUp(self):
        self.api = RealTimeMonitoringAAAApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_aa_aservers(self):
        """Test case for get_aa_aservers

        """
        pass

    def test_get_aaa_users(self):
        """Test case for get_aaa_users

        """
        pass

    def test_get_acl_match_counter_users(self):
        """Test case for get_acl_match_counter_users

        """
        pass

    def test_get_all_device_users(self):
        """Test case for get_all_device_users

        """
        pass

    def test_get_logging_from_device(self):
        """Test case for get_logging_from_device

        """
        pass

    def test_get_unclaimed_vedges(self):
        """Test case for get_unclaimed_vedges

        """
        pass

    def test_get_users_from_device(self):
        """Test case for get_users_from_device

        """
        pass


if __name__ == '__main__':
    unittest.main()
