# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.document_types_api import DocumentTypesApi


class TestDocumentTypesApi(unittest.TestCase):
    """DocumentTypesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DocumentTypesApi()

    def tearDown(self) -> None:
        pass

    def test_get_system_document_types_by_id_info(self) -> None:
        """Test case for get_system_document_types_by_id_info

        Get DocumentType
        """
        pass

    def test_get_system_document_types_info(self) -> None:
        """Test case for get_system_document_types_info

        Get List of DocumentType
        """
        pass

    def test_get_system_document_types_info_count(self) -> None:
        """Test case for get_system_document_types_info_count

        Get Count of DocumentType
        """
        pass


if __name__ == '__main__':
    unittest.main()
