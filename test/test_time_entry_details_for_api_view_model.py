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

from connectwise_psa.models.time_entry_details_for_api_view_model import TimeEntryDetailsForApiViewModel

class TestTimeEntryDetailsForApiViewModel(unittest.TestCase):
    """TimeEntryDetailsForApiViewModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeEntryDetailsForApiViewModel:
        """Test TimeEntryDetailsForApiViewModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeEntryDetailsForApiViewModel`
        """
        model = TimeEntryDetailsForApiViewModel()
        if include_optional:
            return TimeEntryDetailsForApiViewModel(
                billable = connectwise_psa.models.generic_name_id_dto.GenericNameIdDTO(
                    id = 56, 
                    name = '', 
                    tag = '', ),
                deduct = 1.337,
                end_time = '',
                hours = 1.337,
                internal_notes = '',
                member_time_zone_offset = 56,
                notes = '',
                start_time = '',
                time_details_pod_user_defined_fields = [
                    connectwise_psa.models.user_defined_field_value.UserDefinedFieldValue(
                        filtered = True, 
                        row_num = 56, 
                        skip_location_and_billing_unit = True, 
                        user_defined_field_rec_id = 56, 
                        value = '', )
                    ],
                work_type = connectwise_psa.models.generic_name_id_dto.GenericNameIdDTO(
                    id = 56, 
                    name = '', 
                    tag = '', )
            )
        else:
            return TimeEntryDetailsForApiViewModel(
        )
        """

    def testTimeEntryDetailsForApiViewModel(self):
        """Test TimeEntryDetailsForApiViewModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()