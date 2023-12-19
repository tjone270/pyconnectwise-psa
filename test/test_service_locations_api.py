# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.service_locations_api import ServiceLocationsApi


class TestServiceLocationsApi(unittest.TestCase):
    """ServiceLocationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ServiceLocationsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_service_locations_by_id(self) -> None:
        """Test case for delete_service_locations_by_id

        Delete ServiceLocation
        """
        pass

    def test_get_service_locations(self) -> None:
        """Test case for get_service_locations

        Get List of ServiceLocation
        """
        pass

    def test_get_service_locations_by_id(self) -> None:
        """Test case for get_service_locations_by_id

        Get ServiceLocation
        """
        pass

    def test_get_service_locations_count(self) -> None:
        """Test case for get_service_locations_count

        Get Count of ServiceLocation
        """
        pass

    def test_patch_service_locations_by_id(self) -> None:
        """Test case for patch_service_locations_by_id

        Patch ServiceLocation
        """
        pass

    def test_post_service_locations(self) -> None:
        """Test case for post_service_locations

        Post ServiceLocation
        """
        pass

    def test_put_service_locations_by_id(self) -> None:
        """Test case for put_service_locations_by_id

        Put ServiceLocation
        """
        pass


if __name__ == '__main__':
    unittest.main()
