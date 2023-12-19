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

from connectwise_psa.models.sales_team import SalesTeam

class TestSalesTeam(unittest.TestCase):
    """SalesTeam unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SalesTeam:
        """Test SalesTeam
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SalesTeam`
        """
        model = SalesTeam()
        if include_optional:
            return SalesTeam(
                info = {
                    'key' : ''
                    },
                id = 56,
                inactive_flag = True,
                sales_team_description = '',
                sales_team_identifier = '',
                sales_team_location = connectwise_psa.models.system_location_reference.SystemLocationReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return SalesTeam(
                sales_team_description = '',
                sales_team_identifier = '',
        )
        """

    def testSalesTeam(self):
        """Test SalesTeam"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()