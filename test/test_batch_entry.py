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

from connectwise_psa.models.batch_entry import BatchEntry

class TestBatchEntry(unittest.TestCase):
    """BatchEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BatchEntry:
        """Test BatchEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BatchEntry`
        """
        model = BatchEntry()
        if include_optional:
            return BatchEntry(
                info = {
                    'key' : ''
                    },
                account_number = '',
                account_type = '',
                adjustment_detail = connectwise_psa.models.adjustment_detail_reference.AdjustmentDetailReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                cost = 1.337,
                cost_of_goods_sold_account_number = '',
                credit = 1.337,
                debit = 1.337,
                expense = connectwise_psa.models.expense_detail_reference.ExpenseDetailReference(
                    _info = {
                        'key' : ''
                        }, 
                    amount = 1.337, 
                    id = 56, ),
                id = 56,
                invoice = connectwise_psa.models.invoice_reference.InvoiceReference(
                    _info = {
                        'key' : ''
                        }, 
                    apply_to_type = '', 
                    billing_type = '', 
                    id = 56, 
                    identifier = '', ),
                item = '',
                line_item = connectwise_psa.models.purchase_order_line_item_reference.PurchaseOrderLineItemReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', ),
                name = '',
                purchase_order = connectwise_psa.models.purchase_order_reference.PurchaseOrderReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                sales_code = '',
                transfer = ''
            )
        else:
            return BatchEntry(
        )
        """

    def testBatchEntry(self):
        """Test BatchEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
