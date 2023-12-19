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

from connectwise_psa.models.ticket_sync import TicketSync

class TestTicketSync(unittest.TestCase):
    """TicketSync unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TicketSync:
        """Test TicketSync
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TicketSync`
        """
        model = TicketSync()
        if include_optional:
            return TicketSync(
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
                id = 56,
                integrator_login = connectwise_psa.models.integrator_login_reference.IntegratorLoginReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                internal_analysis_flag = True,
                name = '',
                password = '',
                problem_description_flag = True,
                psg = '',
                resolution_flag = True,
                url = '',
                user_name = '',
                vendor_type = 'Zenith'
            )
        else:
            return TicketSync(
                name = '',
                url = '',
                vendor_type = 'Zenith',
        )
        """

    def testTicketSync(self):
        """Test TicketSync"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
