# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, field_validator
from pydantic import Field
from connectwise_psa.models.document_reference import DocumentReference
from connectwise_psa.models.member_reference import MemberReference
from connectwise_psa.models.service_email_template_reference import ServiceEmailTemplateReference
from connectwise_psa.models.service_signoff_reference import ServiceSignoffReference
from connectwise_psa.models.service_status_reference import ServiceStatusReference
from connectwise_psa.models.system_department_reference import SystemDepartmentReference
from connectwise_psa.models.system_location_reference import SystemLocationReference
from connectwise_psa.models.work_role_reference import WorkRoleReference
from connectwise_psa.models.work_type_reference import WorkTypeReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Board(BaseModel):
    """
    Board
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    all_sort: Optional[StrictStr] = Field(default=None, alias="allSort")
    auto_assign_limit_amount: Optional[StrictInt] = Field(default=None, description="This field can only be set when autoAssignLimitFlag is true", alias="autoAssignLimitAmount")
    auto_assign_limit_flag: Optional[StrictBool] = Field(default=None, alias="autoAssignLimitFlag")
    auto_assign_new_ec_tickets_flag: Optional[StrictBool] = Field(default=None, alias="autoAssignNewECTicketsFlag")
    auto_assign_new_portal_tickets_flag: Optional[StrictBool] = Field(default=None, alias="autoAssignNewPortalTicketsFlag")
    auto_assign_new_tickets_flag: Optional[StrictBool] = Field(default=None, alias="autoAssignNewTicketsFlag")
    auto_assign_ticket_owner_flag: Optional[StrictBool] = Field(default=None, alias="autoAssignTicketOwnerFlag")
    auto_close_status: Optional[ServiceStatusReference] = Field(default=None, alias="autoCloseStatus")
    bill_expense: Optional[StrictStr] = Field(default=None, alias="billExpense")
    bill_product: Optional[StrictStr] = Field(default=None, alias="billProduct")
    bill_ticket_separately_flag: Optional[StrictBool] = Field(default=None, alias="billTicketSeparatelyFlag")
    bill_tickets_after_closed_flag: Optional[StrictBool] = Field(default=None, alias="billTicketsAfterClosedFlag")
    bill_time: Optional[StrictStr] = Field(default=None, alias="billTime")
    bill_unapproved_time_expense_flag: Optional[StrictBool] = Field(default=None, alias="billUnapprovedTimeExpenseFlag")
    board_icon: Optional[DocumentReference] = Field(default=None, alias="boardIcon")
    closed_loop_all_flag: Optional[StrictBool] = Field(default=None, alias="closedLoopAllFlag")
    closed_loop_discussions_flag: Optional[StrictBool] = Field(default=None, alias="closedLoopDiscussionsFlag")
    closed_loop_internal_analysis_flag: Optional[StrictBool] = Field(default=None, alias="closedLoopInternalAnalysisFlag")
    closed_loop_resolution_flag: Optional[StrictBool] = Field(default=None, alias="closedLoopResolutionFlag")
    contact_template: Optional[ServiceEmailTemplateReference] = Field(default=None, alias="contactTemplate")
    department: Optional[SystemDepartmentReference] = None
    discussions_locked_flag: Optional[StrictBool] = Field(default=None, alias="discussionsLockedFlag")
    dispatch_member: Optional[MemberReference] = Field(default=None, alias="dispatchMember")
    duty_manager_member: Optional[MemberReference] = Field(default=None, alias="dutyManagerMember")
    email_connector_allow_reopen_closed_flag: Optional[StrictBool] = Field(default=None, alias="emailConnectorAllowReopenClosedFlag")
    email_connector_never_reopen_by_days_closed_flag: Optional[StrictBool] = Field(default=None, description="This field can only be set when emailConnectorAllowReopenClosed is true.", alias="emailConnectorNeverReopenByDaysClosedFlag")
    email_connector_never_reopen_by_days_flag: Optional[StrictBool] = Field(default=None, description="This field can only be set when emailConnectorAllowReopenClosed is true.", alias="emailConnectorNeverReopenByDaysFlag")
    email_connector_new_ticket_no_match_flag: Optional[StrictBool] = Field(default=None, description="This field can only be set when emailConnectorAllowReopenClosed is true.", alias="emailConnectorNewTicketNoMatchFlag")
    email_connector_reopen_days_closed_limit: Optional[StrictInt] = Field(default=None, description="This field can only be set when emailConnectorNeverReopenByDaysClosedFlag and emailConnectorAllowReopenClosed are both true             This field is required when emailConnectorNeverReopenByDaysClosedFlag is true.", alias="emailConnectorReopenDaysClosedLimit")
    email_connector_reopen_days_limit: Optional[StrictInt] = Field(default=None, description="This field can only be set when emailConnectorNeverReopenByDaysFlag and emailConnectorAllowReopenClosed are both true             This field is required when emailConnectorNeverReopenByDaysFlag is true.", alias="emailConnectorReopenDaysLimit")
    email_connector_reopen_resources_flag: Optional[StrictBool] = Field(default=None, description="This field can only be set when emailConnectorAllowReopenClosed is true.", alias="emailConnectorReopenResourcesFlag")
    email_connector_reopen_status: Optional[ServiceStatusReference] = Field(default=None, alias="emailConnectorReopenStatus")
    id: Optional[StrictInt] = None
    inactive_flag: Optional[StrictBool] = Field(default=None, alias="inactiveFlag")
    internal_analysis_sort: Optional[StrictStr] = Field(default=None, alias="internalAnalysisSort")
    location: Optional[SystemLocationReference] = None
    mark_first_note_issue_flag: Optional[StrictBool] = Field(default=None, alias="markFirstNoteIssueFlag")
    name: StrictStr = Field(description=" Max length: 50;")
    notify_email_from: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="notifyEmailFrom")
    notify_email_from_name: Optional[StrictStr] = Field(default=None, description=" Max length: 60;", alias="notifyEmailFromName")
    oncall_member: Optional[MemberReference] = Field(default=None, alias="oncallMember")
    override_billing_setup_flag: Optional[StrictBool] = Field(default=None, alias="overrideBillingSetupFlag")
    percentage_calculation: Optional[StrictStr] = Field(default=None, alias="percentageCalculation")
    problem_sort: Optional[StrictStr] = Field(default=None, alias="problemSort")
    project_flag: Optional[StrictBool] = Field(default=None, alias="projectFlag")
    resolution_sort: Optional[StrictStr] = Field(default=None, alias="resolutionSort")
    resource_template: Optional[ServiceEmailTemplateReference] = Field(default=None, alias="resourceTemplate")
    restrict_board_by_default_flag: Optional[StrictBool] = Field(default=None, alias="restrictBoardByDefaultFlag")
    send_to_cc_flag: Optional[StrictBool] = Field(default=None, alias="sendToCCFlag")
    send_to_contact_flag: Optional[StrictBool] = Field(default=None, alias="sendToContactFlag")
    send_to_resource_flag: Optional[StrictBool] = Field(default=None, alias="sendToResourceFlag")
    service_manager_member: Optional[MemberReference] = Field(default=None, alias="serviceManagerMember")
    show_dependencies_flag: Optional[StrictBool] = Field(default=None, description="This field only shows if it is Project Board.", alias="showDependenciesFlag")
    show_estimates_flag: Optional[StrictBool] = Field(default=None, description="This field only shows if it is Project Board.", alias="showEstimatesFlag")
    sign_off_template: Optional[ServiceSignoffReference] = Field(default=None, alias="signOffTemplate")
    time_entry_discussion_flag: Optional[StrictBool] = Field(default=None, alias="timeEntryDiscussionFlag")
    time_entry_internal_analysis_flag: Optional[StrictBool] = Field(default=None, alias="timeEntryInternalAnalysisFlag")
    time_entry_locked_flag: Optional[StrictBool] = Field(default=None, alias="timeEntryLockedFlag")
    time_entry_resolution_flag: Optional[StrictBool] = Field(default=None, alias="timeEntryResolutionFlag")
    use_member_display_name_flag: Optional[StrictBool] = Field(default=None, alias="useMemberDisplayNameFlag")
    work_role: Optional[WorkRoleReference] = Field(default=None, alias="workRole")
    work_type: Optional[WorkTypeReference] = Field(default=None, alias="workType")
    __properties: ClassVar[List[str]] = ["_info", "allSort", "autoAssignLimitAmount", "autoAssignLimitFlag", "autoAssignNewECTicketsFlag", "autoAssignNewPortalTicketsFlag", "autoAssignNewTicketsFlag", "autoAssignTicketOwnerFlag", "autoCloseStatus", "billExpense", "billProduct", "billTicketSeparatelyFlag", "billTicketsAfterClosedFlag", "billTime", "billUnapprovedTimeExpenseFlag", "boardIcon", "closedLoopAllFlag", "closedLoopDiscussionsFlag", "closedLoopInternalAnalysisFlag", "closedLoopResolutionFlag", "contactTemplate", "department", "discussionsLockedFlag", "dispatchMember", "dutyManagerMember", "emailConnectorAllowReopenClosedFlag", "emailConnectorNeverReopenByDaysClosedFlag", "emailConnectorNeverReopenByDaysFlag", "emailConnectorNewTicketNoMatchFlag", "emailConnectorReopenDaysClosedLimit", "emailConnectorReopenDaysLimit", "emailConnectorReopenResourcesFlag", "emailConnectorReopenStatus", "id", "inactiveFlag", "internalAnalysisSort", "location", "markFirstNoteIssueFlag", "name", "notifyEmailFrom", "notifyEmailFromName", "oncallMember", "overrideBillingSetupFlag", "percentageCalculation", "problemSort", "projectFlag", "resolutionSort", "resourceTemplate", "restrictBoardByDefaultFlag", "sendToCCFlag", "sendToContactFlag", "sendToResourceFlag", "serviceManagerMember", "showDependenciesFlag", "showEstimatesFlag", "signOffTemplate", "timeEntryDiscussionFlag", "timeEntryInternalAnalysisFlag", "timeEntryLockedFlag", "timeEntryResolutionFlag", "useMemberDisplayNameFlag", "workRole", "workType"]

    @field_validator('all_sort')
    def all_sort_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Ascending', 'Descending'):
            raise ValueError("must be one of enum values ('Ascending', 'Descending')")
        return value

    @field_validator('bill_expense')
    def bill_expense_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Billable', 'DoNotBill', 'NoCharge', 'NoDefault'):
            raise ValueError("must be one of enum values ('Billable', 'DoNotBill', 'NoCharge', 'NoDefault')")
        return value

    @field_validator('bill_product')
    def bill_product_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Billable', 'DoNotBill', 'NoCharge', 'NoDefault'):
            raise ValueError("must be one of enum values ('Billable', 'DoNotBill', 'NoCharge', 'NoDefault')")
        return value

    @field_validator('bill_time')
    def bill_time_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Billable', 'DoNotBill', 'NoCharge', 'NoDefault'):
            raise ValueError("must be one of enum values ('Billable', 'DoNotBill', 'NoCharge', 'NoDefault')")
        return value

    @field_validator('internal_analysis_sort')
    def internal_analysis_sort_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Ascending', 'Descending'):
            raise ValueError("must be one of enum values ('Ascending', 'Descending')")
        return value

    @field_validator('percentage_calculation')
    def percentage_calculation_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ActualHours', 'Manual', 'ClosedPhases', 'ClosedTickets'):
            raise ValueError("must be one of enum values ('ActualHours', 'Manual', 'ClosedPhases', 'ClosedTickets')")
        return value

    @field_validator('problem_sort')
    def problem_sort_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Ascending', 'Descending'):
            raise ValueError("must be one of enum values ('Ascending', 'Descending')")
        return value

    @field_validator('resolution_sort')
    def resolution_sort_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Ascending', 'Descending'):
            raise ValueError("must be one of enum values ('Ascending', 'Descending')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Board from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of auto_close_status
        if self.auto_close_status:
            _dict['autoCloseStatus'] = self.auto_close_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of board_icon
        if self.board_icon:
            _dict['boardIcon'] = self.board_icon.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contact_template
        if self.contact_template:
            _dict['contactTemplate'] = self.contact_template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of department
        if self.department:
            _dict['department'] = self.department.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dispatch_member
        if self.dispatch_member:
            _dict['dispatchMember'] = self.dispatch_member.to_dict()
        # override the default output from pydantic by calling `to_dict()` of duty_manager_member
        if self.duty_manager_member:
            _dict['dutyManagerMember'] = self.duty_manager_member.to_dict()
        # override the default output from pydantic by calling `to_dict()` of email_connector_reopen_status
        if self.email_connector_reopen_status:
            _dict['emailConnectorReopenStatus'] = self.email_connector_reopen_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oncall_member
        if self.oncall_member:
            _dict['oncallMember'] = self.oncall_member.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resource_template
        if self.resource_template:
            _dict['resourceTemplate'] = self.resource_template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_manager_member
        if self.service_manager_member:
            _dict['serviceManagerMember'] = self.service_manager_member.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sign_off_template
        if self.sign_off_template:
            _dict['signOffTemplate'] = self.sign_off_template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of work_role
        if self.work_role:
            _dict['workRole'] = self.work_role.to_dict()
        # override the default output from pydantic by calling `to_dict()` of work_type
        if self.work_type:
            _dict['workType'] = self.work_type.to_dict()
        # set to None if all_sort (nullable) is None
        # and model_fields_set contains the field
        if self.all_sort is None and "all_sort" in self.model_fields_set:
            _dict['allSort'] = None

        # set to None if auto_assign_limit_amount (nullable) is None
        # and model_fields_set contains the field
        if self.auto_assign_limit_amount is None and "auto_assign_limit_amount" in self.model_fields_set:
            _dict['autoAssignLimitAmount'] = None

        # set to None if auto_assign_limit_flag (nullable) is None
        # and model_fields_set contains the field
        if self.auto_assign_limit_flag is None and "auto_assign_limit_flag" in self.model_fields_set:
            _dict['autoAssignLimitFlag'] = None

        # set to None if auto_assign_new_ec_tickets_flag (nullable) is None
        # and model_fields_set contains the field
        if self.auto_assign_new_ec_tickets_flag is None and "auto_assign_new_ec_tickets_flag" in self.model_fields_set:
            _dict['autoAssignNewECTicketsFlag'] = None

        # set to None if auto_assign_new_portal_tickets_flag (nullable) is None
        # and model_fields_set contains the field
        if self.auto_assign_new_portal_tickets_flag is None and "auto_assign_new_portal_tickets_flag" in self.model_fields_set:
            _dict['autoAssignNewPortalTicketsFlag'] = None

        # set to None if auto_assign_new_tickets_flag (nullable) is None
        # and model_fields_set contains the field
        if self.auto_assign_new_tickets_flag is None and "auto_assign_new_tickets_flag" in self.model_fields_set:
            _dict['autoAssignNewTicketsFlag'] = None

        # set to None if auto_assign_ticket_owner_flag (nullable) is None
        # and model_fields_set contains the field
        if self.auto_assign_ticket_owner_flag is None and "auto_assign_ticket_owner_flag" in self.model_fields_set:
            _dict['autoAssignTicketOwnerFlag'] = None

        # set to None if bill_expense (nullable) is None
        # and model_fields_set contains the field
        if self.bill_expense is None and "bill_expense" in self.model_fields_set:
            _dict['billExpense'] = None

        # set to None if bill_product (nullable) is None
        # and model_fields_set contains the field
        if self.bill_product is None and "bill_product" in self.model_fields_set:
            _dict['billProduct'] = None

        # set to None if bill_ticket_separately_flag (nullable) is None
        # and model_fields_set contains the field
        if self.bill_ticket_separately_flag is None and "bill_ticket_separately_flag" in self.model_fields_set:
            _dict['billTicketSeparatelyFlag'] = None

        # set to None if bill_tickets_after_closed_flag (nullable) is None
        # and model_fields_set contains the field
        if self.bill_tickets_after_closed_flag is None and "bill_tickets_after_closed_flag" in self.model_fields_set:
            _dict['billTicketsAfterClosedFlag'] = None

        # set to None if bill_time (nullable) is None
        # and model_fields_set contains the field
        if self.bill_time is None and "bill_time" in self.model_fields_set:
            _dict['billTime'] = None

        # set to None if bill_unapproved_time_expense_flag (nullable) is None
        # and model_fields_set contains the field
        if self.bill_unapproved_time_expense_flag is None and "bill_unapproved_time_expense_flag" in self.model_fields_set:
            _dict['billUnapprovedTimeExpenseFlag'] = None

        # set to None if closed_loop_all_flag (nullable) is None
        # and model_fields_set contains the field
        if self.closed_loop_all_flag is None and "closed_loop_all_flag" in self.model_fields_set:
            _dict['closedLoopAllFlag'] = None

        # set to None if closed_loop_discussions_flag (nullable) is None
        # and model_fields_set contains the field
        if self.closed_loop_discussions_flag is None and "closed_loop_discussions_flag" in self.model_fields_set:
            _dict['closedLoopDiscussionsFlag'] = None

        # set to None if closed_loop_internal_analysis_flag (nullable) is None
        # and model_fields_set contains the field
        if self.closed_loop_internal_analysis_flag is None and "closed_loop_internal_analysis_flag" in self.model_fields_set:
            _dict['closedLoopInternalAnalysisFlag'] = None

        # set to None if closed_loop_resolution_flag (nullable) is None
        # and model_fields_set contains the field
        if self.closed_loop_resolution_flag is None and "closed_loop_resolution_flag" in self.model_fields_set:
            _dict['closedLoopResolutionFlag'] = None

        # set to None if discussions_locked_flag (nullable) is None
        # and model_fields_set contains the field
        if self.discussions_locked_flag is None and "discussions_locked_flag" in self.model_fields_set:
            _dict['discussionsLockedFlag'] = None

        # set to None if email_connector_allow_reopen_closed_flag (nullable) is None
        # and model_fields_set contains the field
        if self.email_connector_allow_reopen_closed_flag is None and "email_connector_allow_reopen_closed_flag" in self.model_fields_set:
            _dict['emailConnectorAllowReopenClosedFlag'] = None

        # set to None if email_connector_never_reopen_by_days_closed_flag (nullable) is None
        # and model_fields_set contains the field
        if self.email_connector_never_reopen_by_days_closed_flag is None and "email_connector_never_reopen_by_days_closed_flag" in self.model_fields_set:
            _dict['emailConnectorNeverReopenByDaysClosedFlag'] = None

        # set to None if email_connector_never_reopen_by_days_flag (nullable) is None
        # and model_fields_set contains the field
        if self.email_connector_never_reopen_by_days_flag is None and "email_connector_never_reopen_by_days_flag" in self.model_fields_set:
            _dict['emailConnectorNeverReopenByDaysFlag'] = None

        # set to None if email_connector_new_ticket_no_match_flag (nullable) is None
        # and model_fields_set contains the field
        if self.email_connector_new_ticket_no_match_flag is None and "email_connector_new_ticket_no_match_flag" in self.model_fields_set:
            _dict['emailConnectorNewTicketNoMatchFlag'] = None

        # set to None if email_connector_reopen_days_closed_limit (nullable) is None
        # and model_fields_set contains the field
        if self.email_connector_reopen_days_closed_limit is None and "email_connector_reopen_days_closed_limit" in self.model_fields_set:
            _dict['emailConnectorReopenDaysClosedLimit'] = None

        # set to None if email_connector_reopen_days_limit (nullable) is None
        # and model_fields_set contains the field
        if self.email_connector_reopen_days_limit is None and "email_connector_reopen_days_limit" in self.model_fields_set:
            _dict['emailConnectorReopenDaysLimit'] = None

        # set to None if email_connector_reopen_resources_flag (nullable) is None
        # and model_fields_set contains the field
        if self.email_connector_reopen_resources_flag is None and "email_connector_reopen_resources_flag" in self.model_fields_set:
            _dict['emailConnectorReopenResourcesFlag'] = None

        # set to None if inactive_flag (nullable) is None
        # and model_fields_set contains the field
        if self.inactive_flag is None and "inactive_flag" in self.model_fields_set:
            _dict['inactiveFlag'] = None

        # set to None if internal_analysis_sort (nullable) is None
        # and model_fields_set contains the field
        if self.internal_analysis_sort is None and "internal_analysis_sort" in self.model_fields_set:
            _dict['internalAnalysisSort'] = None

        # set to None if mark_first_note_issue_flag (nullable) is None
        # and model_fields_set contains the field
        if self.mark_first_note_issue_flag is None and "mark_first_note_issue_flag" in self.model_fields_set:
            _dict['markFirstNoteIssueFlag'] = None

        # set to None if override_billing_setup_flag (nullable) is None
        # and model_fields_set contains the field
        if self.override_billing_setup_flag is None and "override_billing_setup_flag" in self.model_fields_set:
            _dict['overrideBillingSetupFlag'] = None

        # set to None if percentage_calculation (nullable) is None
        # and model_fields_set contains the field
        if self.percentage_calculation is None and "percentage_calculation" in self.model_fields_set:
            _dict['percentageCalculation'] = None

        # set to None if problem_sort (nullable) is None
        # and model_fields_set contains the field
        if self.problem_sort is None and "problem_sort" in self.model_fields_set:
            _dict['problemSort'] = None

        # set to None if project_flag (nullable) is None
        # and model_fields_set contains the field
        if self.project_flag is None and "project_flag" in self.model_fields_set:
            _dict['projectFlag'] = None

        # set to None if resolution_sort (nullable) is None
        # and model_fields_set contains the field
        if self.resolution_sort is None and "resolution_sort" in self.model_fields_set:
            _dict['resolutionSort'] = None

        # set to None if restrict_board_by_default_flag (nullable) is None
        # and model_fields_set contains the field
        if self.restrict_board_by_default_flag is None and "restrict_board_by_default_flag" in self.model_fields_set:
            _dict['restrictBoardByDefaultFlag'] = None

        # set to None if send_to_cc_flag (nullable) is None
        # and model_fields_set contains the field
        if self.send_to_cc_flag is None and "send_to_cc_flag" in self.model_fields_set:
            _dict['sendToCCFlag'] = None

        # set to None if send_to_contact_flag (nullable) is None
        # and model_fields_set contains the field
        if self.send_to_contact_flag is None and "send_to_contact_flag" in self.model_fields_set:
            _dict['sendToContactFlag'] = None

        # set to None if send_to_resource_flag (nullable) is None
        # and model_fields_set contains the field
        if self.send_to_resource_flag is None and "send_to_resource_flag" in self.model_fields_set:
            _dict['sendToResourceFlag'] = None

        # set to None if show_dependencies_flag (nullable) is None
        # and model_fields_set contains the field
        if self.show_dependencies_flag is None and "show_dependencies_flag" in self.model_fields_set:
            _dict['showDependenciesFlag'] = None

        # set to None if show_estimates_flag (nullable) is None
        # and model_fields_set contains the field
        if self.show_estimates_flag is None and "show_estimates_flag" in self.model_fields_set:
            _dict['showEstimatesFlag'] = None

        # set to None if time_entry_discussion_flag (nullable) is None
        # and model_fields_set contains the field
        if self.time_entry_discussion_flag is None and "time_entry_discussion_flag" in self.model_fields_set:
            _dict['timeEntryDiscussionFlag'] = None

        # set to None if time_entry_internal_analysis_flag (nullable) is None
        # and model_fields_set contains the field
        if self.time_entry_internal_analysis_flag is None and "time_entry_internal_analysis_flag" in self.model_fields_set:
            _dict['timeEntryInternalAnalysisFlag'] = None

        # set to None if time_entry_locked_flag (nullable) is None
        # and model_fields_set contains the field
        if self.time_entry_locked_flag is None and "time_entry_locked_flag" in self.model_fields_set:
            _dict['timeEntryLockedFlag'] = None

        # set to None if time_entry_resolution_flag (nullable) is None
        # and model_fields_set contains the field
        if self.time_entry_resolution_flag is None and "time_entry_resolution_flag" in self.model_fields_set:
            _dict['timeEntryResolutionFlag'] = None

        # set to None if use_member_display_name_flag (nullable) is None
        # and model_fields_set contains the field
        if self.use_member_display_name_flag is None and "use_member_display_name_flag" in self.model_fields_set:
            _dict['useMemberDisplayNameFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Board from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Board) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "allSort": obj.get("allSort"),
            "autoAssignLimitAmount": obj.get("autoAssignLimitAmount"),
            "autoAssignLimitFlag": obj.get("autoAssignLimitFlag"),
            "autoAssignNewECTicketsFlag": obj.get("autoAssignNewECTicketsFlag"),
            "autoAssignNewPortalTicketsFlag": obj.get("autoAssignNewPortalTicketsFlag"),
            "autoAssignNewTicketsFlag": obj.get("autoAssignNewTicketsFlag"),
            "autoAssignTicketOwnerFlag": obj.get("autoAssignTicketOwnerFlag"),
            "autoCloseStatus": ServiceStatusReference.from_dict(obj.get("autoCloseStatus")) if obj.get("autoCloseStatus") is not None else None,
            "billExpense": obj.get("billExpense"),
            "billProduct": obj.get("billProduct"),
            "billTicketSeparatelyFlag": obj.get("billTicketSeparatelyFlag"),
            "billTicketsAfterClosedFlag": obj.get("billTicketsAfterClosedFlag"),
            "billTime": obj.get("billTime"),
            "billUnapprovedTimeExpenseFlag": obj.get("billUnapprovedTimeExpenseFlag"),
            "boardIcon": DocumentReference.from_dict(obj.get("boardIcon")) if obj.get("boardIcon") is not None else None,
            "closedLoopAllFlag": obj.get("closedLoopAllFlag"),
            "closedLoopDiscussionsFlag": obj.get("closedLoopDiscussionsFlag"),
            "closedLoopInternalAnalysisFlag": obj.get("closedLoopInternalAnalysisFlag"),
            "closedLoopResolutionFlag": obj.get("closedLoopResolutionFlag"),
            "contactTemplate": ServiceEmailTemplateReference.from_dict(obj.get("contactTemplate")) if obj.get("contactTemplate") is not None else None,
            "department": SystemDepartmentReference.from_dict(obj.get("department")) if obj.get("department") is not None else None,
            "discussionsLockedFlag": obj.get("discussionsLockedFlag"),
            "dispatchMember": MemberReference.from_dict(obj.get("dispatchMember")) if obj.get("dispatchMember") is not None else None,
            "dutyManagerMember": MemberReference.from_dict(obj.get("dutyManagerMember")) if obj.get("dutyManagerMember") is not None else None,
            "emailConnectorAllowReopenClosedFlag": obj.get("emailConnectorAllowReopenClosedFlag"),
            "emailConnectorNeverReopenByDaysClosedFlag": obj.get("emailConnectorNeverReopenByDaysClosedFlag"),
            "emailConnectorNeverReopenByDaysFlag": obj.get("emailConnectorNeverReopenByDaysFlag"),
            "emailConnectorNewTicketNoMatchFlag": obj.get("emailConnectorNewTicketNoMatchFlag"),
            "emailConnectorReopenDaysClosedLimit": obj.get("emailConnectorReopenDaysClosedLimit"),
            "emailConnectorReopenDaysLimit": obj.get("emailConnectorReopenDaysLimit"),
            "emailConnectorReopenResourcesFlag": obj.get("emailConnectorReopenResourcesFlag"),
            "emailConnectorReopenStatus": ServiceStatusReference.from_dict(obj.get("emailConnectorReopenStatus")) if obj.get("emailConnectorReopenStatus") is not None else None,
            "id": obj.get("id"),
            "inactiveFlag": obj.get("inactiveFlag"),
            "internalAnalysisSort": obj.get("internalAnalysisSort"),
            "location": SystemLocationReference.from_dict(obj.get("location")) if obj.get("location") is not None else None,
            "markFirstNoteIssueFlag": obj.get("markFirstNoteIssueFlag"),
            "name": obj.get("name"),
            "notifyEmailFrom": obj.get("notifyEmailFrom"),
            "notifyEmailFromName": obj.get("notifyEmailFromName"),
            "oncallMember": MemberReference.from_dict(obj.get("oncallMember")) if obj.get("oncallMember") is not None else None,
            "overrideBillingSetupFlag": obj.get("overrideBillingSetupFlag"),
            "percentageCalculation": obj.get("percentageCalculation"),
            "problemSort": obj.get("problemSort"),
            "projectFlag": obj.get("projectFlag"),
            "resolutionSort": obj.get("resolutionSort"),
            "resourceTemplate": ServiceEmailTemplateReference.from_dict(obj.get("resourceTemplate")) if obj.get("resourceTemplate") is not None else None,
            "restrictBoardByDefaultFlag": obj.get("restrictBoardByDefaultFlag"),
            "sendToCCFlag": obj.get("sendToCCFlag"),
            "sendToContactFlag": obj.get("sendToContactFlag"),
            "sendToResourceFlag": obj.get("sendToResourceFlag"),
            "serviceManagerMember": MemberReference.from_dict(obj.get("serviceManagerMember")) if obj.get("serviceManagerMember") is not None else None,
            "showDependenciesFlag": obj.get("showDependenciesFlag"),
            "showEstimatesFlag": obj.get("showEstimatesFlag"),
            "signOffTemplate": ServiceSignoffReference.from_dict(obj.get("signOffTemplate")) if obj.get("signOffTemplate") is not None else None,
            "timeEntryDiscussionFlag": obj.get("timeEntryDiscussionFlag"),
            "timeEntryInternalAnalysisFlag": obj.get("timeEntryInternalAnalysisFlag"),
            "timeEntryLockedFlag": obj.get("timeEntryLockedFlag"),
            "timeEntryResolutionFlag": obj.get("timeEntryResolutionFlag"),
            "useMemberDisplayNameFlag": obj.get("useMemberDisplayNameFlag"),
            "workRole": WorkRoleReference.from_dict(obj.get("workRole")) if obj.get("workRole") is not None else None,
            "workType": WorkTypeReference.from_dict(obj.get("workType")) if obj.get("workType") is not None else None
        })
        return _obj

