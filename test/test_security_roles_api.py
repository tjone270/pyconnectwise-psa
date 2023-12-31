# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.security_roles_api import SecurityRolesApi


class TestSecurityRolesApi(unittest.TestCase):
    """SecurityRolesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SecurityRolesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_system_securityroles_by_id(self) -> None:
        """Test case for delete_system_securityroles_by_id

        Delete SecurityRole
        """
        pass

    def test_get_system_securityroles(self) -> None:
        """Test case for get_system_securityroles

        Get List of SecurityRole
        """
        pass

    def test_get_system_securityroles_by_id(self) -> None:
        """Test case for get_system_securityroles_by_id

        Get SecurityRole
        """
        pass

    def test_get_system_securityroles_count(self) -> None:
        """Test case for get_system_securityroles_count

        Get Count of SecurityRole
        """
        pass

    def test_post_system_securityroles(self) -> None:
        """Test case for post_system_securityroles

        Post SecurityRole
        """
        pass


if __name__ == '__main__':
    unittest.main()
