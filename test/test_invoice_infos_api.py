# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.invoice_infos_api import InvoiceInfosApi


class TestInvoiceInfosApi(unittest.TestCase):
    """InvoiceInfosApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InvoiceInfosApi()

    def tearDown(self) -> None:
        pass

    def test_get_finance_info_invoice_by_id(self) -> None:
        """Test case for get_finance_info_invoice_by_id

        Get InvoiceInfo
        """
        pass


if __name__ == '__main__':
    unittest.main()