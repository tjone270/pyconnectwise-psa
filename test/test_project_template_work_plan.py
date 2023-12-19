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

from connectwise_psa.models.project_template_work_plan import ProjectTemplateWorkPlan

class TestProjectTemplateWorkPlan(unittest.TestCase):
    """ProjectTemplateWorkPlan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectTemplateWorkPlan:
        """Test ProjectTemplateWorkPlan
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectTemplateWorkPlan`
        """
        model = ProjectTemplateWorkPlan()
        if include_optional:
            return ProjectTemplateWorkPlan(
                budget_amount = 1.337,
                description = '',
                display_id = '',
                i_d = 56,
                is_new_item = True,
                is_phase = True,
                is_project = True,
                is_ticket = True,
                parent_phase_rec_id = 56,
                project_name = '',
                rec_id = 56,
                s_r_service_rec_id = 56,
                tree_id = '',
                wbs_code = ''
            )
        else:
            return ProjectTemplateWorkPlan(
        )
        """

    def testProjectTemplateWorkPlan(self):
        """Test ProjectTemplateWorkPlan"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
