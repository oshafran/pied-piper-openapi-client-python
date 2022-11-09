"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.real_time_monitoring_tcp_optimization_api import RealTimeMonitoringTCPOptimizationApi  # noqa: E501


class TestRealTimeMonitoringTCPOptimizationApi(unittest.TestCase):
    """RealTimeMonitoringTCPOptimizationApi unit test stubs"""

    def setUp(self):
        self.api = RealTimeMonitoringTCPOptimizationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_active_tcp_flows(self):
        """Test case for get_active_tcp_flows

        """
        pass

    def test_get_expired_tcp_flows(self):
        """Test case for get_expired_tcp_flows

        """
        pass

    def test_get_tcp_summary(self):
        """Test case for get_tcp_summary

        """
        pass


if __name__ == '__main__':
    unittest.main()
