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
from connectwise_psa.models.activity_status_reference import ActivityStatusReference
from connectwise_psa.models.activity_type_reference import ActivityTypeReference
from connectwise_psa.models.automate_script_reference import AutomateScriptReference
from connectwise_psa.models.board_reference import BoardReference
from connectwise_psa.models.company_status_reference import CompanyStatusReference
from connectwise_psa.models.configuration_status_reference import ConfigurationStatusReference
from connectwise_psa.models.configuration_type_reference import ConfigurationTypeReference
from connectwise_psa.models.contact_reference import ContactReference
from connectwise_psa.models.generic_board_team_reference import GenericBoardTeamReference
from connectwise_psa.models.group_reference import GroupReference
from connectwise_psa.models.member_reference import MemberReference
from connectwise_psa.models.notification_recipient_reference import NotificationRecipientReference
from connectwise_psa.models.notify_type_reference import NotifyTypeReference
from connectwise_psa.models.order_status_reference import OrderStatusReference
from connectwise_psa.models.priority_reference import PriorityReference
from connectwise_psa.models.project_status_reference import ProjectStatusReference
from connectwise_psa.models.service_item_reference import ServiceItemReference
from connectwise_psa.models.service_status_reference import ServiceStatusReference
from connectwise_psa.models.service_sub_type_reference import ServiceSubTypeReference
from connectwise_psa.models.service_survey_reference import ServiceSurveyReference
from connectwise_psa.models.service_template_reference import ServiceTemplateReference
from connectwise_psa.models.service_type_reference import ServiceTypeReference
from connectwise_psa.models.track_reference import TrackReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WorkflowAction(BaseModel):
    """
    WorkflowAction
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    activity_status: Optional[ActivityStatusReference] = Field(default=None, alias="activityStatus")
    activity_type: Optional[ActivityTypeReference] = Field(default=None, alias="activityType")
    attach_configurations_for: Optional[StrictStr] = Field(default=None, description="Required when notifyType is set to: \"Attach Configuration\"", alias="attachConfigurationsFor")
    attached_track: Optional[TrackReference] = Field(default=None, alias="attachedTrack")
    attachments: Optional[List[StrictInt]] = None
    audit_notes_flag: Optional[StrictBool] = Field(default=None, alias="auditNotesFlag")
    automate_script: Optional[AutomateScriptReference] = Field(default=None, alias="automateScript")
    bcc_contact: Optional[ContactReference] = Field(default=None, alias="bccContact")
    board: Optional[BoardReference] = None
    board_status: Optional[ServiceStatusReference] = Field(default=None, alias="boardStatus")
    cc_contact: Optional[ContactReference] = Field(default=None, alias="ccContact")
    company_status: Optional[CompanyStatusReference] = Field(default=None, alias="companyStatus")
    configuration_status: Optional[ConfigurationStatusReference] = Field(default=None, alias="configurationStatus")
    configuration_type: Optional[ConfigurationTypeReference] = Field(default=None, alias="configurationType")
    days_to_execute: Optional[StrictInt] = Field(default=None, alias="daysToExecute")
    detail_notes_flag: Optional[StrictBool] = Field(default=None, alias="detailNotesFlag")
    email_from: Optional[StrictStr] = Field(default=None, description="Required when notifyFrom is set to: \"Email Address\" Max length: 250;", alias="emailFrom")
    email_recipient: Optional[StrictStr] = Field(default=None, description="Required when notifyWho is set to: \"Email Address\" Max length: 250;", alias="emailRecipient")
    group: Optional[GroupReference] = None
    id: Optional[StrictInt] = None
    internal_notes_flag: Optional[StrictBool] = Field(default=None, alias="internalNotesFlag")
    invoice_min_days: Optional[StrictInt] = Field(default=None, alias="invoiceMinDays")
    notes: Optional[StrictStr] = None
    notify_from: Optional[NotificationRecipientReference] = Field(default=None, alias="notifyFrom")
    notify_type: NotifyTypeReference = Field(alias="notifyType")
    notify_who: Optional[NotificationRecipientReference] = Field(default=None, alias="notifyWho")
    project_status: Optional[ProjectStatusReference] = Field(default=None, alias="projectStatus")
    sales_order_status: Optional[OrderStatusReference] = Field(default=None, alias="salesOrderStatus")
    script_fail_status: Optional[ServiceStatusReference] = Field(default=None, alias="scriptFailStatus")
    script_success_status: Optional[ServiceStatusReference] = Field(default=None, alias="scriptSuccessStatus")
    service_item: Optional[ServiceItemReference] = Field(default=None, alias="serviceItem")
    service_priority: Optional[PriorityReference] = Field(default=None, alias="servicePriority")
    service_sub_type: Optional[ServiceSubTypeReference] = Field(default=None, alias="serviceSubType")
    service_survey: Optional[ServiceSurveyReference] = Field(default=None, alias="serviceSurvey")
    service_template: Optional[ServiceTemplateReference] = Field(default=None, alias="serviceTemplate")
    service_type: Optional[ServiceTypeReference] = Field(default=None, alias="serviceType")
    specific_member_from: Optional[MemberReference] = Field(default=None, alias="specificMemberFrom")
    specific_member_to: Optional[MemberReference] = Field(default=None, alias="specificMemberTo")
    specific_team_to: Optional[GenericBoardTeamReference] = Field(default=None, alias="specificTeamTo")
    subject: Optional[StrictStr] = Field(default=None, description="Required when notifyType is set to: \"Create Activity\", \"Send Email\", \"Assign Resource\" Max length: 100;")
    update_owner_flag: Optional[StrictBool] = Field(default=None, alias="updateOwnerFlag")
    __properties: ClassVar[List[str]] = ["_info", "activityStatus", "activityType", "attachConfigurationsFor", "attachedTrack", "attachments", "auditNotesFlag", "automateScript", "bccContact", "board", "boardStatus", "ccContact", "companyStatus", "configurationStatus", "configurationType", "daysToExecute", "detailNotesFlag", "emailFrom", "emailRecipient", "group", "id", "internalNotesFlag", "invoiceMinDays", "notes", "notifyFrom", "notifyType", "notifyWho", "projectStatus", "salesOrderStatus", "scriptFailStatus", "scriptSuccessStatus", "serviceItem", "servicePriority", "serviceSubType", "serviceSurvey", "serviceTemplate", "serviceType", "specificMemberFrom", "specificMemberTo", "specificTeamTo", "subject", "updateOwnerFlag"]

    @field_validator('attach_configurations_for')
    def attach_configurations_for_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Company', 'Contact'):
            raise ValueError("must be one of enum values ('Company', 'Contact')")
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
        """Create an instance of WorkflowAction from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of activity_status
        if self.activity_status:
            _dict['activityStatus'] = self.activity_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of activity_type
        if self.activity_type:
            _dict['activityType'] = self.activity_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of attached_track
        if self.attached_track:
            _dict['attachedTrack'] = self.attached_track.to_dict()
        # override the default output from pydantic by calling `to_dict()` of automate_script
        if self.automate_script:
            _dict['automateScript'] = self.automate_script.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bcc_contact
        if self.bcc_contact:
            _dict['bccContact'] = self.bcc_contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of board
        if self.board:
            _dict['board'] = self.board.to_dict()
        # override the default output from pydantic by calling `to_dict()` of board_status
        if self.board_status:
            _dict['boardStatus'] = self.board_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cc_contact
        if self.cc_contact:
            _dict['ccContact'] = self.cc_contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of company_status
        if self.company_status:
            _dict['companyStatus'] = self.company_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of configuration_status
        if self.configuration_status:
            _dict['configurationStatus'] = self.configuration_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of configuration_type
        if self.configuration_type:
            _dict['configurationType'] = self.configuration_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict['group'] = self.group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of notify_from
        if self.notify_from:
            _dict['notifyFrom'] = self.notify_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of notify_type
        if self.notify_type:
            _dict['notifyType'] = self.notify_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of notify_who
        if self.notify_who:
            _dict['notifyWho'] = self.notify_who.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project_status
        if self.project_status:
            _dict['projectStatus'] = self.project_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sales_order_status
        if self.sales_order_status:
            _dict['salesOrderStatus'] = self.sales_order_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of script_fail_status
        if self.script_fail_status:
            _dict['scriptFailStatus'] = self.script_fail_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of script_success_status
        if self.script_success_status:
            _dict['scriptSuccessStatus'] = self.script_success_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_item
        if self.service_item:
            _dict['serviceItem'] = self.service_item.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_priority
        if self.service_priority:
            _dict['servicePriority'] = self.service_priority.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_sub_type
        if self.service_sub_type:
            _dict['serviceSubType'] = self.service_sub_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_survey
        if self.service_survey:
            _dict['serviceSurvey'] = self.service_survey.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_template
        if self.service_template:
            _dict['serviceTemplate'] = self.service_template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_type
        if self.service_type:
            _dict['serviceType'] = self.service_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of specific_member_from
        if self.specific_member_from:
            _dict['specificMemberFrom'] = self.specific_member_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of specific_member_to
        if self.specific_member_to:
            _dict['specificMemberTo'] = self.specific_member_to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of specific_team_to
        if self.specific_team_to:
            _dict['specificTeamTo'] = self.specific_team_to.to_dict()
        # set to None if attach_configurations_for (nullable) is None
        # and model_fields_set contains the field
        if self.attach_configurations_for is None and "attach_configurations_for" in self.model_fields_set:
            _dict['attachConfigurationsFor'] = None

        # set to None if audit_notes_flag (nullable) is None
        # and model_fields_set contains the field
        if self.audit_notes_flag is None and "audit_notes_flag" in self.model_fields_set:
            _dict['auditNotesFlag'] = None

        # set to None if days_to_execute (nullable) is None
        # and model_fields_set contains the field
        if self.days_to_execute is None and "days_to_execute" in self.model_fields_set:
            _dict['daysToExecute'] = None

        # set to None if detail_notes_flag (nullable) is None
        # and model_fields_set contains the field
        if self.detail_notes_flag is None and "detail_notes_flag" in self.model_fields_set:
            _dict['detailNotesFlag'] = None

        # set to None if internal_notes_flag (nullable) is None
        # and model_fields_set contains the field
        if self.internal_notes_flag is None and "internal_notes_flag" in self.model_fields_set:
            _dict['internalNotesFlag'] = None

        # set to None if invoice_min_days (nullable) is None
        # and model_fields_set contains the field
        if self.invoice_min_days is None and "invoice_min_days" in self.model_fields_set:
            _dict['invoiceMinDays'] = None

        # set to None if update_owner_flag (nullable) is None
        # and model_fields_set contains the field
        if self.update_owner_flag is None and "update_owner_flag" in self.model_fields_set:
            _dict['updateOwnerFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WorkflowAction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in WorkflowAction) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "activityStatus": ActivityStatusReference.from_dict(obj.get("activityStatus")) if obj.get("activityStatus") is not None else None,
            "activityType": ActivityTypeReference.from_dict(obj.get("activityType")) if obj.get("activityType") is not None else None,
            "attachConfigurationsFor": obj.get("attachConfigurationsFor"),
            "attachedTrack": TrackReference.from_dict(obj.get("attachedTrack")) if obj.get("attachedTrack") is not None else None,
            "attachments": obj.get("attachments"),
            "auditNotesFlag": obj.get("auditNotesFlag"),
            "automateScript": AutomateScriptReference.from_dict(obj.get("automateScript")) if obj.get("automateScript") is not None else None,
            "bccContact": ContactReference.from_dict(obj.get("bccContact")) if obj.get("bccContact") is not None else None,
            "board": BoardReference.from_dict(obj.get("board")) if obj.get("board") is not None else None,
            "boardStatus": ServiceStatusReference.from_dict(obj.get("boardStatus")) if obj.get("boardStatus") is not None else None,
            "ccContact": ContactReference.from_dict(obj.get("ccContact")) if obj.get("ccContact") is not None else None,
            "companyStatus": CompanyStatusReference.from_dict(obj.get("companyStatus")) if obj.get("companyStatus") is not None else None,
            "configurationStatus": ConfigurationStatusReference.from_dict(obj.get("configurationStatus")) if obj.get("configurationStatus") is not None else None,
            "configurationType": ConfigurationTypeReference.from_dict(obj.get("configurationType")) if obj.get("configurationType") is not None else None,
            "daysToExecute": obj.get("daysToExecute"),
            "detailNotesFlag": obj.get("detailNotesFlag"),
            "emailFrom": obj.get("emailFrom"),
            "emailRecipient": obj.get("emailRecipient"),
            "group": GroupReference.from_dict(obj.get("group")) if obj.get("group") is not None else None,
            "id": obj.get("id"),
            "internalNotesFlag": obj.get("internalNotesFlag"),
            "invoiceMinDays": obj.get("invoiceMinDays"),
            "notes": obj.get("notes"),
            "notifyFrom": NotificationRecipientReference.from_dict(obj.get("notifyFrom")) if obj.get("notifyFrom") is not None else None,
            "notifyType": NotifyTypeReference.from_dict(obj.get("notifyType")) if obj.get("notifyType") is not None else None,
            "notifyWho": NotificationRecipientReference.from_dict(obj.get("notifyWho")) if obj.get("notifyWho") is not None else None,
            "projectStatus": ProjectStatusReference.from_dict(obj.get("projectStatus")) if obj.get("projectStatus") is not None else None,
            "salesOrderStatus": OrderStatusReference.from_dict(obj.get("salesOrderStatus")) if obj.get("salesOrderStatus") is not None else None,
            "scriptFailStatus": ServiceStatusReference.from_dict(obj.get("scriptFailStatus")) if obj.get("scriptFailStatus") is not None else None,
            "scriptSuccessStatus": ServiceStatusReference.from_dict(obj.get("scriptSuccessStatus")) if obj.get("scriptSuccessStatus") is not None else None,
            "serviceItem": ServiceItemReference.from_dict(obj.get("serviceItem")) if obj.get("serviceItem") is not None else None,
            "servicePriority": PriorityReference.from_dict(obj.get("servicePriority")) if obj.get("servicePriority") is not None else None,
            "serviceSubType": ServiceSubTypeReference.from_dict(obj.get("serviceSubType")) if obj.get("serviceSubType") is not None else None,
            "serviceSurvey": ServiceSurveyReference.from_dict(obj.get("serviceSurvey")) if obj.get("serviceSurvey") is not None else None,
            "serviceTemplate": ServiceTemplateReference.from_dict(obj.get("serviceTemplate")) if obj.get("serviceTemplate") is not None else None,
            "serviceType": ServiceTypeReference.from_dict(obj.get("serviceType")) if obj.get("serviceType") is not None else None,
            "specificMemberFrom": MemberReference.from_dict(obj.get("specificMemberFrom")) if obj.get("specificMemberFrom") is not None else None,
            "specificMemberTo": MemberReference.from_dict(obj.get("specificMemberTo")) if obj.get("specificMemberTo") is not None else None,
            "specificTeamTo": GenericBoardTeamReference.from_dict(obj.get("specificTeamTo")) if obj.get("specificTeamTo") is not None else None,
            "subject": obj.get("subject"),
            "updateOwnerFlag": obj.get("updateOwnerFlag")
        })
        return _obj

