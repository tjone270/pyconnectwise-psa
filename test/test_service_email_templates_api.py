# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.service_email_templates_api import ServiceEmailTemplatesApi


class TestServiceEmailTemplatesApi(unittest.TestCase):
    """ServiceEmailTemplatesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ServiceEmailTemplatesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_service_email_templates_by_id(self) -> None:
        """Test case for delete_service_email_templates_by_id

        Delete ServiceEmailTemplate
        """
        pass

    def test_get_service_email_templates(self) -> None:
        """Test case for get_service_email_templates

        Get List of ServiceEmailTemplate
        """
        pass

    def test_get_service_email_templates_by_id(self) -> None:
        """Test case for get_service_email_templates_by_id

        Get ServiceEmailTemplate
        """
        pass

    def test_get_service_email_templates_by_id_usages(self) -> None:
        """Test case for get_service_email_templates_by_id_usages

        Get List of Usage Count
        """
        pass

    def test_get_service_email_templates_by_id_usages_list(self) -> None:
        """Test case for get_service_email_templates_by_id_usages_list

        Get List of Usage
        """
        pass

    def test_get_service_email_templates_count(self) -> None:
        """Test case for get_service_email_templates_count

        Get Count of ServiceEmailTemplate
        """
        pass

    def test_patch_service_email_templates_by_id(self) -> None:
        """Test case for patch_service_email_templates_by_id

        Patch ServiceEmailTemplate
        """
        pass

    def test_post_service_email_templates(self) -> None:
        """Test case for post_service_email_templates

        Post ServiceEmailTemplate
        """
        pass

    def test_put_service_email_templates_by_id(self) -> None:
        """Test case for put_service_email_templates_by_id

        Put ServiceEmailTemplate
        """
        pass


if __name__ == '__main__':
    unittest.main()
