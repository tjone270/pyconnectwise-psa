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

from connectwise_psa.models.on_hand_serial_number import OnHandSerialNumber

class TestOnHandSerialNumber(unittest.TestCase):
    """OnHandSerialNumber unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OnHandSerialNumber:
        """Test OnHandSerialNumber
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OnHandSerialNumber`
        """
        model = OnHandSerialNumber()
        if include_optional:
            return OnHandSerialNumber(
                info = {
                    'key' : ''
                    },
                catalog_item = connectwise_psa.models.catalog_item_reference.CatalogItemReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                id = 56,
                serial = '',
                warehouse = connectwise_psa.models.warehouse_reference.WarehouseReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    locked_flag = True, 
                    name = '', ),
                warehouse_bin = connectwise_psa.models.warehouse_bin_reference.WarehouseBinReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return OnHandSerialNumber(
        )
        """

    def testOnHandSerialNumber(self):
        """Test OnHandSerialNumber"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
