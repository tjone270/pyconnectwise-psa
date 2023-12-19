# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.entity_types_api import EntityTypesApi


class TestEntityTypesApi(unittest.TestCase):
    """EntityTypesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EntityTypesApi()

    def tearDown(self) -> None:
        pass

    def test_get_company_entity_types(self) -> None:
        """Test case for get_company_entity_types

        Get List of EntityType
        """
        pass

    def test_get_company_entity_types_by_id(self) -> None:
        """Test case for get_company_entity_types_by_id

        Get EntityType
        """
        pass

    def test_get_company_entity_types_count(self) -> None:
        """Test case for get_company_entity_types_count

        Get Count of EntityType
        """
        pass


if __name__ == '__main__':
    unittest.main()
