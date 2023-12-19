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

from connectwise_psa.models.managed_information import ManagedInformation

class TestManagedInformation(unittest.TestCase):
    """ManagedInformation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ManagedInformation:
        """Test ManagedInformation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ManagedInformation`
        """
        model = ManagedInformation()
        if include_optional:
            return ManagedInformation(
                child_configurations_matching_on = '',
                inactivate_configurations_matching_on = '',
                inactive_configuration_status_id = 56,
                level = '',
                managed_identifier = '',
                management_solution_name = '',
                type = ''
            )
        else:
            return ManagedInformation(
        )
        """

    def testManagedInformation(self):
        """Test ManagedInformation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
