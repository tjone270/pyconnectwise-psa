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

from connectwise_psa.models.opportunity_status import OpportunityStatus

class TestOpportunityStatus(unittest.TestCase):
    """OpportunityStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OpportunityStatus:
        """Test OpportunityStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OpportunityStatus`
        """
        model = OpportunityStatus()
        if include_optional:
            return OpportunityStatus(
                info = {
                    'key' : ''
                    },
                closed_flag = True,
                date_entered = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                default_flag = True,
                entered_by = '',
                id = 56,
                inactive_flag = True,
                lost_flag = True,
                name = '',
                won_flag = True
            )
        else:
            return OpportunityStatus(
                name = '',
        )
        """

    def testOpportunityStatus(self):
        """Test OpportunityStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()