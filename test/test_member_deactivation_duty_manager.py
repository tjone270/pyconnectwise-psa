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

from connectwise_psa.models.member_deactivation_duty_manager import MemberDeactivationDutyManager

class TestMemberDeactivationDutyManager(unittest.TestCase):
    """MemberDeactivationDutyManager unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MemberDeactivationDutyManager:
        """Test MemberDeactivationDutyManager
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MemberDeactivationDutyManager`
        """
        model = MemberDeactivationDutyManager()
        if include_optional:
            return MemberDeactivationDutyManager(
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
            return MemberDeactivationDutyManager(
        )
        """

    def testMemberDeactivationDutyManager(self):
        """Test MemberDeactivationDutyManager"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
