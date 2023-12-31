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

from connectwise_psa.models.callback_entry import CallbackEntry

class TestCallbackEntry(unittest.TestCase):
    """CallbackEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CallbackEntry:
        """Test CallbackEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CallbackEntry`
        """
        model = CallbackEntry()
        if include_optional:
            return CallbackEntry(
                info = {
                    'key' : ''
                    },
                description = '',
                id = 56,
                inactive_flag = True,
                is_self_suppressed_flag = True,
                is_soap_callback_flag = True,
                level = '',
                member_id = 56,
                object_id = 56,
                payload_version = '',
                type = '',
                url = ''
            )
        else:
            return CallbackEntry(
        )
        """

    def testCallbackEntry(self):
        """Test CallbackEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
