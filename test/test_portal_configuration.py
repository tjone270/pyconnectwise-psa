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

from connectwise_psa.models.portal_configuration import PortalConfiguration

class TestPortalConfiguration(unittest.TestCase):
    """PortalConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PortalConfiguration:
        """Test PortalConfiguration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PortalConfiguration`
        """
        model = PortalConfiguration()
        if include_optional:
            return PortalConfiguration(
                info = {
                    'key' : ''
                    },
                agreement_type_ids = [
                    56
                    ],
                board_ids = [
                    56
                    ],
                button_color = '',
                company = connectwise_psa.models.company_reference.CompanyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                config_type_ids = [
                    56
                    ],
                default_flag = True,
                display_vendor_flag = True,
                header_color = '',
                id = 56,
                language = 'English',
                location_ids = [
                    56
                    ],
                login_background_color = '',
                menu_color = '',
                name = '',
                portal_background_color = '',
                portal_image_copy_success_flag = True,
                url = '',
                welcome_text = ''
            )
        else:
            return PortalConfiguration(
                name = '',
        )
        """

    def testPortalConfiguration(self):
        """Test PortalConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
