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

from connectwise_psa.models.note_type_reference import NoteTypeReference

class TestNoteTypeReference(unittest.TestCase):
    """NoteTypeReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NoteTypeReference:
        """Test NoteTypeReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NoteTypeReference`
        """
        model = NoteTypeReference()
        if include_optional:
            return NoteTypeReference(
                info = {
                    'key' : ''
                    },
                id = 56,
                name = ''
            )
        else:
            return NoteTypeReference(
        )
        """

    def testNoteTypeReference(self):
        """Test NoteTypeReference"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()