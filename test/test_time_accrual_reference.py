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

from connectwise_psa.models.time_accrual_reference import TimeAccrualReference

class TestTimeAccrualReference(unittest.TestCase):
    """TimeAccrualReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeAccrualReference:
        """Test TimeAccrualReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeAccrualReference`
        """
        model = TimeAccrualReference()
        if include_optional:
            return TimeAccrualReference(
                info = {
                    'key' : ''
                    },
                id = 56,
                name = ''
            )
        else:
            return TimeAccrualReference(
        )
        """

    def testTimeAccrualReference(self):
        """Test TimeAccrualReference"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
