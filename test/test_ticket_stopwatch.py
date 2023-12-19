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

from connectwise_psa.models.ticket_stopwatch import TicketStopwatch

class TestTicketStopwatch(unittest.TestCase):
    """TicketStopwatch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TicketStopwatch:
        """Test TicketStopwatch
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TicketStopwatch`
        """
        model = TicketStopwatch()
        if include_optional:
            return TicketStopwatch(
                info = {
                    'key' : ''
                    },
                agreement = connectwise_psa.models.agreement_reference.AgreementReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', 
                    type = '', ),
                billable_option = 'Billable',
                business_unit_id = 56,
                date_entered = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                email_notes_to_contact_flag = True,
                email_notes_to_resources_flag = True,
                end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = 56,
                internal_notes = '',
                location_id = 56,
                member = connectwise_psa.models.member_reference.MemberReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                mobile_guid = '',
                notes = '',
                service_status = connectwise_psa.models.service_status_reference.ServiceStatusReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', 
                    sort = 56, ),
                show_notes_in_discussion_flag = True,
                show_notes_in_internal_flag = True,
                show_notes_in_resolution_flag = True,
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = 'Reset',
                ticket = connectwise_psa.models.ticket_reference.TicketReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    summary = '', ),
                ticket_mobile_guid = '',
                total_pause_time = 56,
                work_role = connectwise_psa.models.work_role_reference.WorkRoleReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                work_type = connectwise_psa.models.work_type_reference.WorkTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return TicketStopwatch(
                status = 'Reset',
        )
        """

    def testTicketStopwatch(self):
        """Test TicketStopwatch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()