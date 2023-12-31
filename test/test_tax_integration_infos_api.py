# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.tax_integration_infos_api import TaxIntegrationInfosApi


class TestTaxIntegrationInfosApi(unittest.TestCase):
    """TaxIntegrationInfosApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TaxIntegrationInfosApi()

    def tearDown(self) -> None:
        pass

    def test_get_finance_info_tax_integrations(self) -> None:
        """Test case for get_finance_info_tax_integrations

        Get List of TaxIntegrationInfo
        """
        pass

    def test_get_finance_info_tax_integrations_by_id(self) -> None:
        """Test case for get_finance_info_tax_integrations_by_id

        Get TaxIntegrationInfo
        """
        pass

    def test_get_finance_info_tax_integrations_count(self) -> None:
        """Test case for get_finance_info_tax_integrations_count

        Get Count of TaxIntegrationInfo
        """
        pass


if __name__ == '__main__':
    unittest.main()
