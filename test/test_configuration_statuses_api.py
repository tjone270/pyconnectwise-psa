# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.configuration_statuses_api import ConfigurationStatusesApi


class TestConfigurationStatusesApi(unittest.TestCase):
    """ConfigurationStatusesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConfigurationStatusesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_company_configurations_statuses_by_id(self) -> None:
        """Test case for delete_company_configurations_statuses_by_id

        Delete ConfigurationStatus
        """
        pass

    def test_get_company_configurations_statuses(self) -> None:
        """Test case for get_company_configurations_statuses

        Get List of ConfigurationStatus
        """
        pass

    def test_get_company_configurations_statuses_by_id(self) -> None:
        """Test case for get_company_configurations_statuses_by_id

        Get ConfigurationStatus
        """
        pass

    def test_get_company_configurations_statuses_by_id_usages(self) -> None:
        """Test case for get_company_configurations_statuses_by_id_usages

        Get List of Usage Count
        """
        pass

    def test_get_company_configurations_statuses_by_id_usages_list(self) -> None:
        """Test case for get_company_configurations_statuses_by_id_usages_list

        Get List of Usage
        """
        pass

    def test_get_company_configurations_statuses_count(self) -> None:
        """Test case for get_company_configurations_statuses_count

        Get Count of ConfigurationStatus
        """
        pass

    def test_patch_company_configurations_statuses_by_id(self) -> None:
        """Test case for patch_company_configurations_statuses_by_id

        Patch ConfigurationStatus
        """
        pass

    def test_post_company_configurations_statuses(self) -> None:
        """Test case for post_company_configurations_statuses

        Post ConfigurationStatus
        """
        pass

    def test_put_company_configurations_statuses_by_id(self) -> None:
        """Test case for put_company_configurations_statuses_by_id

        Put ConfigurationStatus
        """
        pass


if __name__ == '__main__':
    unittest.main()
