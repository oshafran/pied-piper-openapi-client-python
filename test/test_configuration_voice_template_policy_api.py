"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.configuration_voice_template_policy_api import ConfigurationVoiceTemplatePolicyApi  # noqa: E501


class TestConfigurationVoiceTemplatePolicyApi(unittest.TestCase):
    """ConfigurationVoiceTemplatePolicyApi unit test stubs"""

    def setUp(self):
        self.api = ConfigurationVoiceTemplatePolicyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_voice_template(self):
        """Test case for create_voice_template

        """
        pass

    def test_delete_voice_template(self):
        """Test case for delete_voice_template

        """
        pass

    def test_edit_voice_template(self):
        """Test case for edit_voice_template

        """
        pass

    def test_generate_voice_policy_summary(self):
        """Test case for generate_voice_policy_summary

        """
        pass

    def test_generate_voice_template_list(self):
        """Test case for generate_voice_template_list

        """
        pass

    def test_get_device_list_by_policy_id(self):
        """Test case for get_device_list_by_policy_id

        """
        pass

    def test_get_template_by_id(self):
        """Test case for get_template_by_id

        """
        pass

    def test_get_voice_policy_device_list(self):
        """Test case for get_voice_policy_device_list

        """
        pass

    def test_get_voice_templates_for_device(self):
        """Test case for get_voice_templates_for_device

        """
        pass


if __name__ == '__main__':
    unittest.main()