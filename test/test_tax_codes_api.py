# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.tax_codes_api import TaxCodesApi


class TestTaxCodesApi(unittest.TestCase):
    """TaxCodesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TaxCodesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_finance_tax_codes_by_id(self) -> None:
        """Test case for delete_finance_tax_codes_by_id

        Delete Usage
        """
        pass

    def test_get_finance_tax_codes(self) -> None:
        """Test case for get_finance_tax_codes

        Get List of TaxCode
        """
        pass

    def test_get_finance_tax_codes_by_id(self) -> None:
        """Test case for get_finance_tax_codes_by_id

        Get TaxCode
        """
        pass

    def test_get_finance_tax_codes_by_id_usages(self) -> None:
        """Test case for get_finance_tax_codes_by_id_usages

        Get List of Usage Count
        """
        pass

    def test_get_finance_tax_codes_by_id_usages_list(self) -> None:
        """Test case for get_finance_tax_codes_by_id_usages_list

        Get List of Usage
        """
        pass

    def test_get_finance_tax_codes_count(self) -> None:
        """Test case for get_finance_tax_codes_count

        Get Count of TaxCode
        """
        pass

    def test_patch_finance_tax_codes_by_id(self) -> None:
        """Test case for patch_finance_tax_codes_by_id

        Patch TaxCode
        """
        pass

    def test_post_finance_tax_codes(self) -> None:
        """Test case for post_finance_tax_codes

        Post TaxCode
        """
        pass

    def test_post_finance_tax_codes_by_id_copy(self) -> None:
        """Test case for post_finance_tax_codes_by_id_copy

        Post TaxCode
        """
        pass

    def test_put_finance_tax_codes_by_id(self) -> None:
        """Test case for put_finance_tax_codes_by_id

        Put TaxCode
        """
        pass


if __name__ == '__main__':
    unittest.main()
