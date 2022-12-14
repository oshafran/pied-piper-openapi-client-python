"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.radio_band_setting24_g import RadioBandSetting24G
from openapi_client.model.radio_band_setting5_g import RadioBandSetting5G
globals()['RadioBandSetting24G'] = RadioBandSetting24G
globals()['RadioBandSetting5G'] = RadioBandSetting5G
from openapi_client.model.channel_power_settings import ChannelPowerSettings


class TestChannelPowerSettings(unittest.TestCase):
    """ChannelPowerSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testChannelPowerSettings(self):
        """Test ChannelPowerSettings"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ChannelPowerSettings()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
