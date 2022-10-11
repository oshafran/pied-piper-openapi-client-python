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
from openapi_client.model.control_status import ControlStatus
from openapi_client.model.site_health import SiteHealth
from openapi_client.model.v_edge_health import VEdgeHealth
from openapi_client.model.v_smart_status import VSmartStatus
globals()['ControlStatus'] = ControlStatus
globals()['SiteHealth'] = SiteHealth
globals()['VEdgeHealth'] = VEdgeHealth
globals()['VSmartStatus'] = VSmartStatus
from openapi_client.model.tenant_status import TenantStatus


class TestTenantStatus(unittest.TestCase):
    """TenantStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTenantStatus(self):
        """Test TenantStatus"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TenantStatus()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
