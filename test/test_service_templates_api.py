# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.service_templates_api import ServiceTemplatesApi


class TestServiceTemplatesApi(unittest.TestCase):
    """ServiceTemplatesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ServiceTemplatesApi()

    def tearDown(self) -> None:
        pass

    def test_get_service_templates(self) -> None:
        """Test case for get_service_templates

        Get List of ServiceTemplate
        """
        pass

    def test_get_service_templates_by_id(self) -> None:
        """Test case for get_service_templates_by_id

        Get ServiceTemplate
        """
        pass

    def test_get_service_templates_count(self) -> None:
        """Test case for get_service_templates_count

        Get Count of ServiceTemplate
        """
        pass

    def test_post_service_templates_by_id_generate(self) -> None:
        """Test case for post_service_templates_by_id_generate

        Post Count of ServiceTemplate
        """
        pass


if __name__ == '__main__':
    unittest.main()
