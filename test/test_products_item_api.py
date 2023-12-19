# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.products_item_api import ProductsItemApi


class TestProductsItemApi(unittest.TestCase):
    """ProductsItemApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProductsItemApi()

    def tearDown(self) -> None:
        pass

    def test_delete_procurement_products_by_id(self) -> None:
        """Test case for delete_procurement_products_by_id

        Delete ProductItem
        """
        pass

    def test_get_procurement_products(self) -> None:
        """Test case for get_procurement_products

        Get List of ProductItem
        """
        pass

    def test_get_procurement_products_by_id(self) -> None:
        """Test case for get_procurement_products_by_id

        Get ProductItem
        """
        pass

    def test_get_procurement_products_count(self) -> None:
        """Test case for get_procurement_products_count

        Get Count of ProductItem
        """
        pass

    def test_patch_procurement_products_by_id(self) -> None:
        """Test case for patch_procurement_products_by_id

        Patch ProductItem
        """
        pass

    def test_post_procurement_products(self) -> None:
        """Test case for post_procurement_products

        Post ProductItem
        """
        pass

    def test_post_procurement_products_by_id_detach(self) -> None:
        """Test case for post_procurement_products_by_id_detach

        Post ProductDetach
        """
        pass

    def test_put_procurement_products_by_id(self) -> None:
        """Test case for put_procurement_products_by_id

        Put ProductItem
        """
        pass


if __name__ == '__main__':
    unittest.main()
