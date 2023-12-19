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

from connectwise_psa.models.time_sheet import TimeSheet

class TestTimeSheet(unittest.TestCase):
    """TimeSheet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeSheet:
        """Test TimeSheet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeSheet`
        """
        model = TimeSheet()
        if include_optional:
            return TimeSheet(
                info = {
                    'key' : ''
                    },
                date_end = '',
                date_start = '',
                deadline = '',
                hours = 1.337,
                id = 56,
                member = connectwise_psa.models.member_reference.MemberReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                period = 56,
                status = 'Open',
                year = 56
            )
        else:
            return TimeSheet(
        )
        """

    def testTimeSheet(self):
        """Test TimeSheet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()