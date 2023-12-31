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

from connectwise_psa.models.contact_track import ContactTrack

class TestContactTrack(unittest.TestCase):
    """ContactTrack unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContactTrack:
        """Test ContactTrack
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContactTrack`
        """
        model = ContactTrack()
        if include_optional:
            return ContactTrack(
                info = {
                    'key' : ''
                    },
                action_remaining = 56,
                action_taken = 56,
                company = connectwise_psa.models.company_reference.CompanyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                contact = connectwise_psa.models.contact_reference.ContactReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                end_date = '',
                id = 56,
                name = '',
                start_date = '',
                started_by = '',
                track_id = 56
            )
        else:
            return ContactTrack(
        )
        """

    def testContactTrack(self):
        """Test ContactTrack"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
