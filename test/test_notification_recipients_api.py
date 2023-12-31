# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.notification_recipients_api import NotificationRecipientsApi


class TestNotificationRecipientsApi(unittest.TestCase):
    """NotificationRecipientsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NotificationRecipientsApi()

    def tearDown(self) -> None:
        pass

    def test_get_system_notification_recipients(self) -> None:
        """Test case for get_system_notification_recipients

        Get List of NotificationRecipient
        """
        pass

    def test_get_system_notification_recipients_by_id(self) -> None:
        """Test case for get_system_notification_recipients_by_id

        Get NotificationRecipient
        """
        pass

    def test_get_system_notification_recipients_count(self) -> None:
        """Test case for get_system_notification_recipients_count

        Get Count of NotificationRecipient
        """
        pass


if __name__ == '__main__':
    unittest.main()
