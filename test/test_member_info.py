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

from connectwise_psa.models.member_info import MemberInfo

class TestMemberInfo(unittest.TestCase):
    """MemberInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MemberInfo:
        """Test MemberInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MemberInfo`
        """
        model = MemberInfo()
        if include_optional:
            return MemberInfo(
                info = {
                    'key' : ''
                    },
                default_email = '',
                first_name = '',
                full_name = '',
                id = 56,
                identifier = '',
                inactive_flag = True,
                last_name = '',
                license_class = 'A',
                middle_initial = '',
                photo = connectwise_psa.models.document_reference.DocumentReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return MemberInfo(
        )
        """

    def testMemberInfo(self):
        """Test MemberInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
