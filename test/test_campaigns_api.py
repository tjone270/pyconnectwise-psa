# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.campaigns_api import CampaignsApi


class TestCampaignsApi(unittest.TestCase):
    """CampaignsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CampaignsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_marketing_campaigns_by_id(self) -> None:
        """Test case for delete_marketing_campaigns_by_id

        Delete Campaign
        """
        pass

    def test_get_marketing_campaigns(self) -> None:
        """Test case for get_marketing_campaigns

        Get List of Campaign
        """
        pass

    def test_get_marketing_campaigns_by_id(self) -> None:
        """Test case for get_marketing_campaigns_by_id

        Get Campaign
        """
        pass

    def test_get_marketing_campaigns_by_id_activities(self) -> None:
        """Test case for get_marketing_campaigns_by_id_activities

        Get List of ActivityReference
        """
        pass

    def test_get_marketing_campaigns_by_id_activities_count(self) -> None:
        """Test case for get_marketing_campaigns_by_id_activities_count

        Get Count of ActivityReference
        """
        pass

    def test_get_marketing_campaigns_by_id_opportunities(self) -> None:
        """Test case for get_marketing_campaigns_by_id_opportunities

        Get List of OpportunityReference
        """
        pass

    def test_get_marketing_campaigns_by_id_opportunities_count(self) -> None:
        """Test case for get_marketing_campaigns_by_id_opportunities_count

        Get Count of OpportunityReference
        """
        pass

    def test_get_marketing_campaigns_count(self) -> None:
        """Test case for get_marketing_campaigns_count

        Get Count of Campaign
        """
        pass

    def test_patch_marketing_campaigns_by_id(self) -> None:
        """Test case for patch_marketing_campaigns_by_id

        Patch Campaign
        """
        pass

    def test_post_marketing_campaigns(self) -> None:
        """Test case for post_marketing_campaigns

        Post Campaign
        """
        pass

    def test_put_marketing_campaigns_by_id(self) -> None:
        """Test case for put_marketing_campaigns_by_id

        Put Campaign
        """
        pass


if __name__ == '__main__':
    unittest.main()