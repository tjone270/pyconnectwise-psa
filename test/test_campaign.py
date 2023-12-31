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

from connectwise_psa.models.campaign import Campaign

class TestCampaign(unittest.TestCase):
    """Campaign unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Campaign:
        """Test Campaign
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Campaign`
        """
        model = Campaign()
        if include_optional:
            return Campaign(
                info = {
                    'key' : ''
                    },
                actual_cost = 1.337,
                actual_gross_margin = 1.337,
                actual_roi = 1.337,
                actual_revenue = 1.337,
                budget_cost = 1.337,
                budget_gross_margin = 1.337,
                budget_roi = 1.337,
                budget_revenue = 1.337,
                default_group = connectwise_psa.models.group_reference.GroupReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                emails_sent = 56,
                end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = 56,
                impressions = 56,
                inactive = True,
                inactive_days_after_end = 56,
                location_id = 56,
                marketing_manager_default_track_id = 56,
                member = connectwise_psa.models.member_reference.MemberReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                name = '',
                notes = '',
                opportunity_default_track_id = 56,
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                status = connectwise_psa.models.campaign_status_reference.CampaignStatusReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                sub_type = connectwise_psa.models.campaign_sub_type_reference.CampaignSubTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                type = connectwise_psa.models.campaign_type_reference.CampaignTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return Campaign(
                name = '',
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testCampaign(self):
        """Test Campaign"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
