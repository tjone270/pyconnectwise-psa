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

from connectwise_psa.models.activity_type_reference import ActivityTypeReference

class TestActivityTypeReference(unittest.TestCase):
    """ActivityTypeReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActivityTypeReference:
        """Test ActivityTypeReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActivityTypeReference`
        """
        model = ActivityTypeReference()
        if include_optional:
            return ActivityTypeReference(
                info = {
                    'key' : ''
                    },
                id = 56,
                name = ''
            )
        else:
            return ActivityTypeReference(
        )
        """

    def testActivityTypeReference(self):
        """Test ActivityTypeReference"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
