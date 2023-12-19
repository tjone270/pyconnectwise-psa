# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.warehouses_api import WarehousesApi


class TestWarehousesApi(unittest.TestCase):
    """WarehousesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = WarehousesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_procurement_warehouses_by_id(self) -> None:
        """Test case for delete_procurement_warehouses_by_id

        Delete Warehouse
        """
        pass

    def test_get_procurement_warehouses(self) -> None:
        """Test case for get_procurement_warehouses

        Get List of Warehouse
        """
        pass

    def test_get_procurement_warehouses_by_id(self) -> None:
        """Test case for get_procurement_warehouses_by_id

        Get Warehouse
        """
        pass

    def test_get_procurement_warehouses_count(self) -> None:
        """Test case for get_procurement_warehouses_count

        Get Count of Warehouse
        """
        pass

    def test_patch_procurement_warehouses_by_id(self) -> None:
        """Test case for patch_procurement_warehouses_by_id

        Patch Warehouse
        """
        pass

    def test_post_procurement_warehouses(self) -> None:
        """Test case for post_procurement_warehouses

        Post Warehouse
        """
        pass

    def test_put_procurement_warehouses_by_id(self) -> None:
        """Test case for put_procurement_warehouses_by_id

        Put Warehouse
        """
        pass


if __name__ == '__main__':
    unittest.main()