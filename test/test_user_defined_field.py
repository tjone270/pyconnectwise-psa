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

from connectwise_psa.models.user_defined_field import UserDefinedField

class TestUserDefinedField(unittest.TestCase):
    """UserDefinedField unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserDefinedField:
        """Test UserDefinedField
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserDefinedField`
        """
        model = UserDefinedField()
        if include_optional:
            return UserDefinedField(
                info = {
                    'key' : ''
                    },
                add_all_business_units = True,
                add_all_locations = True,
                business_unit_ids = [
                    56
                    ],
                button_url = '',
                caption = '',
                date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
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
                remove_all_business_units = True,
                remove_all_locations = True,
                required_flag = True,
                screen_id = '',
                sequence_number = 56
            )
        else:
            return UserDefinedField(
                caption = '',
                field_type_identifier = 'TextArea',
                pod_id = 56,
                sequence_number = 56,
        )
        """

    def testUserDefinedField(self):
        """Test UserDefinedField"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()