# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.board_status_info_api import BoardStatusInfoApi


class TestBoardStatusInfoApi(unittest.TestCase):
    """BoardStatusInfoApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BoardStatusInfoApi()

    def tearDown(self) -> None:
        pass

    def test_get_service_boards_by_parent_id_statuses_by_id_info(self) -> None:
        """Test case for get_service_boards_by_parent_id_statuses_by_id_info

        Get BoardStatusInfos
        """
        pass

    def test_get_service_boards_by_parent_id_statuses_info(self) -> None:
        """Test case for get_service_boards_by_parent_id_statuses_info

        Get List of BoardStatusInfos
        """
        pass

    def test_get_service_boards_by_parent_id_statuses_info_count(self) -> None:
        """Test case for get_service_boards_by_parent_id_statuses_info_count

        Get Count of BoardStatusInfos
        """
        pass


if __name__ == '__main__':
    unittest.main()
