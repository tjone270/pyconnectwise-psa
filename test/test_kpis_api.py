# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.kpis_api import KPIsApi


class TestKPIsApi(unittest.TestCase):
    """KPIsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = KPIsApi()

    def tearDown(self) -> None:
        pass

    def test_get_system_kpis(self) -> None:
        """Test case for get_system_kpis

        Get List of KPI
        """
        pass

    def test_get_system_kpis_by_id(self) -> None:
        """Test case for get_system_kpis_by_id

        Get KPI
        """
        pass

    def test_get_system_kpis_count(self) -> None:
        """Test case for get_system_kpis_count

        Get Count of KPI
        """
        pass


if __name__ == '__main__':
    unittest.main()
