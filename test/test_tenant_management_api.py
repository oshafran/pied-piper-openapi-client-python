"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.tenant_management_api import TenantManagementApi  # noqa: E501


class TestTenantManagementApi(unittest.TestCase):
    """TenantManagementApi unit test stubs"""

    def setUp(self):
        self.api = TenantManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_tenant(self):
        """Test case for create_tenant

        """
        pass

    def test_create_tenant_async(self):
        """Test case for create_tenant_async

        """
        pass

    def test_create_tenant_async_bulk(self):
        """Test case for create_tenant_async_bulk

        """
        pass

    def test_delete_tenant(self):
        """Test case for delete_tenant

        """
        pass

    def test_delete_tenant_async_bulk(self):
        """Test case for delete_tenant_async_bulk

        """
        pass

    def test_force_status_collection(self):
        """Test case for force_status_collection

        """
        pass

    def test_get_all_tenant_statuses(self):
        """Test case for get_all_tenant_statuses

        """
        pass

    def test_get_all_tenants(self):
        """Test case for get_all_tenants

        """
        pass

    def test_get_tenant(self):
        """Test case for get_tenant

        """
        pass

    def test_get_tenant_hosting_capacity_onv_smarts(self):
        """Test case for get_tenant_hosting_capacity_onv_smarts

        """
        pass

    def test_get_tenantv_smart_mapping(self):
        """Test case for get_tenantv_smart_mapping

        """
        pass

    def test_switch_tenant(self):
        """Test case for switch_tenant

        """
        pass

    def test_tenantv_smart_mt_migrate(self):
        """Test case for tenantv_smart_mt_migrate

        """
        pass

    def test_update_tenant(self):
        """Test case for update_tenant

        """
        pass

    def test_v_session_id(self):
        """Test case for v_session_id

        """
        pass


if __name__ == '__main__':
    unittest.main()
