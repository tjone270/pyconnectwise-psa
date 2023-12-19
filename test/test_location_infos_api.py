# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.location_infos_api import LocationInfosApi


class TestLocationInfosApi(unittest.TestCase):
    """LocationInfosApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LocationInfosApi()

    def tearDown(self) -> None:
        pass

    def test_get_system_info_locations(self) -> None:
        """Test case for get_system_info_locations

        Get List of LocationInfo
        """
        pass

    def test_get_system_info_locations_by_id(self) -> None:
        """Test case for get_system_info_locations_by_id

        Get LocationInfo
        """
        pass

    def test_get_system_info_locations_count(self) -> None:
        """Test case for get_system_info_locations_count

        Get Count of LocationInfo
        """
        pass


if __name__ == '__main__':
    unittest.main()
