# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.managed_device_accounts_api import ManagedDeviceAccountsApi


class TestManagedDeviceAccountsApi(unittest.TestCase):
    """ManagedDeviceAccountsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ManagedDeviceAccountsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_system_members_by_parent_id_managed_device_accounts_bulk(self) -> None:
        """Test case for delete_system_members_by_parent_id_managed_device_accounts_bulk

        Delete BulkResult
        """
        pass

    def test_get_system_members_by_parent_id_managed_device_accounts(self) -> None:
        """Test case for get_system_members_by_parent_id_managed_device_accounts

        Get List of ManagedDeviceAccount
        """
        pass

    def test_put_system_members_by_parent_id_managed_device_accounts_bulk(self) -> None:
        """Test case for put_system_members_by_parent_id_managed_device_accounts_bulk

        Put BulkResult
        """
        pass


if __name__ == '__main__':
    unittest.main()