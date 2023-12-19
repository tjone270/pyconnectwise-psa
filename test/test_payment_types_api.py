# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.payment_types_api import PaymentTypesApi


class TestPaymentTypesApi(unittest.TestCase):
    """PaymentTypesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PaymentTypesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_expense_payment_types_by_id(self) -> None:
        """Test case for delete_expense_payment_types_by_id

        Delete PaymentType
        """
        pass

    def test_get_expense_payment_types(self) -> None:
        """Test case for get_expense_payment_types

        Get List of PaymentType
        """
        pass

    def test_get_expense_payment_types_by_id(self) -> None:
        """Test case for get_expense_payment_types_by_id

        Get PaymentType
        """
        pass

    def test_get_expense_payment_types_count(self) -> None:
        """Test case for get_expense_payment_types_count

        Get Count of PaymentType
        """
        pass

    def test_patch_expense_payment_types_by_id(self) -> None:
        """Test case for patch_expense_payment_types_by_id

        Patch PaymentType
        """
        pass

    def test_post_expense_payment_types(self) -> None:
        """Test case for post_expense_payment_types

        Post PaymentType
        """
        pass

    def test_put_expense_payment_types_by_id(self) -> None:
        """Test case for put_expense_payment_types_by_id

        Put PaymentType
        """
        pass


if __name__ == '__main__':
    unittest.main()