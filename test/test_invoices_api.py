# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.invoices_api import InvoicesApi


class TestInvoicesApi(unittest.TestCase):
    """InvoicesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InvoicesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_finance_invoices_by_id(self) -> None:
        """Test case for delete_finance_invoices_by_id

        Delete Invoice
        """
        pass

    def test_get_finance_invoices(self) -> None:
        """Test case for get_finance_invoices

        Get List of Invoice
        """
        pass

    def test_get_finance_invoices_by_id(self) -> None:
        """Test case for get_finance_invoices_by_id

        Get Invoice
        """
        pass

    def test_get_finance_invoices_by_id_pdf(self) -> None:
        """Test case for get_finance_invoices_by_id_pdf

        Get Invoice
        """
        pass

    def test_get_finance_invoices_count(self) -> None:
        """Test case for get_finance_invoices_count

        Get Count of Invoice
        """
        pass

    def test_patch_finance_invoices_by_id(self) -> None:
        """Test case for patch_finance_invoices_by_id

        Patch Invoice
        """
        pass

    def test_post_finance_invoices(self) -> None:
        """Test case for post_finance_invoices

        Post Invoice
        """
        pass

    def test_put_finance_invoices_by_id(self) -> None:
        """Test case for put_finance_invoices_by_id

        Put Invoice
        """
        pass


if __name__ == '__main__':
    unittest.main()
