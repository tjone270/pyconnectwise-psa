# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.ownership_type_infos_api import OwnershipTypeInfosApi


class TestOwnershipTypeInfosApi(unittest.TestCase):
    """OwnershipTypeInfosApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OwnershipTypeInfosApi()

    def tearDown(self) -> None:
        pass

    def test_get_company_ownership_types_by_id_info(self) -> None:
        """Test case for get_company_ownership_types_by_id_info

        Get OwnershipTypeInfos
        """
        pass

    def test_get_company_ownership_types_info(self) -> None:
        """Test case for get_company_ownership_types_info

        Get List of OwnershipTypeInfos
        """
        pass

    def test_get_company_ownership_types_info_count(self) -> None:
        """Test case for get_company_ownership_types_info_count

        Get Count of OwnershipTypeInfos
        """
        pass


if __name__ == '__main__':
    unittest.main()