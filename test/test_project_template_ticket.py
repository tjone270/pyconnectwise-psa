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

from connectwise_psa.models.project_template_ticket import ProjectTemplateTicket

class TestProjectTemplateTicket(unittest.TestCase):
    """ProjectTemplateTicket unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectTemplateTicket:
        """Test ProjectTemplateTicket
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectTemplateTicket`
        """
        model = ProjectTemplateTicket()
        if include_optional:
            return ProjectTemplateTicket(
                info = {
                    'key' : ''
                    },
                bill_separately_flag = True,
                budget_hours = 1.337,
                description = '',
                duration = 56,
                id = 56,
                internal_analysis = '',
                line_number = 1.337,
                mark_as_milestone_flag = True,
                notes = '',
                pm_tmp_project_rec_id = 56,
                priority = connectwise_psa.models.priority_reference.PriorityReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    level = '', 
                    name = '', 
                    sort = 56, ),
                project_template_id = 56,
                project_template_phase_id = 56,
                record_type = '',
                resolution = '',
                source = connectwise_psa.models.service_source_reference.ServiceSourceReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                wbs_code = '',
                work_role = connectwise_psa.models.work_role_reference.WorkRoleReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                work_type = connectwise_psa.models.work_type_reference.WorkTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return ProjectTemplateTicket(
                description = '',
        )
        """

    def testProjectTemplateTicket(self):
        """Test ProjectTemplateTicket"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
