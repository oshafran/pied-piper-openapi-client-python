"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.configuration_template_master_api import ConfigurationTemplateMasterApi  # noqa: E501


class TestConfigurationTemplateMasterApi(unittest.TestCase):
    """ConfigurationTemplateMasterApi unit test stubs"""

    def setUp(self):
        self.api = ConfigurationTemplateMasterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_change_template_resource_group1(self):
        """Test case for change_template_resource_group1

        """
        pass

    def test_create_cli_template(self):
        """Test case for create_cli_template

        """
        pass

    def test_create_master_template(self):
        """Test case for create_master_template

        """
        pass

    def test_delete_master_template(self):
        """Test case for delete_master_template

        """
        pass

    def test_edit_master_template(self):
        """Test case for edit_master_template

        """
        pass

    def test_generate_master_template_list(self):
        """Test case for generate_master_template_list

        """
        pass

    def test_generate_template_for_migration(self):
        """Test case for generate_template_for_migration

        """
        pass

    def test_get_master_template_definition(self):
        """Test case for get_master_template_definition

        """
        pass

    def test_get_out_of_sync_devices(self):
        """Test case for get_out_of_sync_devices

        """
        pass

    def test_get_out_of_sync_templates(self):
        """Test case for get_out_of_sync_templates

        """
        pass

    def test_is_migration_required(self):
        """Test case for is_migration_required

        """
        pass

    def test_migrate_templates(self):
        """Test case for migrate_templates

        """
        pass

    def test_migration_info(self):
        """Test case for migration_info

        """
        pass


if __name__ == '__main__':
    unittest.main()
