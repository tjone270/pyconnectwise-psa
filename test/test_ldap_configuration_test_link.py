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

from connectwise_psa.models.ldap_configuration_test_link import LdapConfigurationTestLink

class TestLdapConfigurationTestLink(unittest.TestCase):
    """LdapConfigurationTestLink unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LdapConfigurationTestLink:
        """Test LdapConfigurationTestLink
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LdapConfigurationTestLink`
        """
        model = LdapConfigurationTestLink()
        if include_optional:
            return LdapConfigurationTestLink(
                server = ''
            )
        else:
            return LdapConfigurationTestLink(
        )
        """

    def testLdapConfigurationTestLink(self):
        """Test LdapConfigurationTestLink"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
