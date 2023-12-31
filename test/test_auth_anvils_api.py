# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.auth_anvils_api import AuthAnvilsApi


class TestAuthAnvilsApi(unittest.TestCase):
    """AuthAnvilsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthAnvilsApi()

    def tearDown(self) -> None:
        pass

    def test_get_system_auth_anvils(self) -> None:
        """Test case for get_system_auth_anvils

        Get List of ConnectWise.Apis.v3_0.v2015_3.System.AuthAnvil.AuthAnvil
        """
        pass

    def test_get_system_auth_anvils_by_id(self) -> None:
        """Test case for get_system_auth_anvils_by_id

        Get ConnectWise.Apis.v3_0.v2015_3.System.AuthAnvil.AuthAnvil
        """
        pass

    def test_get_system_auth_anvils_count(self) -> None:
        """Test case for get_system_auth_anvils_count

        Get Count of SuccessResponse
        """
        pass

    def test_get_system_auth_anvils_test_connection(self) -> None:
        """Test case for get_system_auth_anvils_test_connection

        Get SuccessResponse
        """
        pass

    def test_patch_system_auth_anvils_by_id(self) -> None:
        """Test case for patch_system_auth_anvils_by_id

        Patch ConnectWise.Apis.v3_0.v2015_3.System.AuthAnvil.AuthAnvil
        """
        pass

    def test_put_system_auth_anvils_by_id(self) -> None:
        """Test case for put_system_auth_anvils_by_id

        Put ConnectWise.Apis.v3_0.v2015_3.System.AuthAnvil.AuthAnvil
        """
        pass


if __name__ == '__main__':
    unittest.main()
