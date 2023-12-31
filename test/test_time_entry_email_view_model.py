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

from connectwise_psa.models.time_entry_email_view_model import TimeEntryEmailViewModel

class TestTimeEntryEmailViewModel(unittest.TestCase):
    """TimeEntryEmailViewModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeEntryEmailViewModel:
        """Test TimeEntryEmailViewModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeEntryEmailViewModel`
        """
        model = TimeEntryEmailViewModel()
        if include_optional:
            return TimeEntryEmailViewModel(
                append_discussion = True,
                append_internal = True,
                append_resolution = True,
                cc_email_address_list = '',
                contact = '',
                contact_email_address = '',
                document_rec_id_list = [
                    56
                    ],
                var_from = '',
                from_email_address = '',
                from_email_address_for_resources = '',
                from_for_resources = '',
                is_to_ccs = True,
                is_to_contact = True,
                is_to_resources = True,
                member_rec_id = 56,
                no_time_entry = True,
                note = '',
                resource_email_address_list = '',
                resources = '',
                save_cc_list = True,
                schedule_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                schedule_done = True,
                sr_detail_rec_id = 56,
                sr_service_rec_id = 56,
                sr_service_status_rec_id = 56,
                time_rec_id = 56
            )
        else:
            return TimeEntryEmailViewModel(
        )
        """

    def testTimeEntryEmailViewModel(self):
        """Test TimeEntryEmailViewModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
