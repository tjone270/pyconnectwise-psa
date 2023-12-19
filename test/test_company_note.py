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

from connectwise_psa.models.company_note import CompanyNote

class TestCompanyNote(unittest.TestCase):
    """CompanyNote unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompanyNote:
        """Test CompanyNote
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompanyNote`
        """
        model = CompanyNote()
        if include_optional:
            return CompanyNote(
                info = {
                    'key' : ''
                    },
                company = connectwise_psa.models.company_reference.CompanyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                entered_by = '',
                flagged = True,
                id = 56,
                text = '',
                type = connectwise_psa.models.note_type_reference.NoteTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return CompanyNote(
                text = '',
        )
        """

    def testCompanyNote(self):
        """Test CompanyNote"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
