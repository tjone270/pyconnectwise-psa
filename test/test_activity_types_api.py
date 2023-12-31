# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.activity_types_api import ActivityTypesApi


class TestActivityTypesApi(unittest.TestCase):
    """ActivityTypesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ActivityTypesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_sales_activities_types_by_id(self) -> None:
        """Test case for delete_sales_activities_types_by_id

        Delete ActivityType
        """
        pass

    def test_get_sales_activities_types(self) -> None:
        """Test case for get_sales_activities_types

        Get List of ActivityType
        """
        pass

    def test_get_sales_activities_types_by_id(self) -> None:
        """Test case for get_sales_activities_types_by_id

        Get ActivityType
        """
        pass

    def test_get_sales_activities_types_by_id_usages(self) -> None:
        """Test case for get_sales_activities_types_by_id_usages

        Get List of Usage Count
        """
        pass

    def test_get_sales_activities_types_by_id_usages_list(self) -> None:
        """Test case for get_sales_activities_types_by_id_usages_list

        Get List of Usage
        """
        pass

    def test_get_sales_activities_types_count(self) -> None:
        """Test case for get_sales_activities_types_count

        Get Count of ActivityType
        """
        pass

    def test_patch_sales_activities_types_by_id(self) -> None:
        """Test case for patch_sales_activities_types_by_id

        Patch ActivityType
        """
        pass

    def test_post_sales_activities_types(self) -> None:
        """Test case for post_sales_activities_types

        Post ActivityType
        """
        pass

    def test_put_sales_activities_types_by_id(self) -> None:
        """Test case for put_sales_activities_types_by_id

        Put ActivityType
        """
        pass


if __name__ == '__main__':
    unittest.main()
