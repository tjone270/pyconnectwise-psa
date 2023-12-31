# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.accounting_packages_api import AccountingPackagesApi


class TestAccountingPackagesApi(unittest.TestCase):
    """AccountingPackagesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AccountingPackagesApi()

    def tearDown(self) -> None:
        pass

    def test_get_finance_accounting_packages(self) -> None:
        """Test case for get_finance_accounting_packages

        Get List of AccountingPackage
        """
        pass

    def test_get_finance_accounting_packages_by_id(self) -> None:
        """Test case for get_finance_accounting_packages_by_id

        Get AccountingPackage
        """
        pass

    def test_get_finance_accounting_packages_count(self) -> None:
        """Test case for get_finance_accounting_packages_count

        Get Count of AccountingPackage
        """
        pass


if __name__ == '__main__':
    unittest.main()
