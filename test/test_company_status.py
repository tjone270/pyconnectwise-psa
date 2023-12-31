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

from connectwise_psa.models.company_status import CompanyStatus

class TestCompanyStatus(unittest.TestCase):
    """CompanyStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompanyStatus:
        """Test CompanyStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompanyStatus`
        """
        model = CompanyStatus()
        if include_optional:
            return CompanyStatus(
                info = {
                    'key' : ''
                    },
                cancel_open_tracks_flag = True,
                custom_note_flag = True,
                default_flag = True,
                disallow_saving_flag = True,
                id = 56,
                inactive_flag = True,
                name = '',
                notification_message = '',
                notify_flag = True,
                track = connectwise_psa.models.track_reference.TrackReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return CompanyStatus(
                name = '',
        )
        """

    def testCompanyStatus(self):
        """Test CompanyStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
