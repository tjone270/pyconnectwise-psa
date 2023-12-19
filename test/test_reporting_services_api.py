# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.reporting_services_api import ReportingServicesApi


class TestReportingServicesApi(unittest.TestCase):
    """ReportingServicesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ReportingServicesApi()

    def tearDown(self) -> None:
        pass

    def test_get_system_mycompany_reporting_services(self) -> None:
        """Test case for get_system_mycompany_reporting_services

        Get List of ReportingService
        """
        pass

    def test_get_system_mycompany_reporting_services_by_id(self) -> None:
        """Test case for get_system_mycompany_reporting_services_by_id

        Get ReportingService
        """
        pass

    def test_patch_system_mycompany_reporting_services_by_id(self) -> None:
        """Test case for patch_system_mycompany_reporting_services_by_id

        Patch ReportingService
        """
        pass

    def test_post_system_mycompany_reporting_services_by_id_test_connection(self) -> None:
        """Test case for post_system_mycompany_reporting_services_by_id_test_connection

        Post SuccessResponse
        """
        pass

    def test_put_system_mycompany_reporting_services_by_id(self) -> None:
        """Test case for put_system_mycompany_reporting_services_by_id

        Put ReportingService
        """
        pass


if __name__ == '__main__':
    unittest.main()