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

from connectwise_psa.models.agreement_type_work_role_exclusion import AgreementTypeWorkRoleExclusion

class TestAgreementTypeWorkRoleExclusion(unittest.TestCase):
    """AgreementTypeWorkRoleExclusion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgreementTypeWorkRoleExclusion:
        """Test AgreementTypeWorkRoleExclusion
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgreementTypeWorkRoleExclusion`
        """
        model = AgreementTypeWorkRoleExclusion()
        if include_optional:
            return AgreementTypeWorkRoleExclusion(
                info = {
                    'key' : ''
                    },
                id = 56,
                type = connectwise_psa.models.agreement_type_reference.AgreementTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                work_role = connectwise_psa.models.work_role_reference.WorkRoleReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return AgreementTypeWorkRoleExclusion(
        )
        """

    def testAgreementTypeWorkRoleExclusion(self):
        """Test AgreementTypeWorkRoleExclusion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
