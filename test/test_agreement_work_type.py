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

from connectwise_psa.models.agreement_work_type import AgreementWorkType

class TestAgreementWorkType(unittest.TestCase):
    """AgreementWorkType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgreementWorkType:
        """Test AgreementWorkType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgreementWorkType`
        """
        model = AgreementWorkType()
        if include_optional:
            return AgreementWorkType(
                info = {
                    'key' : ''
                    },
                agreement = connectwise_psa.models.agreement_reference.AgreementReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', 
                    type = '', ),
                agreement_id = 56,
                agreement_limit = 1.337,
                bill_time = 'Billable',
                company = connectwise_psa.models.company_reference.CompanyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                effective_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                ending_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                hours_max = 1.337,
                hours_min = 1.337,
                id = 56,
                location = connectwise_psa.models.owner_level_reference.OwnerLevelReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                location_id = 56,
                overage_rate = 1.337,
                overage_rate_type = 'AdjAmount',
                rate = 1.337,
                rate_type = 'AdjAmount',
                round_bill_hours = 1.337,
                site = connectwise_psa.models.site_reference.SiteReference(
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
            return AgreementWorkType(
                bill_time = 'Billable',
                rate_type = 'AdjAmount',
        )
        """

    def testAgreementWorkType(self):
        """Test AgreementWorkType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()