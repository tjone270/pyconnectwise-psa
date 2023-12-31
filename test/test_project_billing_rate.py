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

from connectwise_psa.models.project_billing_rate import ProjectBillingRate

class TestProjectBillingRate(unittest.TestCase):
    """ProjectBillingRate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectBillingRate:
        """Test ProjectBillingRate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectBillingRate`
        """
        model = ProjectBillingRate()
        if include_optional:
            return ProjectBillingRate(
                info = {
                    'key' : ''
                    },
                activity_class_rec_id = 56,
                hourly_rate = 1.337,
                id = 56,
                member = connectwise_psa.models.member_reference.MemberReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                member_rec_id = 56,
                project_rec_id = 56,
                work_role = connectwise_psa.models.work_role_reference.WorkRoleReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return ProjectBillingRate(
        )
        """

    def testProjectBillingRate(self):
        """Test ProjectBillingRate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
