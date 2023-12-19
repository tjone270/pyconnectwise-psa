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

from connectwise_psa.models.convert_to_project import ConvertToProject

class TestConvertToProject(unittest.TestCase):
    """ConvertToProject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConvertToProject:
        """Test ConvertToProject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConvertToProject`
        """
        model = ConvertToProject()
        if include_optional:
            return ConvertToProject(
                id = 56,
                phase = connectwise_psa.models.project_phase_reference.ProjectPhaseReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                project = connectwise_psa.models.project_reference.ProjectReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                record_type = 'ProjectIssue',
                wbs_code = ''
            )
        else:
            return ConvertToProject(
                wbs_code = '',
        )
        """

    def testConvertToProject(self):
        """Test ConvertToProject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()