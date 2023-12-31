# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.currencies_api import CurrenciesApi


class TestCurrenciesApi(unittest.TestCase):
    """CurrenciesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CurrenciesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_finance_currencies_by_id(self) -> None:
        """Test case for delete_finance_currencies_by_id

        Delete Currency
        """
        pass

    def test_get_finance_currencies(self) -> None:
        """Test case for get_finance_currencies

        Get List of Currency
        """
        pass

    def test_get_finance_currencies_by_id(self) -> None:
        """Test case for get_finance_currencies_by_id

        Get Currency
        """
        pass

    def test_get_finance_currencies_by_id_usages(self) -> None:
        """Test case for get_finance_currencies_by_id_usages

        Get List of Usage Count
        """
        pass

    def test_get_finance_currencies_by_id_usages_list(self) -> None:
        """Test case for get_finance_currencies_by_id_usages_list

        Get List of Usage
        """
        pass

    def test_get_finance_currencies_count(self) -> None:
        """Test case for get_finance_currencies_count

        Get Count of Currency
        """
        pass

    def test_patch_finance_currencies_by_id(self) -> None:
        """Test case for patch_finance_currencies_by_id

        Patch Currency
        """
        pass

    def test_post_finance_currencies(self) -> None:
        """Test case for post_finance_currencies

        Post Currency
        """
        pass

    def test_put_finance_currencies_by_id(self) -> None:
        """Test case for put_finance_currencies_by_id

        Put Currency
        """
        pass


if __name__ == '__main__':
    unittest.main()
