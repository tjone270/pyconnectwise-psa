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

from connectwise_psa.models.project_status import ProjectStatus

class TestProjectStatus(unittest.TestCase):
    """ProjectStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectStatus:
        """Test ProjectStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectStatus`
        """
        model = ProjectStatus()
        if include_optional:
            return ProjectStatus(
                info = {
                    'key' : ''
                    },
                closed_flag = True,
                custom_status_indicator_name = '',
                default_flag = True,
                id = 56,
                inactive_flag = True,
                name = '',
                no_time_flag = True,
                status_indicator = connectwise_psa.models.status_indicator_reference.StatusIndicatorReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', )
            )
        else:
            return ProjectStatus(
                name = '',
        )
        """

    def testProjectStatus(self):
        """Test ProjectStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
