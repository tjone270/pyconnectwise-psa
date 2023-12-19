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

from connectwise_psa.models.gl_export_expense_bill import GLExportExpenseBill

class TestGLExportExpenseBill(unittest.TestCase):
    """GLExportExpenseBill unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GLExportExpenseBill:
        """Test GLExportExpenseBill
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GLExportExpenseBill`
        """
        model = GLExportExpenseBill()
        if include_optional:
            return GLExportExpenseBill(
                ap_account_number = '',
                currency = connectwise_psa.models.currency_reference.CurrencyReference(
                    _info = {
                        'key' : ''
                        }, 
                    currency_code = '', 
                    currency_identifier = '', 
                    decimal_separator = '', 
                    display_id_flag = True, 
                    display_symbol_flag = True, 
                    id = 56, 
                    name = '', 
                    negative_parentheses_flag = True, 
                    number_of_decimals = 56, 
                    right_align = True, 
                    symbol = '', 
                    thousands_separator = '', ),
                detail = [
                    connectwise_psa.models.gl_export_expense_bill_detail.GLExportExpenseBillDetail(
                        account_number = '', 
                        billable = True, 
                        company = connectwise_psa.models.company_reference.CompanyReference(
                            _info = {
                                'key' : ''
                                }, 
                            id = 56, 
                            identifier = '', 
                            name = '', ), 
                        company_advance = True, 
                        currency = connectwise_psa.models.currency_reference.CurrencyReference(
                            currency_code = '', 
                            currency_identifier = '', 
                            decimal_separator = '', 
                            display_id_flag = True, 
                            display_symbol_flag = True, 
                            id = 56, 
                            name = '', 
                            negative_parentheses_flag = True, 
                            number_of_decimals = 56, 
                            right_align = True, 
                            symbol = '', 
                            thousands_separator = '', ), 
                        document_date = '', 
                        expense_class = connectwise_psa.models.classification_reference.ClassificationReference(
                            id = 56, 
                            name = '', ), 
                        gl_type_id = '', 
                        id = [
                            56
                            ], 
                        memo = '', 
                        reimbursable = True, 
                        total = 1.337, )
                    ],
                document_date = '',
                document_number = '',
                document_type = '',
                gl_class = '',
                id = 56,
                member = connectwise_psa.models.member_reference.MemberReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                memo = '',
                total = 1.337,
                vendor_number = ''
            )
        else:
            return GLExportExpenseBill(
        )
        """

    def testGLExportExpenseBill(self):
        """Test GLExportExpenseBill"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()