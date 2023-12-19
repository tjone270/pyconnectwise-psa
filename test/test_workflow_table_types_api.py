# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.workflow_table_types_api import WorkflowTableTypesApi


class TestWorkflowTableTypesApi(unittest.TestCase):
    """WorkflowTableTypesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = WorkflowTableTypesApi()

    def tearDown(self) -> None:
        pass

    def test_get_system_workflows_table_types(self) -> None:
        """Test case for get_system_workflows_table_types

        Get List of WorkflowTableType
        """
        pass

    def test_get_system_workflows_table_types_by_id(self) -> None:
        """Test case for get_system_workflows_table_types_by_id

        Get WorkflowTableType
        """
        pass

    def test_get_system_workflows_table_types_by_id_info(self) -> None:
        """Test case for get_system_workflows_table_types_by_id_info

        Get WorkflowTableTypeInfo
        """
        pass

    def test_get_system_workflows_table_types_count(self) -> None:
        """Test case for get_system_workflows_table_types_count

        Get Count of WorkflowTableType
        """
        pass

    def test_get_system_workflows_table_types_info(self) -> None:
        """Test case for get_system_workflows_table_types_info

        Get List of WorkflowTableTypeInfo
        """
        pass

    def test_get_system_workflows_table_types_info_count(self) -> None:
        """Test case for get_system_workflows_table_types_info_count

        Get Count of WorkflowTableTypeInfo
        """
        pass


if __name__ == '__main__':
    unittest.main()