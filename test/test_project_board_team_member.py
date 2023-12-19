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

from connectwise_psa.models.project_board_team_member import ProjectBoardTeamMember

class TestProjectBoardTeamMember(unittest.TestCase):
    """ProjectBoardTeamMember unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectBoardTeamMember:
        """Test ProjectBoardTeamMember
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectBoardTeamMember`
        """
        model = ProjectBoardTeamMember()
        if include_optional:
            return ProjectBoardTeamMember(
                info = {
                    'key' : ''
                    },
                id = 56,
                member = connectwise_psa.models.member_reference.MemberReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                project_role = connectwise_psa.models.project_role_reference.ProjectRoleReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', ),
                work_role = connectwise_psa.models.work_role_reference.WorkRoleReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return ProjectBoardTeamMember(
        )
        """

    def testProjectBoardTeamMember(self):
        """Test ProjectBoardTeamMember"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
