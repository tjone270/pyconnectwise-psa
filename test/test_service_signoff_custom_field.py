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

from connectwise_psa.models.service_signoff_custom_field import ServiceSignoffCustomField

class TestServiceSignoffCustomField(unittest.TestCase):
    """ServiceSignoffCustomField unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceSignoffCustomField:
        """Test ServiceSignoffCustomField
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceSignoffCustomField`
        """
        model = ServiceSignoffCustomField()
        if include_optional:
            return ServiceSignoffCustomField(
                info = {
                    'key' : ''
                    },
                display_section = 'CustomerInformation',
                id = 56,
                sequence_number = 1.337,
                user_defined_field = connectwise_psa.models.user_defined_field_reference.UserDefinedFieldReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return ServiceSignoffCustomField(
                display_section = 'CustomerInformation',
                sequence_number = 1.337,
        )
        """

    def testServiceSignoffCustomField(self):
        """Test ServiceSignoffCustomField"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
