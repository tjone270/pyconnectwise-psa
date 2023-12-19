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

from connectwise_psa.models.billing_term import BillingTerm

class TestBillingTerm(unittest.TestCase):
    """BillingTerm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillingTerm:
        """Test BillingTerm
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillingTerm`
        """
        model = BillingTerm()
        if include_optional:
            return BillingTerm(
                info = {
                    'key' : ''
                    },
                default_flag = True,
                due_days = 56,
                id = 56,
                name = '',
                terms_xref = ''
            )
        else:
            return BillingTerm(
                due_days = 56,
                name = '',
        )
        """

    def testBillingTerm(self):
        """Test BillingTerm"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
