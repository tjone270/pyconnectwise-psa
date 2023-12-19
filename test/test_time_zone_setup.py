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

from connectwise_psa.models.time_zone_setup import TimeZoneSetup

class TestTimeZoneSetup(unittest.TestCase):
    """TimeZoneSetup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeZoneSetup:
        """Test TimeZoneSetup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeZoneSetup`
        """
        model = TimeZoneSetup()
        if include_optional:
            return TimeZoneSetup(
                info = {
                    'key' : ''
                    },
                daylight_savings_flag = True,
                default_flag = True,
                id = 56,
                name = '',
                offset = 1.337,
                time_zone = connectwise_psa.models.time_zone_reference.TimeZoneReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return TimeZoneSetup(
                name = '',
        )
        """

    def testTimeZoneSetup(self):
        """Test TimeZoneSetup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()