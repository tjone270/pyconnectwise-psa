# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.slas_api import SLAsApi


class TestSLAsApi(unittest.TestCase):
    """SLAsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SLAsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_service_slas_by_id(self) -> None:
        """Test case for delete_service_slas_by_id

        Delete SLA
        """
        pass

    def test_get_service_slas(self) -> None:
        """Test case for get_service_slas

        Get List of SLA
        """
        pass

    def test_get_service_slas_by_id(self) -> None:
        """Test case for get_service_slas_by_id

        Get SLA
        """
        pass

    def test_get_service_slas_by_id_usages(self) -> None:
        """Test case for get_service_slas_by_id_usages

        Get List of Usage
        """
        pass

    def test_get_service_slas_by_id_usages_list(self) -> None:
        """Test case for get_service_slas_by_id_usages_list

        Get List of Usage
        """
        pass

    def test_get_service_slas_count(self) -> None:
        """Test case for get_service_slas_count

        Get Count of SLA
        """
        pass

    def test_patch_service_slas_by_id(self) -> None:
        """Test case for patch_service_slas_by_id

        Patch SLA
        """
        pass

    def test_post_service_slas(self) -> None:
        """Test case for post_service_slas

        Post SLA
        """
        pass

    def test_put_service_slas_by_id(self) -> None:
        """Test case for put_service_slas_by_id

        Put SLA
        """
        pass


if __name__ == '__main__':
    unittest.main()