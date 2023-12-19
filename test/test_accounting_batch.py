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

from connectwise_psa.models.accounting_batch import AccountingBatch

class TestAccountingBatch(unittest.TestCase):
    """AccountingBatch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountingBatch:
        """Test AccountingBatch
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountingBatch`
        """
        model = AccountingBatch()
        if include_optional:
            return AccountingBatch(
                info = {
                    'key' : ''
                    },
                batch_identifier = '',
                closed_flag = True,
                export_expenses_flag = True,
                export_invoices_flag = True,
                export_products_flag = True,
                id = 56
            )
        else:
            return AccountingBatch(
        )
        """

    def testAccountingBatch(self):
        """Test AccountingBatch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
