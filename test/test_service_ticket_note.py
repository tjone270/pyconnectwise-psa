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

from connectwise_psa.models.service_ticket_note import ServiceTicketNote

class TestServiceTicketNote(unittest.TestCase):
    """ServiceTicketNote unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceTicketNote:
        """Test ServiceTicketNote
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceTicketNote`
        """
        model = ServiceTicketNote()
        if include_optional:
            return ServiceTicketNote(
                info = {
                    'key' : ''
                    },
                bundled_flag = True,
                contact = connectwise_psa.models.contact_reference.ContactReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                detail_description_flag = True,
                id = 56,
                internal_analysis_flag = True,
                is_markdown_flag = True,
                issue_flag = True,
                member = connectwise_psa.models.member_reference.MemberReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                merged_flag = True,
                note_type = 'TicketNote',
                original_author = '',
                resolution_flag = True,
                text = '',
                ticket = connectwise_psa.models.ticket_reference.TicketReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    summary = '', ),
                time_end = '',
                time_start = ''
            )
        else:
            return ServiceTicketNote(
        )
        """

    def testServiceTicketNote(self):
        """Test ServiceTicketNote"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
