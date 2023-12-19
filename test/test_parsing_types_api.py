# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.parsing_types_api import ParsingTypesApi


class TestParsingTypesApi(unittest.TestCase):
    """ParsingTypesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ParsingTypesApi()

    def tearDown(self) -> None:
        pass

    def test_get_system_parsing_types(self) -> None:
        """Test case for get_system_parsing_types

        Get List of ParsingType
        """
        pass

    def test_get_system_parsing_types_by_id(self) -> None:
        """Test case for get_system_parsing_types_by_id

        Get ParsingType
        """
        pass

    def test_get_system_parsing_types_count(self) -> None:
        """Test case for get_system_parsing_types_count

        Get Count of ParsingType
        """
        pass


if __name__ == '__main__':
    unittest.main()
