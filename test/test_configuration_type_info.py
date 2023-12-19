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

from connectwise_psa.models.configuration_type_info import ConfigurationTypeInfo

class TestConfigurationTypeInfo(unittest.TestCase):
    """ConfigurationTypeInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigurationTypeInfo:
        """Test ConfigurationTypeInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigurationTypeInfo`
        """
        model = ConfigurationTypeInfo()
        if include_optional:
            return ConfigurationTypeInfo(
                info = {
                    'key' : ''
                    },
                id = 56,
                inactive_flag = True,
                name = '',
                system_flag = True
            )
        else:
            return ConfigurationTypeInfo(
        )
        """

    def testConfigurationTypeInfo(self):
        """Test ConfigurationTypeInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
