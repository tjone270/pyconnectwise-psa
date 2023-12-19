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
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
from connectwise_psa.models.member_reference import MemberReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TimeEntryAudit(BaseModel):
    """
    TimeEntryAudit
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    id: Optional[StrictInt] = None
    member: Optional[MemberReference] = None
    message: Optional[StrictStr] = None
    new_value: Optional[StrictStr] = Field(default=None, alias="newValue")
    old_value: Optional[StrictStr] = Field(default=None, alias="oldValue")
    source: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    value: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["_info", "id", "member", "message", "newValue", "oldValue", "source", "type", "value"]

    @field_validator('source')
    def source_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('None', 'Member', 'API', 'Workflow', 'Portal', 'Mobile', 'Network', 'EmailConnector', 'MassMaintenance', 'Application', 'SystemAPI', 'Conversion'):
            raise ValueError("must be one of enum values ('None', 'Member', 'API', 'Workflow', 'Portal', 'Mobile', 'Network', 'EmailConnector', 'MassMaintenance', 'Application', 'SystemAPI', 'Conversion')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Activity', 'CloseDate', 'Company', 'Contact', 'Conversion', 'Document', 'Forecast', 'Note', 'Notes', 'Opportunity', 'Products', 'Stage', 'Status', 'Surveys', 'Team', 'Tracks', 'Configuration', 'ConfigurationQuestions', 'DeviceBackupDetails', 'Tickets', 'Subject', 'ActivityOverview', 'Schedule', 'Resources', 'ExpenseEntry', 'Member', 'Date', 'Classification', 'Amount', 'ExpenseType', 'WorkType', 'WorkRole', 'Mileage', 'Billing', 'ExpenseHeader', 'Project', 'TimeEntry', 'TicketStatus', 'DateTime', 'DeductHours', 'ActualHours', 'Invoice', 'CompanyFinance', 'Billable', 'SalesOrder', 'Shipping', 'Profile', 'Group', 'GroupContact', 'GroupCompany', 'Options', 'Site', 'Agreement', 'Addition', 'Adjustment', 'Microsoft365', 'API', 'ProjectFinance', 'CompanyProfile', 'CompanyTeam', 'CompanyMgmt', 'InvoiceTotal', 'BillingInformation', 'ShippingInformation', 'BillingStatus', 'Location', 'Department', 'Territory', 'Payment', 'Credit', 'SubcontractorInformation', 'InvoicingParameters', 'ApplicationParameters', 'Finance', 'Invoicing', 'Email', 'Batching', 'KnowledgeBase', 'KbArticle', 'KnowledgeBaseApproval', 'KnowledgeBaseTicket', 'ManageNetwork', 'Tasks', 'CustomField', 'ScreenConnect', 'SLA', 'Ticket', 'Workflow', 'Record', 'CombinedTickets', 'Template', 'PurchaseOrder', 'Meeting', 'RmaOverview', 'ReturnedBy', 'PurchasedFromVendor', 'WarrantyVendor', 'RepairVendor', 'AdditionalDetails', 'TicketTemplate', 'AutoGeneration', 'TimeInternalNote', 'TimeDiscussion', 'TimeInternal', 'TimeResolution', 'MemberTemplate', 'Delegation', 'Skill', 'Certification', 'Accrual', 'ApiKey', 'Login', 'Notifications', 'System', 'ServiceBoard', 'ProjectBoard', 'Scheduling', 'TimeBillingExpense', 'CRM', 'Procurement', 'JobRole', 'Details', 'Authentication'):
            raise ValueError("must be one of enum values ('Activity', 'CloseDate', 'Company', 'Contact', 'Conversion', 'Document', 'Forecast', 'Note', 'Notes', 'Opportunity', 'Products', 'Stage', 'Status', 'Surveys', 'Team', 'Tracks', 'Configuration', 'ConfigurationQuestions', 'DeviceBackupDetails', 'Tickets', 'Subject', 'ActivityOverview', 'Schedule', 'Resources', 'ExpenseEntry', 'Member', 'Date', 'Classification', 'Amount', 'ExpenseType', 'WorkType', 'WorkRole', 'Mileage', 'Billing', 'ExpenseHeader', 'Project', 'TimeEntry', 'TicketStatus', 'DateTime', 'DeductHours', 'ActualHours', 'Invoice', 'CompanyFinance', 'Billable', 'SalesOrder', 'Shipping', 'Profile', 'Group', 'GroupContact', 'GroupCompany', 'Options', 'Site', 'Agreement', 'Addition', 'Adjustment', 'Microsoft365', 'API', 'ProjectFinance', 'CompanyProfile', 'CompanyTeam', 'CompanyMgmt', 'InvoiceTotal', 'BillingInformation', 'ShippingInformation', 'BillingStatus', 'Location', 'Department', 'Territory', 'Payment', 'Credit', 'SubcontractorInformation', 'InvoicingParameters', 'ApplicationParameters', 'Finance', 'Invoicing', 'Email', 'Batching', 'KnowledgeBase', 'KbArticle', 'KnowledgeBaseApproval', 'KnowledgeBaseTicket', 'ManageNetwork', 'Tasks', 'CustomField', 'ScreenConnect', 'SLA', 'Ticket', 'Workflow', 'Record', 'CombinedTickets', 'Template', 'PurchaseOrder', 'Meeting', 'RmaOverview', 'ReturnedBy', 'PurchasedFromVendor', 'WarrantyVendor', 'RepairVendor', 'AdditionalDetails', 'TicketTemplate', 'AutoGeneration', 'TimeInternalNote', 'TimeDiscussion', 'TimeInternal', 'TimeResolution', 'MemberTemplate', 'Delegation', 'Skill', 'Certification', 'Accrual', 'ApiKey', 'Login', 'Notifications', 'System', 'ServiceBoard', 'ProjectBoard', 'Scheduling', 'TimeBillingExpense', 'CRM', 'Procurement', 'JobRole', 'Details', 'Authentication')")
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
        """Create an instance of TimeEntryAudit from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of member
        if self.member:
            _dict['member'] = self.member.to_dict()
        # set to None if source (nullable) is None
        # and model_fields_set contains the field
        if self.source is None and "source" in self.model_fields_set:
            _dict['source'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TimeEntryAudit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in TimeEntryAudit) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "id": obj.get("id"),
            "member": MemberReference.from_dict(obj.get("member")) if obj.get("member") is not None else None,
            "message": obj.get("message"),
            "newValue": obj.get("newValue"),
            "oldValue": obj.get("oldValue"),
            "source": obj.get("source"),
            "type": obj.get("type"),
            "value": obj.get("value")
        })
        return _obj


