# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.catalog_inventories_api import CatalogInventoriesApi


class TestCatalogInventoriesApi(unittest.TestCase):
    """CatalogInventoriesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CatalogInventoriesApi()

    def tearDown(self) -> None:
        pass

    def test_get_procurement_catalog_by_parent_id_inventory(self) -> None:
        """Test case for get_procurement_catalog_by_parent_id_inventory

        Get List of CatalogInventory
        """
        pass

    def test_get_procurement_catalog_by_parent_id_inventory_by_id(self) -> None:
        """Test case for get_procurement_catalog_by_parent_id_inventory_by_id

        Get CatalogInventory
        """
        pass

    def test_get_procurement_catalog_by_parent_id_inventory_count(self) -> None:
        """Test case for get_procurement_catalog_by_parent_id_inventory_count

        Get Count of CatalogInventory
        """
        pass


if __name__ == '__main__':
    unittest.main()