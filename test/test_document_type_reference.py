# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from connectwise_psa.models.document_type_reference import DocumentTypeReference

class TestDocumentTypeReference(unittest.TestCase):
    """DocumentTypeReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DocumentTypeReference:
        """Test DocumentTypeReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DocumentTypeReference`
        """
        model = DocumentTypeReference()
        if include_optional:
            return DocumentTypeReference(
                info = {
                    'key' : ''
                    },
                id = 56,
                name = ''
            )
        else:
            return DocumentTypeReference(
        )
        """

    def testDocumentTypeReference(self):
        """Test DocumentTypeReference"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
