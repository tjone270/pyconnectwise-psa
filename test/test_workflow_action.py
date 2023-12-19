# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from connectwise_psa.models.workflow_action import WorkflowAction

class TestWorkflowAction(unittest.TestCase):
    """WorkflowAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkflowAction:
        """Test WorkflowAction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkflowAction`
        """
        model = WorkflowAction()
        if include_optional:
            return WorkflowAction(
                info = {
                    'key' : ''
                    },
                activity_status = connectwise_psa.models.activity_status_reference.ActivityStatusReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                activity_type = connectwise_psa.models.activity_type_reference.ActivityTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                attach_configurations_for = 'Company',
                attached_track = connectwise_psa.models.track_reference.TrackReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                attachments = [
                    56
                    ],
                audit_notes_flag = True,
                automate_script = connectwise_psa.models.automate_script_reference.AutomateScriptReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                bcc_contact = connectwise_psa.models.contact_reference.ContactReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                board = connectwise_psa.models.board_reference.BoardReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                board_status = connectwise_psa.models.service_status_reference.ServiceStatusReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', 
                    sort = 56, ),
                cc_contact = connectwise_psa.models.contact_reference.ContactReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                company_status = connectwise_psa.models.company_status_reference.CompanyStatusReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                configuration_status = connectwise_psa.models.configuration_status_reference.ConfigurationStatusReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                configuration_type = connectwise_psa.models.configuration_type_reference.ConfigurationTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                days_to_execute = 56,
                detail_notes_flag = True,
                email_from = '',
                email_recipient = '',
                group = connectwise_psa.models.group_reference.GroupReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                id = 56,
                internal_notes_flag = True,
                invoice_min_days = 56,
                notes = '',
                notify_from = connectwise_psa.models.notification_recipient_reference.NotificationRecipientReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                notify_type = connectwise_psa.models.notify_type_reference.NotifyTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                notify_who = connectwise_psa.models.notification_recipient_reference.NotificationRecipientReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                project_status = connectwise_psa.models.project_status_reference.ProjectStatusReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                sales_order_status = connectwise_psa.models.order_status_reference.OrderStatusReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                script_fail_status = connectwise_psa.models.service_status_reference.ServiceStatusReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', 
                    sort = 56, ),
                script_success_status = connectwise_psa.models.service_status_reference.ServiceStatusReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', 
                    sort = 56, ),
                service_item = connectwise_psa.models.service_item_reference.ServiceItemReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                service_priority = connectwise_psa.models.priority_reference.PriorityReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    level = '', 
                    name = '', 
                    sort = 56, ),
                service_sub_type = connectwise_psa.models.service_sub_type_reference.ServiceSubTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                service_survey = connectwise_psa.models.service_survey_reference.ServiceSurveyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                service_template = connectwise_psa.models.service_template_reference.ServiceTemplateReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', 
                    summary = '', ),
                service_type = connectwise_psa.models.service_type_reference.ServiceTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                specific_member_from = connectwise_psa.models.member_reference.MemberReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                specific_member_to = connectwise_psa.models.member_reference.MemberReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                specific_team_to = connectwise_psa.models.generic_board_team_reference.GenericBoardTeamReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    is_project_team_flag = True, 
                    name = '', ),
                subject = '',
                update_owner_flag = True
            )
        else:
            return WorkflowAction(
                notify_type = connectwise_psa.models.notify_type_reference.NotifyTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
        )
        """

    def testWorkflowAction(self):
        """Test WorkflowAction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
