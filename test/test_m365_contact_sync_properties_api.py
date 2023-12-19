# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.m365_contact_sync_properties_api import M365ContactSyncPropertiesApi


class TestM365ContactSyncPropertiesApi(unittest.TestCase):
    """M365ContactSyncPropertiesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = M365ContactSyncPropertiesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_company_m365contactsync_property(self) -> None:
        """Test case for delete_company_m365contactsync_property

        Delete M365ContactSyncProperty
        """
        pass

    def test_get_company_m365contactsync_by_id_property(self) -> None:
        """Test case for get_company_m365contactsync_by_id_property

        Get M365ContactSyncProperties
        """
        pass

    def test_get_company_m365contactsync_property_count(self) -> None:
        """Test case for get_company_m365contactsync_property_count

        Get Count of M365ContactSyncProperty
        """
        pass

    def test_get_company_m365contactsync_property_excluded(self) -> None:
        """Test case for get_company_m365contactsync_property_excluded

        Get List of M365ContactSyncPropertiesExcluded
        """
        pass

    def test_get_company_m365contactsync_property_included(self) -> None:
        """Test case for get_company_m365contactsync_property_included

        Get List of M365ContactSyncPropertiesIncluded
        """
        pass

    def test_post_company_m365contactsync_property(self) -> None:
        """Test case for post_company_m365contactsync_property

        Create M365ContactSyncProperty
        """
        pass


if __name__ == '__main__':
    unittest.main()
