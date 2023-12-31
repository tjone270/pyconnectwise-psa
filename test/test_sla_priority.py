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

from connectwise_psa.models.sla_priority import SLAPriority

class TestSLAPriority(unittest.TestCase):
    """SLAPriority unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SLAPriority:
        """Test SLAPriority
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SLAPriority`
        """
        model = SLAPriority()
        if include_optional:
            return SLAPriority(
                info = {
                    'key' : ''
                    },
                id = 56,
                plan_within = 1.337,
                plan_within_percent = 56,
                priority = connectwise_psa.models.priority_reference.PriorityReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    level = '', 
                    name = '', 
                    sort = 56, ),
                resolution_hours = 1.337,
                resolution_percent = 56,
                respond_hours = 1.337,
                respond_percent = 56,
                sla = connectwise_psa.models.sla_reference.SLAReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return SLAPriority(
        )
        """

    def testSLAPriority(self):
        """Test SLAPriority"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
