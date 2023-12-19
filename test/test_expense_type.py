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

from connectwise_psa.models.expense_type import ExpenseType

class TestExpenseType(unittest.TestCase):
    """ExpenseType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExpenseType:
        """Test ExpenseType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExpenseType`
        """
        model = ExpenseType()
        if include_optional:
            return ExpenseType(
                info = {
                    'key' : ''
                    },
                advanced_amount_flag = True,
                amount_caption = '',
                bill_expenses = 'Billable',
                default_flag = True,
                id = 56,
                inactive_flag = True,
                integration_x_ref = '',
                invoice_markup_amount = 1.337,
                invoice_markup_option = 'Amount',
                max_amount = 1.337,
                mileage_flag = True,
                name = '',
                quantity_flag = True,
                reimbursement_rate = 1.337
            )
        else:
            return ExpenseType(
                amount_caption = '',
                bill_expenses = 'Billable',
                invoice_markup_option = 'Amount',
                name = '',
        )
        """

    def testExpenseType(self):
        """Test ExpenseType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()