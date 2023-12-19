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

from connectwise_psa.models.user_defined_field_info import UserDefinedFieldInfo

class TestUserDefinedFieldInfo(unittest.TestCase):
    """UserDefinedFieldInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserDefinedFieldInfo:
        """Test UserDefinedFieldInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserDefinedFieldInfo`
        """
        model = UserDefinedFieldInfo()
        if include_optional:
            return UserDefinedFieldInfo(
                info = {
                    'key' : ''
                    },
                business_unit_ids = [
                    56
                    ],
                button_url = '',
                caption = '',
                date_created = '',
                display_on_screen_flag = True,
                entry_type_identifier = 'Date',
                field_type_identifier = 'TextArea',
                help_text = '',
                id = 56,
                list_view_flag = True,
                location_ids = [
                    56
                    ],
                number_decimals = 56,
                options = [
                    connectwise_psa.models.user_defined_field_option.UserDefinedFieldOption(
                        default_flag = True, 
                        id = 56, 
                        inactive_flag = True, 
                        option_value = '', 
                        sort_order = 56, )
                    ],
                pod_id = 56,
                read_only_flag = True,
                required_flag = True,
                sequence_number = 56
            )
        else:
            return UserDefinedFieldInfo(
        )
        """

    def testUserDefinedFieldInfo(self):
        """Test UserDefinedFieldInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()