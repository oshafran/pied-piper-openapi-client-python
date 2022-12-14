"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.real_time_monitoring_ip_api import RealTimeMonitoringIPApi  # noqa: E501


class TestRealTimeMonitoringIPApi(unittest.TestCase):
    """RealTimeMonitoringIPApi unit test stubs"""

    def setUp(self):
        self.api = RealTimeMonitoringIPApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_fib_list(self):
        """Test case for create_fib_list

        """
        pass

    def test_create_ietf_routing_list(self):
        """Test case for create_ietf_routing_list

        """
        pass

    def test_create_ip_mfib_oil_list(self):
        """Test case for create_ip_mfib_oil_list

        """
        pass

    def test_create_ip_mfib_stats_list(self):
        """Test case for create_ip_mfib_stats_list

        """
        pass

    def test_create_ip_mfib_summary_list(self):
        """Test case for create_ip_mfib_summary_list

        """
        pass

    def test_create_nat64_translation_list(self):
        """Test case for create_nat64_translation_list

        """
        pass

    def test_create_nat_filter_list(self):
        """Test case for create_nat_filter_list

        """
        pass

    def test_create_nat_interface_list(self):
        """Test case for create_nat_interface_list

        """
        pass

    def test_create_nat_interface_statistics_list(self):
        """Test case for create_nat_interface_statistics_list

        """
        pass

    def test_create_nat_translation_list(self):
        """Test case for create_nat_translation_list

        """
        pass

    def test_create_route_table_list(self):
        """Test case for create_route_table_list

        """
        pass


if __name__ == '__main__':
    unittest.main()
