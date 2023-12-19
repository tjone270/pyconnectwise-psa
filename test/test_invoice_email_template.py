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

from connectwise_psa.models.invoice_email_template import InvoiceEmailTemplate

class TestInvoiceEmailTemplate(unittest.TestCase):
    """InvoiceEmailTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvoiceEmailTemplate:
        """Test InvoiceEmailTemplate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvoiceEmailTemplate`
        """
        model = InvoiceEmailTemplate()
        if include_optional:
            return InvoiceEmailTemplate(
                info = {
                    'key' : ''
                    },
                attach_invoice_flag = True,
                body = '',
                copy_sender_flag = True,
                email_address = '',
                first_name = '',
                id = 56,
                invoice_status = connectwise_psa.models.billing_status_reference.BillingStatusReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                last_name = '',
                name = '',
                service_survey = connectwise_psa.models.service_survey_reference.ServiceSurveyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                subject = '',
                use_sender_flag = True
            )
        else:
            return InvoiceEmailTemplate(
                name = '',
                subject = '',
        )
        """

    def testInvoiceEmailTemplate(self):
        """Test InvoiceEmailTemplate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()