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

from connectwise_psa.models.conversion import Conversion

class TestConversion(unittest.TestCase):
    """Conversion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Conversion:
        """Test Conversion
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Conversion`
        """
        model = Conversion()
        if include_optional:
            return Conversion(
                info = {
                    'key' : ''
                    },
                id = 56,
                parent_uom = connectwise_psa.models.unit_of_measure_reference.UnitOfMeasureReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                quantity = 1.337,
                uom_type = connectwise_psa.models.unit_of_measure_reference.UnitOfMeasureReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return Conversion(
        )
        """

    def testConversion(self):
        """Test Conversion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
