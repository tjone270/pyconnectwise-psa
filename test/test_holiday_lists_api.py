# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.holiday_lists_api import HolidayListsApi


class TestHolidayListsApi(unittest.TestCase):
    """HolidayListsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = HolidayListsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_schedule_holiday_lists_by_id(self) -> None:
        """Test case for delete_schedule_holiday_lists_by_id

        Delete HolidayList
        """
        pass

    def test_get_schedule_holiday_lists(self) -> None:
        """Test case for get_schedule_holiday_lists

        Get List of HolidayList
        """
        pass

    def test_get_schedule_holiday_lists_by_id(self) -> None:
        """Test case for get_schedule_holiday_lists_by_id

        Get HolidayList
        """
        pass

    def test_get_schedule_holiday_lists_by_id_usages(self) -> None:
        """Test case for get_schedule_holiday_lists_by_id_usages

        Get List of Usage Count
        """
        pass

    def test_get_schedule_holiday_lists_by_id_usages_list(self) -> None:
        """Test case for get_schedule_holiday_lists_by_id_usages_list

        Get List of Usage
        """
        pass

    def test_get_schedule_holiday_lists_count(self) -> None:
        """Test case for get_schedule_holiday_lists_count

        Get Count of Usage
        """
        pass

    def test_patch_schedule_holiday_lists_by_id(self) -> None:
        """Test case for patch_schedule_holiday_lists_by_id

        Patch HolidayList
        """
        pass

    def test_post_schedule_holiday_lists(self) -> None:
        """Test case for post_schedule_holiday_lists

        Post HolidayList
        """
        pass

    def test_post_schedule_holiday_lists_copy(self) -> None:
        """Test case for post_schedule_holiday_lists_copy

        Post HolidayList
        """
        pass

    def test_put_schedule_holiday_lists_by_id(self) -> None:
        """Test case for put_schedule_holiday_lists_by_id

        Put HolidayList
        """
        pass


if __name__ == '__main__':
    unittest.main()