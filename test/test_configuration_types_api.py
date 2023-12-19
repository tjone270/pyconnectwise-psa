# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.configuration_types_api import ConfigurationTypesApi


class TestConfigurationTypesApi(unittest.TestCase):
    """ConfigurationTypesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConfigurationTypesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_company_configurations_types_by_id(self) -> None:
        """Test case for delete_company_configurations_types_by_id

        Delete ConfigurationType
        """
        pass

    def test_get_company_configurations_types(self) -> None:
        """Test case for get_company_configurations_types

        Get List of ConfigurationType
        """
        pass

    def test_get_company_configurations_types_by_id(self) -> None:
        """Test case for get_company_configurations_types_by_id

        Get ConfigurationType
        """
        pass

    def test_get_company_configurations_types_by_id_usages(self) -> None:
        """Test case for get_company_configurations_types_by_id_usages

        Get List of Usage Count
        """
        pass

    def test_get_company_configurations_types_by_id_usages_list(self) -> None:
        """Test case for get_company_configurations_types_by_id_usages_list

        Get List of Usage
        """
        pass

    def test_get_company_configurations_types_count(self) -> None:
        """Test case for get_company_configurations_types_count

        Get Count of ConfigurationType
        """
        pass

    def test_patch_company_configurations_types_by_id(self) -> None:
        """Test case for patch_company_configurations_types_by_id

        Patch ConfigurationType
        """
        pass

    def test_post_company_configurations_types(self) -> None:
        """Test case for post_company_configurations_types

        Post ConfigurationType
        """
        pass

    def test_post_company_configurations_types_copy(self) -> None:
        """Test case for post_company_configurations_types_copy

        Post Board
        """
        pass

    def test_put_company_configurations_types_by_id(self) -> None:
        """Test case for put_company_configurations_types_by_id

        Put ConfigurationType
        """
        pass


if __name__ == '__main__':
    unittest.main()
