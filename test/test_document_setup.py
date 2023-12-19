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

from connectwise_psa.models.document_setup import DocumentSetup

class TestDocumentSetup(unittest.TestCase):
    """DocumentSetup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DocumentSetup:
        """Test DocumentSetup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DocumentSetup`
        """
        model = DocumentSetup()
        if include_optional:
            return DocumentSetup(
                info = {
                    'key' : ''
                    },
                doc_path = '',
                id = 56,
                is_public_flag = True,
                template_output_path = '',
                template_path = '',
                upload_as_link_flag = True
            )
        else:
            return DocumentSetup(
        )
        """

    def testDocumentSetup(self):
        """Test DocumentSetup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()