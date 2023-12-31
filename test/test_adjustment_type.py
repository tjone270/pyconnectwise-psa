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

from connectwise_psa.models.adjustment_type import AdjustmentType

class TestAdjustmentType(unittest.TestCase):
    """AdjustmentType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdjustmentType:
        """Test AdjustmentType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdjustmentType`
        """
        model = AdjustmentType()
        if include_optional:
            return AdjustmentType(
                info = {
                    'key' : ''
                    },
                audit_trail_flag = True,
                created_by = '',
                date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = 56,
                identifier = '',
                name = ''
            )
        else:
            return AdjustmentType(
                identifier = '',
        )
        """

    def testAdjustmentType(self):
        """Test AdjustmentType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
