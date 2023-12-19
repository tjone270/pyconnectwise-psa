# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.project_tickets_api import ProjectTicketsApi


class TestProjectTicketsApi(unittest.TestCase):
    """ProjectTicketsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectTicketsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_project_tickets_by_id(self) -> None:
        """Test case for delete_project_tickets_by_id

        Delete ProjectTicket
        """
        pass

    def test_delete_project_tickets_by_parent_id_configurations_by_id(self) -> None:
        """Test case for delete_project_tickets_by_parent_id_configurations_by_id

        Delete ConfigurationReference
        """
        pass

    def test_get_project_tickets(self) -> None:
        """Test case for get_project_tickets

        Get List of ProjectTicket
        """
        pass

    def test_get_project_tickets_by_id(self) -> None:
        """Test case for get_project_tickets_by_id

        Get ProjectTicket
        """
        pass

    def test_get_project_tickets_by_parent_id_activities(self) -> None:
        """Test case for get_project_tickets_by_parent_id_activities

        Get List of ActivityReference              Gets activities associated to the ticket              Please use the /sales/activities?conditions=ticket/id={id} endpoint
        """
        pass

    def test_get_project_tickets_by_parent_id_activities_count(self) -> None:
        """Test case for get_project_tickets_by_parent_id_activities_count

        Get Count of ActivityReference              Gets count of activities associated to the ticket              Please use the /sales/activities/count?conditions=ticket/id={id} endpoint
        """
        pass

    def test_get_project_tickets_by_parent_id_configurations(self) -> None:
        """Test case for get_project_tickets_by_parent_id_configurations

        Get List of ConfigurationReference
        """
        pass

    def test_get_project_tickets_by_parent_id_configurations_by_id(self) -> None:
        """Test case for get_project_tickets_by_parent_id_configurations_by_id

        Get ConfigurationReference
        """
        pass

    def test_get_project_tickets_by_parent_id_configurations_count(self) -> None:
        """Test case for get_project_tickets_by_parent_id_configurations_count

        Get Count of ConfigurationReference
        """
        pass

    def test_get_project_tickets_by_parent_id_documents(self) -> None:
        """Test case for get_project_tickets_by_parent_id_documents

        Get List of DocumentReference              Gets the documents associated to the ticket              Please use the /system/documents?recordType=Ticket&amp;recordId={id} endpoint
        """
        pass

    def test_get_project_tickets_by_parent_id_documents_count(self) -> None:
        """Test case for get_project_tickets_by_parent_id_documents_count

        Get Count of DocumentReference
        """
        pass

    def test_get_project_tickets_by_parent_id_products(self) -> None:
        """Test case for get_project_tickets_by_parent_id_products

        Get List of ProductReference              Gets the products associated to the ticket              Please use the /procurement/products?conditions=chargeToType='Ticket' AND chargeToId={id} endpoint
        """
        pass

    def test_get_project_tickets_by_parent_id_products_count(self) -> None:
        """Test case for get_project_tickets_by_parent_id_products_count

        Get Count of ProductReference              Gets the products associated to the ticket              Please use the /procurement/products/count?conditions=chargeToType='Ticket' AND chargeToId={id} endpoint
        """
        pass

    def test_get_project_tickets_by_parent_id_scheduleentries(self) -> None:
        """Test case for get_project_tickets_by_parent_id_scheduleentries

        Get List of ScheduleEntryReference              Gets the schedule entries associated to the ticket              Please use the /schedule/entries?conditions=type/id=4 AND objectId={id} endpoint
        """
        pass

    def test_get_project_tickets_by_parent_id_scheduleentries_count(self) -> None:
        """Test case for get_project_tickets_by_parent_id_scheduleentries_count

        Get Count of ScheduleEntryReference              Gets the schedule entries count associated to the ticket              Please use the /schedule/entries/count?conditions=type/id=4 AND objectId={id} endpoint
        """
        pass

    def test_get_project_tickets_by_parent_id_timeentries(self) -> None:
        """Test case for get_project_tickets_by_parent_id_timeentries

        Get List of TimeEntryReference              Gets time entries associated to the ticket              Please use the /time/entries?conditions=(chargeToType=\"ServiceTicket\" OR chargeToType=\"ProjectTicket\") AND chargeToId={id} endpoint
        """
        pass

    def test_get_project_tickets_by_parent_id_timeentries_count(self) -> None:
        """Test case for get_project_tickets_by_parent_id_timeentries_count

        Get Count of TimeEntryReference              Gets time entries count associated to the ticket              Please use the /time/entries/count?conditions=(chargeToType=\"ServiceTicket\" OR chargeToType=\"ProjectTicket\") AND chargeToId={id} endpoint
        """
        pass

    def test_get_project_tickets_count(self) -> None:
        """Test case for get_project_tickets_count

        Get Count of ProjectTicket
        """
        pass

    def test_patch_project_tickets_by_id(self) -> None:
        """Test case for patch_project_tickets_by_id

        Patch ProjectTicket
        """
        pass

    def test_post_project_tickets(self) -> None:
        """Test case for post_project_tickets

        Post ProjectTicket
        """
        pass

    def test_post_project_tickets_by_parent_id_configurations(self) -> None:
        """Test case for post_project_tickets_by_parent_id_configurations

        Post ConfigurationReference
        """
        pass

    def test_post_project_tickets_by_parent_id_convert(self) -> None:
        """Test case for post_project_tickets_by_parent_id_convert

        Post SuccessResponse
        """
        pass

    def test_post_project_tickets_search(self) -> None:
        """Test case for post_project_tickets_search

        Post List of ProjectTicket
        """
        pass

    def test_put_project_tickets_by_id(self) -> None:
        """Test case for put_project_tickets_by_id

        Put ProjectTicket
        """
        pass


if __name__ == '__main__':
    unittest.main()