# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.imap_infos_api import ImapInfosApi


class TestImapInfosApi(unittest.TestCase):
    """ImapInfosApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ImapInfosApi()

    def tearDown(self) -> None:
        pass

    def test_get_system_imaps_by_id_info(self) -> None:
        """Test case for get_system_imaps_by_id_info

        Get ImapInfo
        """
        pass

    def test_get_system_imaps_info(self) -> None:
        """Test case for get_system_imaps_info

        Get List of ImapInfos
        """
        pass

    def test_get_system_imaps_info_count(self) -> None:
        """Test case for get_system_imaps_info_count

        Get Count of ImapInfos
        """
        pass


if __name__ == '__main__':
    unittest.main()