# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.m365_contact_syncs_api import M365ContactSyncsApi


class TestM365ContactSyncsApi(unittest.TestCase):
    """M365ContactSyncsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = M365ContactSyncsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_system_m365contactsync_by_id(self) -> None:
        """Test case for delete_system_m365contactsync_by_id

        Delete M365ContactSync
        """
        pass

    def test_get_system_m365contactsync_authorize(self) -> None:
        """Test case for get_system_m365contactsync_authorize

        Initiate Application ConsentAsync
        """
        pass

    def test_get_system_m365contactsync_by_id(self) -> None:
        """Test case for get_system_m365contactsync_by_id

        Get ContactSync By Id
        """
        pass

    def test_get_system_m365contactsync_by_id_test(self) -> None:
        """Test case for get_system_m365contactsync_by_id_test

        Test Consent Async
        """
        pass

    def test_get_system_m365contactsync_by_id_viewauth(self) -> None:
        """Test case for get_system_m365contactsync_by_id_viewauth

        Get AuthInfo Async
        """
        pass

    def test_patch_system_m365contactsync_by_id(self) -> None:
        """Test case for patch_system_m365contactsync_by_id

        Update ContactSync Async
        """
        pass

    def test_post_system_m365contactsync(self) -> None:
        """Test case for post_system_m365contactsync

        Create Async
        """
        pass


if __name__ == '__main__':
    unittest.main()
