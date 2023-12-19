# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.contacts_api import ContactsApi


class TestContactsApi(unittest.TestCase):
    """ContactsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ContactsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_company_contacts_by_id(self) -> None:
        """Test case for delete_company_contacts_by_id

        Delete ApiContact
        """
        pass

    def test_get_company_contacts(self) -> None:
        """Test case for get_company_contacts

        Get List of ApiContact
        """
        pass

    def test_get_company_contacts_by_id(self) -> None:
        """Test case for get_company_contacts_by_id

        Get ApiContact
        """
        pass

    def test_get_company_contacts_by_id_image(self) -> None:
        """Test case for get_company_contacts_by_id_image

        Get ValidatePortalResponse
        """
        pass

    def test_get_company_contacts_by_id_portal_security(self) -> None:
        """Test case for get_company_contacts_by_id_portal_security

        Get List of PortalSecurity
        """
        pass

    def test_get_company_contacts_by_id_usages(self) -> None:
        """Test case for get_company_contacts_by_id_usages

        Get List of Usage Count
        """
        pass

    def test_get_company_contacts_by_id_usages_list(self) -> None:
        """Test case for get_company_contacts_by_id_usages_list

        Get List of Usage
        """
        pass

    def test_get_company_contacts_count(self) -> None:
        """Test case for get_company_contacts_count

        Get Count of Usage
        """
        pass

    def test_get_company_contacts_default(self) -> None:
        """Test case for get_company_contacts_default

        Get ApiContact
        """
        pass

    def test_patch_company_contacts_by_id(self) -> None:
        """Test case for patch_company_contacts_by_id

        Patch ApiContact
        """
        pass

    def test_post_company_contacts(self) -> None:
        """Test case for post_company_contacts

        Post ApiContact
        """
        pass

    def test_post_company_contacts_request_password(self) -> None:
        """Test case for post_company_contacts_request_password

        Post PortalSecurity
        """
        pass

    def test_post_company_contacts_validate_portal_credentials(self) -> None:
        """Test case for post_company_contacts_validate_portal_credentials

        Post ValidatePortalResponse
        """
        pass

    def test_put_company_contacts_by_id(self) -> None:
        """Test case for put_company_contacts_by_id

        Put ApiContact
        """
        pass


if __name__ == '__main__':
    unittest.main()