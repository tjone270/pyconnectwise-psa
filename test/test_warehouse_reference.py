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

from connectwise_psa.models.warehouse_reference import WarehouseReference

class TestWarehouseReference(unittest.TestCase):
    """WarehouseReference unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WarehouseReference:
        """Test WarehouseReference
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WarehouseReference`
        """
        model = WarehouseReference()
        if include_optional:
            return WarehouseReference(
                info = {
                    'key' : ''
                    },
                id = 56,
                locked_flag = True,
                name = ''
            )
        else:
            return WarehouseReference(
        )
        """

    def testWarehouseReference(self):
        """Test WarehouseReference"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
