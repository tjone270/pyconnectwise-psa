# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.email_tokens_api import EmailTokensApi


class TestEmailTokensApi(unittest.TestCase):
    """EmailTokensApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EmailTokensApi()

    def tearDown(self) -> None:
        pass

    def test_get_system_email_tokens(self) -> None:
        """Test case for get_system_email_tokens

        Get List of EmailToken
        """
        pass

    def test_get_system_email_tokens_by_id(self) -> None:
        """Test case for get_system_email_tokens_by_id

        Get EmailToken
        """
        pass

    def test_get_system_email_tokens_count(self) -> None:
        """Test case for get_system_email_tokens_count

        Get Count of EmailToken
        """
        pass


if __name__ == '__main__':
    unittest.main()
