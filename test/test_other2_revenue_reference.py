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

from connectwise_psa.models.other2_revenue_reference import Other2RevenueReference

class TestOther2RevenueReference(unittest.TestCase):
    """Other2RevenueReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Other2RevenueReference:
        """Test Other2RevenueReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Other2RevenueReference`
        """
        model = Other2RevenueReference()
        if include_optional:
            return Other2RevenueReference(
                info = {
                    'key' : ''
                    },
                cost = 1.337,
                id = 56,
                margin = 1.337,
                percentage = 1.337,
                revenue = 1.337
            )
        else:
            return Other2RevenueReference(
        )
        """

    def testOther2RevenueReference(self):
        """Test Other2RevenueReference"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
