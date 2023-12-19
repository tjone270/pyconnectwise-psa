# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.product_types_api import ProductTypesApi


class TestProductTypesApi(unittest.TestCase):
    """ProductTypesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProductTypesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_procurement_types_by_id(self) -> None:
        """Test case for delete_procurement_types_by_id

        Delete ProductType
        """
        pass

    def test_get_procurement_types(self) -> None:
        """Test case for get_procurement_types

        Get List of ProductType
        """
        pass

    def test_get_procurement_types_by_id(self) -> None:
        """Test case for get_procurement_types_by_id

        Get ProductType
        """
        pass

    def test_get_procurement_types_by_id_info(self) -> None:
        """Test case for get_procurement_types_by_id_info

        Get ProductTypeInfo
        """
        pass

    def test_get_procurement_types_by_id_usages(self) -> None:
        """Test case for get_procurement_types_by_id_usages

        Get List of Usage Count
        """
        pass

    def test_get_procurement_types_by_id_usages_list(self) -> None:
        """Test case for get_procurement_types_by_id_usages_list

        Get List of Usage
        """
        pass

    def test_get_procurement_types_count(self) -> None:
        """Test case for get_procurement_types_count

        Get Count of ProductType
        """
        pass

    def test_get_procurement_types_info(self) -> None:
        """Test case for get_procurement_types_info

        Get List of ProductTypeInfo
        """
        pass

    def test_get_procurement_types_info_count(self) -> None:
        """Test case for get_procurement_types_info_count

        Get Count of ProductTypeInfo
        """
        pass

    def test_patch_procurement_types_by_id(self) -> None:
        """Test case for patch_procurement_types_by_id

        Patch ProductType
        """
        pass

    def test_post_procurement_types(self) -> None:
        """Test case for post_procurement_types

        Post ProductType
        """
        pass

    def test_put_procurement_types_by_id(self) -> None:
        """Test case for put_procurement_types_by_id

        Put ProductType
        """
        pass


if __name__ == '__main__':
    unittest.main()
