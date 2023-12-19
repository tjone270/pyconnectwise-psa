# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from connectwise_psa.models.managed_devices_integration_info import ManagedDevicesIntegrationInfo

class TestManagedDevicesIntegrationInfo(unittest.TestCase):
    """ManagedDevicesIntegrationInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ManagedDevicesIntegrationInfo:
        """Test ManagedDevicesIntegrationInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ManagedDevicesIntegrationInfo`
        """
        model = ManagedDevicesIntegrationInfo()
        if include_optional:
            return ManagedDevicesIntegrationInfo(
                info = {
                    'key' : ''
                    },
                id = 56,
                management_it_setup_type = '',
                name = '',
                solution = ''
            )
        else:
            return ManagedDevicesIntegrationInfo(
        )
        """

    def testManagedDevicesIntegrationInfo(self):
        """Test ManagedDevicesIntegrationInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()