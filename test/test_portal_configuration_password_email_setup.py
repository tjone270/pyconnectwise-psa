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

from connectwise_psa.models.portal_configuration_password_email_setup import PortalConfigurationPasswordEmailSetup

class TestPortalConfigurationPasswordEmailSetup(unittest.TestCase):
    """PortalConfigurationPasswordEmailSetup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PortalConfigurationPasswordEmailSetup:
        """Test PortalConfigurationPasswordEmailSetup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PortalConfigurationPasswordEmailSetup`
        """
        model = PortalConfigurationPasswordEmailSetup()
        if include_optional:
            return PortalConfigurationPasswordEmailSetup(
                info = {
                    'key' : ''
                    },
                id = 56,
                invalid_password_email_body = '',
                invalid_password_email_from_email = '',
                invalid_password_email_from_first_name = '',
                invalid_password_email_from_last_name = '',
                invalid_password_email_subject = '',
                invalid_password_email_use_custom_email_flag = True,
                valid_password_email_body = '',
                valid_password_email_from_email = '',
                valid_password_email_from_first_name = '',
                valid_password_email_from_last_name = '',
                valid_password_email_subject = '',
                valid_password_email_use_custom_email_flag = True
            )
        else:
            return PortalConfigurationPasswordEmailSetup(
        )
        """

    def testPortalConfigurationPasswordEmailSetup(self):
        """Test PortalConfigurationPasswordEmailSetup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
