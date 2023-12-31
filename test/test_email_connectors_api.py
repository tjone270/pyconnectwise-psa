# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.email_connectors_api import EmailConnectorsApi


class TestEmailConnectorsApi(unittest.TestCase):
    """EmailConnectorsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EmailConnectorsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_system_email_connectors_by_id(self) -> None:
        """Test case for delete_system_email_connectors_by_id

        Delete EmailConnector
        """
        pass

    def test_get_system_email_connectors(self) -> None:
        """Test case for get_system_email_connectors

        Get List of EmailConnector
        """
        pass

    def test_get_system_email_connectors_by_id(self) -> None:
        """Test case for get_system_email_connectors_by_id

        Get EmailConnector
        """
        pass

    def test_get_system_email_connectors_count(self) -> None:
        """Test case for get_system_email_connectors_count

        Get Count of EmailConnector
        """
        pass

    def test_patch_system_email_connectors_by_id(self) -> None:
        """Test case for patch_system_email_connectors_by_id

        Patch EmailConnector
        """
        pass

    def test_post_system_email_connectors(self) -> None:
        """Test case for post_system_email_connectors

        Post EmailConnector
        """
        pass

    def test_put_system_email_connectors_by_id(self) -> None:
        """Test case for put_system_email_connectors_by_id

        Put EmailConnector
        """
        pass


if __name__ == '__main__':
    unittest.main()
