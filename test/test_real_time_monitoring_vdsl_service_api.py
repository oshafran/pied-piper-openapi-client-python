"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.real_time_monitoring_vdsl_service_api import RealTimeMonitoringVDSLServiceApi  # noqa: E501


class TestRealTimeMonitoringVDSLServiceApi(unittest.TestCase):
    """RealTimeMonitoringVDSLServiceApi unit test stubs"""

    def setUp(self):
        self.api = RealTimeMonitoringVDSLServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_co_line_specific_stats(self):
        """Test case for get_co_line_specific_stats

        """
        pass

    def test_get_co_stats(self):
        """Test case for get_co_stats

        """
        pass

    def test_get_cpe_line_specific_stats(self):
        """Test case for get_cpe_line_specific_stats

        """
        pass

    def test_get_cpe_stats(self):
        """Test case for get_cpe_stats

        """
        pass

    def test_get_line_bonding_stats(self):
        """Test case for get_line_bonding_stats

        """
        pass

    def test_get_line_specific_stats(self):
        """Test case for get_line_specific_stats

        """
        pass

    def test_get_vdsl_info(self):
        """Test case for get_vdsl_info

        """
        pass


if __name__ == '__main__':
    unittest.main()