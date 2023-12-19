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

from connectwise_psa.models.board_auto_template import BoardAutoTemplate

class TestBoardAutoTemplate(unittest.TestCase):
    """BoardAutoTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BoardAutoTemplate:
        """Test BoardAutoTemplate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BoardAutoTemplate`
        """
        model = BoardAutoTemplate()
        if include_optional:
            return BoardAutoTemplate(
                info = {
                    'key' : ''
                    },
                auto_apply_flag = True,
                board = connectwise_psa.models.board_reference.BoardReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                budget_hours_setting = 'Append',
                discussion_setting = 'Append',
                documents_setting = 'Append',
                finance_information_setting = 'Append',
                id = 56,
                impact_urgency_setting = 'Append',
                internal_analysis_setting = 'Append',
                item = connectwise_psa.models.service_item_reference.ServiceItemReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                resolution_setting = 'Append',
                resources_setting = 'Append',
                send_notes_as_email_setting = 'Append',
                service_template = connectwise_psa.models.service_template_reference.ServiceTemplateReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', 
                    summary = '', ),
                subtype = connectwise_psa.models.service_sub_type_reference.ServiceSubTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                summary_setting = 'Append',
                tasks_setting = 'Append',
                template_priority_setting = 'Append',
                type = connectwise_psa.models.service_type_reference.ServiceTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return BoardAutoTemplate(
        )
        """

    def testBoardAutoTemplate(self):
        """Test BoardAutoTemplate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()