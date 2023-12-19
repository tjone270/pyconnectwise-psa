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

from connectwise_psa.models.service_email_template import ServiceEmailTemplate

class TestServiceEmailTemplate(unittest.TestCase):
    """ServiceEmailTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceEmailTemplate:
        """Test ServiceEmailTemplate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceEmailTemplate`
        """
        model = ServiceEmailTemplate()
        if include_optional:
            return ServiceEmailTemplate(
                info = {
                    'key' : ''
                    },
                body = '',
                copy_sender_flag = True,
                email_address = '',
                external_contact_notifications = True,
                first_name = '',
                id = 56,
                internal_contact_notifications = True,
                last_name = '',
                resource_records_flag = True,
                service_board = connectwise_psa.models.board_reference.BoardReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                service_status = connectwise_psa.models.service_status_reference.ServiceStatusReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', 
                    sort = 56, ),
                service_survey = connectwise_psa.models.service_survey_reference.ServiceSurveyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                subject = '',
                tasks_flag = True,
                type = 'Any',
                use_sender_flag = True
            )
        else:
            return ServiceEmailTemplate(
                type = 'Any',
        )
        """

    def testServiceEmailTemplate(self):
        """Test ServiceEmailTemplate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()