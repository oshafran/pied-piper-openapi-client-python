"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.certificate_management_device_api import CertificateManagementDeviceApi  # noqa: E501


class TestCertificateManagementDeviceApi(unittest.TestCase):
    """CertificateManagementDeviceApi unit test stubs"""

    def setUp(self):
        self.api = CertificateManagementDeviceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_decommission_enterprise_csr_for_vedge(self):
        """Test case for decommission_enterprise_csr_for_vedge

        """
        pass

    def test_delete_configuration(self):
        """Test case for delete_configuration

        """
        pass

    def test_force_sync_root_cert(self):
        """Test case for force_sync_root_cert

        """
        pass

    def test_generate_csr(self):
        """Test case for generate_csr

        """
        pass

    def test_generate_edge_device_csr(self):
        """Test case for generate_edge_device_csr

        """
        pass

    def test_generate_enterprise_csr(self):
        """Test case for generate_enterprise_csr

        """
        pass

    def test_get_cert_details(self):
        """Test case for get_cert_details

        """
        pass

    def test_get_certificate_data(self):
        """Test case for get_certificate_data

        """
        pass

    def test_get_certificate_detail(self):
        """Test case for get_certificate_detail

        """
        pass

    def test_get_certificate_stats(self):
        """Test case for get_certificate_stats

        """
        pass

    def test_get_csr_view_right_menus(self):
        """Test case for get_csr_view_right_menus

        """
        pass

    def test_get_device_view_right_menus(self):
        """Test case for get_device_view_right_menus

        """
        pass

    def test_get_devices_list(self):
        """Test case for get_devices_list

        """
        pass

    def test_get_installed_cert(self):
        """Test case for get_installed_cert

        """
        pass

    def test_get_list_status(self):
        """Test case for get_list_status

        """
        pass

    def test_get_root_cert_chains(self):
        """Test case for get_root_cert_chains

        """
        pass

    def test_get_root_certificate(self):
        """Test case for get_root_certificate

        """
        pass

    def test_get_view(self):
        """Test case for get_view

        """
        pass

    def test_getc_edge_list(self):
        """Test case for getc_edge_list

        """
        pass

    def test_getv_edge_csr(self):
        """Test case for getv_edge_csr

        """
        pass

    def test_getv_edge_list(self):
        """Test case for getv_edge_list

        """
        pass

    def test_getv_smart_list(self):
        """Test case for getv_smart_list

        """
        pass

    def test_install_certificate(self):
        """Test case for install_certificate

        """
        pass

    def test_reset_rsa(self):
        """Test case for reset_rsa

        """
        pass

    def test_save_root_cert_chain(self):
        """Test case for save_root_cert_chain

        """
        pass

    def test_save_v_edge_list(self):
        """Test case for save_v_edge_list

        """
        pass

    def test_setv_edge_list(self):
        """Test case for setv_edge_list

        """
        pass

    def test_setv_smart_list(self):
        """Test case for setv_smart_list

        """
        pass

    def test_setv_smart_list1(self):
        """Test case for setv_smart_list1

        """
        pass

    def test_syncv_bond(self):
        """Test case for syncv_bond

        """
        pass

    def test_update_jks(self):
        """Test case for update_jks

        """
        pass


if __name__ == '__main__':
    unittest.main()
