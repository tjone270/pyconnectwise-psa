# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.catalogs_item_api import CatalogsItemApi


class TestCatalogsItemApi(unittest.TestCase):
    """CatalogsItemApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CatalogsItemApi()

    def tearDown(self) -> None:
        pass

    def test_delete_procurement_catalog_by_id(self) -> None:
        """Test case for delete_procurement_catalog_by_id

        Delete CatalogItem
        """
        pass

    def test_get_procurement_catalog(self) -> None:
        """Test case for get_procurement_catalog

        Get List of CatalogItem
        """
        pass

    def test_get_procurement_catalog_by_catalog_item_identifier_quantity_on_hand(self) -> None:
        """Test case for get_procurement_catalog_by_catalog_item_identifier_quantity_on_hand

        Get Count of CatalogItem
        """
        pass

    def test_get_procurement_catalog_by_id(self) -> None:
        """Test case for get_procurement_catalog_by_id

        Get CatalogItem
        """
        pass

    def test_get_procurement_catalog_by_id_info(self) -> None:
        """Test case for get_procurement_catalog_by_id_info

        Get CatalogItemInfo
        """
        pass

    def test_get_procurement_catalog_count(self) -> None:
        """Test case for get_procurement_catalog_count

        Get Count of CatalogItem
        """
        pass

    def test_get_procurement_catalog_info(self) -> None:
        """Test case for get_procurement_catalog_info

        Get List of CatalogItemInfo
        """
        pass

    def test_get_procurement_catalog_info_count(self) -> None:
        """Test case for get_procurement_catalog_info_count

        Get Count of CatalogItemInfo
        """
        pass

    def test_patch_procurement_catalog_by_id(self) -> None:
        """Test case for patch_procurement_catalog_by_id

        Patch CatalogItem
        """
        pass

    def test_post_procurement_catalog(self) -> None:
        """Test case for post_procurement_catalog

        Post CatalogItem
        """
        pass

    def test_post_procurement_catalog_by_id_pricing(self) -> None:
        """Test case for post_procurement_catalog_by_id_pricing

        Post CatalogPricing
        """
        pass

    def test_put_procurement_catalog_by_id(self) -> None:
        """Test case for put_procurement_catalog_by_id

        Put CatalogItem
        """
        pass


if __name__ == '__main__':
    unittest.main()