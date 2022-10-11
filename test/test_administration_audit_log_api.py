"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.administration_audit_log_api import AdministrationAuditLogApi  # noqa: E501


class TestAdministrationAuditLogApi(unittest.TestCase):
    """AdministrationAuditLogApi unit test stubs"""

    def setUp(self):
        self.api = AdministrationAuditLogApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_generate_audit_log(self):
        """Test case for generate_audit_log

        """
        pass

    def test_get_audit_severity_custom_histogram(self):
        """Test case for get_audit_severity_custom_histogram

        """
        pass

    def test_get_count(self):
        """Test case for get_count

        """
        pass

    def test_get_count_post(self):
        """Test case for get_count_post

        """
        pass

    def test_get_post_property_aggregation_data(self):
        """Test case for get_post_property_aggregation_data

        """
        pass

    def test_get_post_stat_bulk_raw_property_data(self):
        """Test case for get_post_stat_bulk_raw_property_data

        """
        pass

    def test_get_property_aggregation_data(self):
        """Test case for get_property_aggregation_data

        """
        pass

    def test_get_raw_property_data(self):
        """Test case for get_raw_property_data

        """
        pass

    def test_get_stat_bulk_raw_property_data(self):
        """Test case for get_stat_bulk_raw_property_data

        """
        pass

    def test_get_stat_data_fields(self):
        """Test case for get_stat_data_fields

        """
        pass

    def test_get_stat_data_raw_audit_log_data(self):
        """Test case for get_stat_data_raw_audit_log_data

        """
        pass

    def test_get_stat_query_fields(self):
        """Test case for get_stat_query_fields

        """
        pass


if __name__ == '__main__':
    unittest.main()