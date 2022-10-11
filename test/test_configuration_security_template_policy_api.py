"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.configuration_security_template_policy_api import ConfigurationSecurityTemplatePolicyApi  # noqa: E501


class TestConfigurationSecurityTemplatePolicyApi(unittest.TestCase):
    """ConfigurationSecurityTemplatePolicyApi unit test stubs"""

    def setUp(self):
        self.api = ConfigurationSecurityTemplatePolicyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_security_template(self):
        """Test case for create_security_template

        """
        pass

    def test_delete_security_template(self):
        """Test case for delete_security_template

        """
        pass

    def test_edit_security_template(self):
        """Test case for edit_security_template

        """
        pass

    def test_edit_template_with_lenient_lock(self):
        """Test case for edit_template_with_lenient_lock

        """
        pass

    def test_generate_security_policy_summary(self):
        """Test case for generate_security_policy_summary

        """
        pass

    def test_generate_security_template_list(self):
        """Test case for generate_security_template_list

        """
        pass

    def test_get_device_list_by_id(self):
        """Test case for get_device_list_by_id

        """
        pass

    def test_get_security_policy_device_list(self):
        """Test case for get_security_policy_device_list

        """
        pass

    def test_get_security_template(self):
        """Test case for get_security_template

        """
        pass

    def test_get_security_templates_for_device(self):
        """Test case for get_security_templates_for_device

        """
        pass


if __name__ == '__main__':
    unittest.main()
