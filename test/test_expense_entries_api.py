# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.expense_entries_api import ExpenseEntriesApi


class TestExpenseEntriesApi(unittest.TestCase):
    """ExpenseEntriesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ExpenseEntriesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_expense_entries_by_id(self) -> None:
        """Test case for delete_expense_entries_by_id

        Delete ExpenseEntry
        """
        pass

    def test_get_expense_entries(self) -> None:
        """Test case for get_expense_entries

        Get List of ExpenseEntry
        """
        pass

    def test_get_expense_entries_by_id(self) -> None:
        """Test case for get_expense_entries_by_id

        Get ExpenseEntry
        """
        pass

    def test_get_expense_entries_count(self) -> None:
        """Test case for get_expense_entries_count

        Get Count of ExpenseEntry
        """
        pass

    def test_patch_expense_entries_by_id(self) -> None:
        """Test case for patch_expense_entries_by_id

        Patch ExpenseEntry
        """
        pass

    def test_post_expense_entries(self) -> None:
        """Test case for post_expense_entries

        Post ExpenseEntry
        """
        pass

    def test_put_expense_entries_by_id(self) -> None:
        """Test case for put_expense_entries_by_id

        Put ExpenseEntry
        """
        pass


if __name__ == '__main__':
    unittest.main()