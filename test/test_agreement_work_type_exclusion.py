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

from connectwise_psa.models.agreement_work_type_exclusion import AgreementWorkTypeExclusion

class TestAgreementWorkTypeExclusion(unittest.TestCase):
    """AgreementWorkTypeExclusion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgreementWorkTypeExclusion:
        """Test AgreementWorkTypeExclusion
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgreementWorkTypeExclusion`
        """
        model = AgreementWorkTypeExclusion()
        if include_optional:
            return AgreementWorkTypeExclusion(
                info = {
                    'key' : ''
                    },
                agreement_id = 56,
                id = 56,
                work_type = connectwise_psa.models.work_type_reference.WorkTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return AgreementWorkTypeExclusion(
        )
        """

    def testAgreementWorkTypeExclusion(self):
        """Test AgreementWorkTypeExclusion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
