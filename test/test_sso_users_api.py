# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.sso_users_api import SsoUsersApi


class TestSsoUsersApi(unittest.TestCase):
    """SsoUsersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SsoUsersApi()

    def tearDown(self) -> None:
        pass

    def test_get_system_sso_users(self) -> None:
        """Test case for get_system_sso_users

        Get List of SsoUser
        """
        pass

    def test_get_system_sso_users_by_external_id(self) -> None:
        """Test case for get_system_sso_users_by_external_id

        Get SsoUser
        """
        pass

    def test_get_system_sso_users_count(self) -> None:
        """Test case for get_system_sso_users_count

        Get Count of SsoUser
        """
        pass


if __name__ == '__main__':
    unittest.main()