# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.security_role_infos_api import SecurityRoleInfosApi


class TestSecurityRoleInfosApi(unittest.TestCase):
    """SecurityRoleInfosApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SecurityRoleInfosApi()

    def tearDown(self) -> None:
        pass

    def test_get_system_securityroles_by_id_info(self) -> None:
        """Test case for get_system_securityroles_by_id_info

        Get SecurityRoleInfo
        """
        pass

    def test_get_system_securityroles_info(self) -> None:
        """Test case for get_system_securityroles_info

        Get List of SecurityRoleInfo
        """
        pass

    def test_get_system_securityroles_info_count(self) -> None:
        """Test case for get_system_securityroles_info_count

        Get Count of SecurityRoleInfo
        """
        pass


if __name__ == '__main__':
    unittest.main()
