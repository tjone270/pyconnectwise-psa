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

from connectwise_psa.models.opportunity_priority_reference import OpportunityPriorityReference

class TestOpportunityPriorityReference(unittest.TestCase):
    """OpportunityPriorityReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OpportunityPriorityReference:
        """Test OpportunityPriorityReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OpportunityPriorityReference`
        """
        model = OpportunityPriorityReference()
        if include_optional:
            return OpportunityPriorityReference(
                info = {
                    'key' : ''
                    },
                id = 56,
                name = ''
            )
        else:
            return OpportunityPriorityReference(
        )
        """

    def testOpportunityPriorityReference(self):
        """Test OpportunityPriorityReference"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()