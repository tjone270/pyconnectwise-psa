# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.billing_term_infos_api import BillingTermInfosApi


class TestBillingTermInfosApi(unittest.TestCase):
    """BillingTermInfosApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BillingTermInfosApi()

    def tearDown(self) -> None:
        pass

    def test_get_finance_billing_terms_by_id_info(self) -> None:
        """Test case for get_finance_billing_terms_by_id_info

        Get BillingTermInfo
        """
        pass

    def test_get_finance_billing_terms_info(self) -> None:
        """Test case for get_finance_billing_terms_info

        Get List of BillingTermInfo
        """
        pass

    def test_get_finance_billing_terms_info_count(self) -> None:
        """Test case for get_finance_billing_terms_info_count

        Get Count of BillingTermInfo
        """
        pass


if __name__ == '__main__':
    unittest.main()