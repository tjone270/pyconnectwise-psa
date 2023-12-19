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

from connectwise_psa.models.export_accounting_batch_request import ExportAccountingBatchRequest

class TestExportAccountingBatchRequest(unittest.TestCase):
    """ExportAccountingBatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExportAccountingBatchRequest:
        """Test ExportAccountingBatchRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExportAccountingBatchRequest`
        """
        model = ExportAccountingBatchRequest()
        if include_optional:
            return ExportAccountingBatchRequest(
                batch_identifier = '',
                excluded_expense_ids = [
                    56
                    ],
                excluded_invoice_ids = [
                    56
                    ],
                excluded_product_ids = [
                    ''
                    ],
                export_expenses_flag = True,
                export_invoices_flag = True,
                export_payments_flag = True,
                export_products_flag = True,
                gl_interface_identifier = '',
                included_expense_ids = [
                    56
                    ],
                included_invoice_ids = [
                    56
                    ],
                included_payment_ids = [
                    56
                    ],
                included_product_ids = [
                    ''
                    ],
                location_id = 56,
                summarize_invoices = 'Default',
                thru_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ExportAccountingBatchRequest(
        )
        """

    def testExportAccountingBatchRequest(self):
        """Test ExportAccountingBatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
