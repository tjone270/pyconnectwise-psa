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

from connectwise_psa.models.campaign_sub_type_campaign_sub_type import CampaignSubTypeCampaignSubType

class TestCampaignSubTypeCampaignSubType(unittest.TestCase):
    """CampaignSubTypeCampaignSubType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CampaignSubTypeCampaignSubType:
        """Test CampaignSubTypeCampaignSubType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CampaignSubTypeCampaignSubType`
        """
        model = CampaignSubTypeCampaignSubType()
        if include_optional:
            return CampaignSubTypeCampaignSubType(
                info = {
                    'key' : ''
                    },
                id = 56,
                name = '',
                type = connectwise_psa.models.campaign_type_reference.CampaignTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return CampaignSubTypeCampaignSubType(
                name = '',
        )
        """

    def testCampaignSubTypeCampaignSubType(self):
        """Test CampaignSubTypeCampaignSubType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
