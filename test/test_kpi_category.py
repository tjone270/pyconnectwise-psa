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

from connectwise_psa.models.kpi_category import KPICategory

class TestKPICategory(unittest.TestCase):
    """KPICategory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KPICategory:
        """Test KPICategory
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KPICategory`
        """
        model = KPICategory()
        if include_optional:
            return KPICategory(
                id = 56,
                name = '',
                sort_order = 56
            )
        else:
            return KPICategory(
        )
        """

    def testKPICategory(self):
        """Test KPICategory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
