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

from connectwise_psa.models.gl_export_expense import GLExportExpense

class TestGLExportExpense(unittest.TestCase):
    """GLExportExpense unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GLExportExpense:
        """Test GLExportExpense
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GLExportExpense`
        """
        model = GLExportExpense()
        if include_optional:
            return GLExportExpense(
                account_number = '',
                ap_account_number = '',
                ap_class = '',
                company = connectwise_psa.models.company_reference.CompanyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                company_account_number = '',
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
                description = '',
                document_date = '',
                document_type = '',
                gl_class = '',
                gl_type_id = '',
                id = 56,
                member = connectwise_psa.models.member_reference.MemberReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                memo = '',
                offset = connectwise_psa.models.gl_export_expense_offset.GLExportExpenseOffset(
                    account_number = '', 
                    description = '', 
                    document_date = '', 
                    document_type = '', 
                    gl_class = '', 
                    gl_type_id = '', 
                    id = 56, 
                    member = connectwise_psa.models.member_reference.MemberReference(
                        _info = {
                            'key' : ''
                            }, 
                        id = 56, 
                        identifier = '', 
                        name = '', ), 
                    memo = '', 
                    total = 1.337, ),
                period_end_date = '',
                period_start_date = '',
                project = connectwise_psa.models.project_reference.ProjectReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                total = 1.337,
                vendor_number = ''
            )
        else:
            return GLExportExpense(
        )
        """

    def testGLExportExpense(self):
        """Test GLExportExpense"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()