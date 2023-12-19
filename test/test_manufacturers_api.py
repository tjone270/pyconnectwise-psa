# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.manufacturers_api import ManufacturersApi


class TestManufacturersApi(unittest.TestCase):
    """ManufacturersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ManufacturersApi()

    def tearDown(self) -> None:
        pass

    def test_delete_procurement_manufacturers_by_id(self) -> None:
        """Test case for delete_procurement_manufacturers_by_id

        Delete Manufacturer
        """
        pass

    def test_get_procurement_manufacturers(self) -> None:
        """Test case for get_procurement_manufacturers

        Get List of Manufacturer
        """
        pass

    def test_get_procurement_manufacturers_by_id(self) -> None:
        """Test case for get_procurement_manufacturers_by_id

        Get Manufacturer
        """
        pass

    def test_get_procurement_manufacturers_count(self) -> None:
        """Test case for get_procurement_manufacturers_count

        Get Count of Manufacturer
        """
        pass

    def test_patch_procurement_manufacturers_by_id(self) -> None:
        """Test case for patch_procurement_manufacturers_by_id

        Patch Manufacturer
        """
        pass

    def test_post_procurement_manufacturers(self) -> None:
        """Test case for post_procurement_manufacturers

        Post Manufacturer
        """
        pass

    def test_put_procurement_manufacturers_by_id(self) -> None:
        """Test case for put_procurement_manufacturers_by_id

        Put Manufacturer
        """
        pass


if __name__ == '__main__':
    unittest.main()