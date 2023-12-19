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

from connectwise_psa.models.member_deactivation_sales_activity import MemberDeactivationSalesActivity

class TestMemberDeactivationSalesActivity(unittest.TestCase):
    """MemberDeactivationSalesActivity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MemberDeactivationSalesActivity:
        """Test MemberDeactivationSalesActivity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MemberDeactivationSalesActivity`
        """
        model = MemberDeactivationSalesActivity()
        if include_optional:
            return MemberDeactivationSalesActivity(
                count = 56,
                re_assign_to_member = connectwise_psa.models.member_reference.MemberReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', )
            )
        else:
            return MemberDeactivationSalesActivity(
        )
        """

    def testMemberDeactivationSalesActivity(self):
        """Test MemberDeactivationSalesActivity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
