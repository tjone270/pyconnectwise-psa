# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.portal_security_settings_api import PortalSecuritySettingsApi


class TestPortalSecuritySettingsApi(unittest.TestCase):
    """PortalSecuritySettingsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PortalSecuritySettingsApi()

    def tearDown(self) -> None:
        pass

    def test_get_company_portal_security_settings(self) -> None:
        """Test case for get_company_portal_security_settings

        Get List of PortalSecuritySetting
        """
        pass

    def test_get_company_portal_security_settings_by_id(self) -> None:
        """Test case for get_company_portal_security_settings_by_id

        Get PortalSecuritySetting
        """
        pass

    def test_get_company_portal_security_settings_count(self) -> None:
        """Test case for get_company_portal_security_settings_count

        Get Count of PortalSecuritySetting
        """
        pass

    def test_patch_company_portal_security_settings_by_id(self) -> None:
        """Test case for patch_company_portal_security_settings_by_id

        Patch PortalSecuritySetting
        """
        pass

    def test_put_company_portal_security_settings_by_id(self) -> None:
        """Test case for put_company_portal_security_settings_by_id

        Put PortalSecuritySetting
        """
        pass


if __name__ == '__main__':
    unittest.main()
