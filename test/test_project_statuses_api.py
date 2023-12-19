# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.project_statuses_api import ProjectStatusesApi


class TestProjectStatusesApi(unittest.TestCase):
    """ProjectStatusesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectStatusesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_project_statuses_by_id(self) -> None:
        """Test case for delete_project_statuses_by_id

        Delete ProjectStatus
        """
        pass

    def test_get_project_statuses(self) -> None:
        """Test case for get_project_statuses

        Get List of ProjectStatus
        """
        pass

    def test_get_project_statuses_by_id(self) -> None:
        """Test case for get_project_statuses_by_id

        Get ProjectStatus
        """
        pass

    def test_get_project_statuses_count(self) -> None:
        """Test case for get_project_statuses_count

        Get Count of ProjectStatus
        """
        pass

    def test_patch_project_statuses_by_id(self) -> None:
        """Test case for patch_project_statuses_by_id

        Patch ProjectStatus
        """
        pass

    def test_post_project_statuses(self) -> None:
        """Test case for post_project_statuses

        Post ProjectStatus
        """
        pass

    def test_put_project_statuses_by_id(self) -> None:
        """Test case for put_project_statuses_by_id

        Put ProjectStatus
        """
        pass


if __name__ == '__main__':
    unittest.main()
