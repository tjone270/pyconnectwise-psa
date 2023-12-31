# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.schedule_entries_api import ScheduleEntriesApi


class TestScheduleEntriesApi(unittest.TestCase):
    """ScheduleEntriesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ScheduleEntriesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_schedule_entries_by_id(self) -> None:
        """Test case for delete_schedule_entries_by_id

        Delete ScheduleEntry
        """
        pass

    def test_get_schedule_entries(self) -> None:
        """Test case for get_schedule_entries

        Get List of ScheduleEntry
        """
        pass

    def test_get_schedule_entries_by_id(self) -> None:
        """Test case for get_schedule_entries_by_id

        Get ScheduleEntry
        """
        pass

    def test_get_schedule_entries_count(self) -> None:
        """Test case for get_schedule_entries_count

        Get Count of ScheduleEntry
        """
        pass

    def test_patch_schedule_entries_by_id(self) -> None:
        """Test case for patch_schedule_entries_by_id

        Patch ScheduleEntry
        """
        pass

    def test_post_schedule_entries(self) -> None:
        """Test case for post_schedule_entries

        Post ScheduleEntry
        """
        pass

    def test_put_schedule_entries_by_id(self) -> None:
        """Test case for put_schedule_entries_by_id

        Put ScheduleEntry
        """
        pass


if __name__ == '__main__':
    unittest.main()
