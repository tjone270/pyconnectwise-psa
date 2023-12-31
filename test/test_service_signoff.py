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

from connectwise_psa.models.service_signoff import ServiceSignoff

class TestServiceSignoff(unittest.TestCase):
    """ServiceSignoff unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceSignoff:
        """Test ServiceSignoff
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceSignoff`
        """
        model = ServiceSignoff()
        if include_optional:
            return ServiceSignoff(
                info = {
                    'key' : ''
                    },
                billing_methods_text = '',
                billing_methods_text_flag = True,
                billing_terms_flag = True,
                company_info_flag = True,
                configurations_flag = True,
                credit_card_fields_flag = True,
                customer_signoff_fields_flag = True,
                customer_signoff_text = '',
                customer_signoff_text_flag = True,
                default_ff_flag = True,
                default_flag = True,
                discussion_flag = True,
                expense_agreement_flag = True,
                expense_amount_flag = True,
                expense_bill_flag = True,
                expense_date_flag = True,
                expense_flag = True,
                expense_manual_entry = 56,
                expense_manual_flag = True,
                expense_member_flag = True,
                expense_notes_flag = True,
                expense_tax_flag = True,
                expense_type_flag = True,
                id = 56,
                internal_notes_flag = True,
                name = '',
                product_agreement_flag = True,
                product_bill_flag = True,
                product_description_flag = True,
                product_extended_amount_flag = True,
                product_flag = True,
                product_manual_entry = 56,
                product_manual_flag = True,
                product_price_flag = True,
                product_quantity_flag = True,
                product_tax_flag = True,
                resolution_flag = True,
                summary_flag = True,
                task = 'All',
                task_flag = True,
                technician_signoff_flag = True,
                time_agreement_flag = True,
                time_bill_flag = True,
                time_date_flag = True,
                time_extended_amount_flag = True,
                time_flag = True,
                time_hours_flag = True,
                time_manual_entry = 56,
                time_manual_flag = True,
                time_member_flag = True,
                time_notes_flag = True,
                time_rate_flag = True,
                time_start_end_flag = True,
                time_tax_flag = True,
                time_work_type_flag = True,
                visible_logo_flag = True
            )
        else:
            return ServiceSignoff(
                name = '',
        )
        """

    def testServiceSignoff(self):
        """Test ServiceSignoff"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
