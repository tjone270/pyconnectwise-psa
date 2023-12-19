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

from connectwise_psa.models.pricing_break import PricingBreak

class TestPricingBreak(unittest.TestCase):
    """PricingBreak unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PricingBreak:
        """Test PricingBreak
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PricingBreak`
        """
        model = PricingBreak()
        if include_optional:
            return PricingBreak(
                info = {
                    'key' : ''
                    },
                amount = 1.337,
                detail_id = 56,
                id = 56,
                price_method = 'FlatRateForRange',
                quantity_end = 1.337,
                quantity_start = 1.337,
                unlimited = True
            )
        else:
            return PricingBreak(
                price_method = 'FlatRateForRange',
                quantity_start = 1.337,
        )
        """

    def testPricingBreak(self):
        """Test PricingBreak"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()