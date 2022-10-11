"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.real_time_monitoring_tunnel_api import RealTimeMonitoringTunnelApi  # noqa: E501


class TestRealTimeMonitoringTunnelApi(unittest.TestCase):
    """RealTimeMonitoringTunnelApi unit test stubs"""

    def setUp(self):
        self.api = RealTimeMonitoringTunnelApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_bfd_statistics_list(self):
        """Test case for create_bfd_statistics_list

        """
        pass

    def test_create_fec_statistics(self):
        """Test case for create_fec_statistics

        """
        pass

    def test_create_gre_keepalives_list(self):
        """Test case for create_gre_keepalives_list

        """
        pass

    def test_create_ipsec_statistics_list(self):
        """Test case for create_ipsec_statistics_list

        """
        pass

    def test_create_packet_duplicate_statistics(self):
        """Test case for create_packet_duplicate_statistics

        """
        pass

    def test_create_statistics_list(self):
        """Test case for create_statistics_list

        """
        pass


if __name__ == '__main__':
    unittest.main()