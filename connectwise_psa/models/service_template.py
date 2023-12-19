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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from connectwise_psa.models.agreement_reference import AgreementReference
from connectwise_psa.models.board_reference import BoardReference
from connectwise_psa.models.company_reference import CompanyReference
from connectwise_psa.models.contact_reference import ContactReference
from connectwise_psa.models.member_reference import MemberReference
from connectwise_psa.models.priority_reference import PriorityReference
from connectwise_psa.models.service_item_reference import ServiceItemReference
from connectwise_psa.models.service_location_reference import ServiceLocationReference
from connectwise_psa.models.service_source_reference import ServiceSourceReference
from connectwise_psa.models.service_status_reference import ServiceStatusReference
from connectwise_psa.models.service_sub_type_reference import ServiceSubTypeReference
from connectwise_psa.models.service_team_reference import ServiceTeamReference
from connectwise_psa.models.service_type_reference import ServiceTypeReference
from connectwise_psa.models.site_reference import SiteReference
from connectwise_psa.models.system_department_reference import SystemDepartmentReference
from connectwise_psa.models.system_location_reference import SystemLocationReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ServiceTemplate(BaseModel):
    """
    ServiceTemplate
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    agreement: Optional[AgreementReference] = None
    assigned_by: Optional[MemberReference] = Field(default=None, alias="assignedBy")
    assigned_notify_flag: Optional[StrictBool] = Field(default=None, alias="assignedNotifyFlag")
    attach_schedule_to_new_service_flag: Optional[StrictBool] = Field(default=None, alias="attachScheduleToNewServiceFlag")
    bill_complete_flag: Optional[StrictBool] = Field(default=None, alias="billComplete_Flag")
    bill_service_separately_flag: Optional[StrictBool] = Field(default=None, alias="billServiceSeparatelyFlag")
    bill_unapproved_time_and_expenses_flag: Optional[StrictBool] = Field(default=None, alias="billUnapprovedTimeAndExpensesFlag")
    billing_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="billingAmount")
    billing_method: Optional[StrictStr] = Field(default=None, alias="billingMethod")
    board: Optional[BoardReference] = None
    company: Optional[CompanyReference] = None
    contact: Optional[ContactReference] = None
    department: Optional[SystemDepartmentReference] = None
    email_cc: Optional[StrictStr] = Field(default=None, alias="emailCC")
    email_cc_flag: Optional[StrictBool] = Field(default=None, alias="emailCCFlag")
    email_contact_flag: Optional[StrictBool] = Field(default=None, alias="emailContactFlag")
    email_resource_flag: Optional[StrictBool] = Field(default=None, alias="emailResourceFlag")
    expense_billable_flag: Optional[StrictBool] = Field(default=None, alias="expenseBillableFlag")
    expense_invoice_flag: Optional[StrictBool] = Field(default=None, alias="expenseInvoiceFlag")
    hours_budget: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="hoursBudget")
    id: Optional[StrictInt] = None
    impact: Optional[StrictStr] = None
    internal_analysis: Optional[StrictStr] = Field(default=None, alias="internalAnalysis")
    item: Optional[ServiceItemReference] = None
    location: Optional[SystemLocationReference] = None
    name: Optional[StrictStr] = None
    override_flag: Optional[StrictBool] = Field(default=None, alias="overrideFlag")
    priority: Optional[PriorityReference] = None
    problem: Optional[StrictStr] = None
    product_invoice_flag: Optional[StrictBool] = Field(default=None, alias="productInvoiceFlag")
    purchase_order_number: Optional[StrictStr] = Field(default=None, alias="purchaseOrderNumber")
    reference: Optional[StrictStr] = None
    restrict_downpayment_flag: Optional[StrictBool] = Field(default=None, alias="restrictDownpaymentFlag")
    schedule_days_before: Optional[StrictInt] = Field(default=None, alias="scheduleDaysBefore")
    service_days_before: Optional[StrictInt] = Field(default=None, alias="serviceDaysBefore")
    service_location: Optional[ServiceLocationReference] = Field(default=None, alias="serviceLocation")
    severity: Optional[StrictStr] = None
    site: Optional[SiteReference] = None
    source: Optional[ServiceSourceReference] = None
    status: Optional[ServiceStatusReference] = None
    subtype: Optional[ServiceSubTypeReference] = None
    summary: Optional[StrictStr] = None
    team: Optional[ServiceTeamReference] = None
    template_flag: Optional[StrictBool] = Field(default=None, alias="templateFlag")
    time_billable_flag: Optional[StrictBool] = Field(default=None, alias="timeBillableFlag")
    time_invoice_flag: Optional[StrictBool] = Field(default=None, alias="timeInvoiceFlag")
    type: Optional[ServiceTypeReference] = None
    __properties: ClassVar[List[str]] = ["_info", "agreement", "assignedBy", "assignedNotifyFlag", "attachScheduleToNewServiceFlag", "billComplete_Flag", "billServiceSeparatelyFlag", "billUnapprovedTimeAndExpensesFlag", "billingAmount", "billingMethod", "board", "company", "contact", "department", "emailCC", "emailCCFlag", "emailContactFlag", "emailResourceFlag", "expenseBillableFlag", "expenseInvoiceFlag", "hoursBudget", "id", "impact", "internalAnalysis", "item", "location", "name", "overrideFlag", "priority", "problem", "productInvoiceFlag", "purchaseOrderNumber", "reference", "restrictDownpaymentFlag", "scheduleDaysBefore", "serviceDaysBefore", "serviceLocation", "severity", "site", "source", "status", "subtype", "summary", "team", "templateFlag", "timeBillableFlag", "timeInvoiceFlag", "type"]

    @field_validator('billing_method')
    def billing_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ActualRates', 'FixedFee', 'NotToExceed', 'OverrideRate'):
            raise ValueError("must be one of enum values ('ActualRates', 'FixedFee', 'NotToExceed', 'OverrideRate')")
        return value

    @field_validator('impact')
    def impact_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Low', 'Medium', 'High'):
            raise ValueError("must be one of enum values ('Low', 'Medium', 'High')")
        return value

    @field_validator('severity')
    def severity_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Low', 'Medium', 'High'):
            raise ValueError("must be one of enum values ('Low', 'Medium', 'High')")
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
        """Create an instance of ServiceTemplate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of agreement
        if self.agreement:
            _dict['agreement'] = self.agreement.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assigned_by
        if self.assigned_by:
            _dict['assignedBy'] = self.assigned_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of board
        if self.board:
            _dict['board'] = self.board.to_dict()
        # override the default output from pydantic by calling `to_dict()` of company
        if self.company:
            _dict['company'] = self.company.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contact
        if self.contact:
            _dict['contact'] = self.contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of department
        if self.department:
            _dict['department'] = self.department.to_dict()
        # override the default output from pydantic by calling `to_dict()` of item
        if self.item:
            _dict['item'] = self.item.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of priority
        if self.priority:
            _dict['priority'] = self.priority.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_location
        if self.service_location:
            _dict['serviceLocation'] = self.service_location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of site
        if self.site:
            _dict['site'] = self.site.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subtype
        if self.subtype:
            _dict['subtype'] = self.subtype.to_dict()
        # override the default output from pydantic by calling `to_dict()` of team
        if self.team:
            _dict['team'] = self.team.to_dict()
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        # set to None if assigned_notify_flag (nullable) is None
        # and model_fields_set contains the field
        if self.assigned_notify_flag is None and "assigned_notify_flag" in self.model_fields_set:
            _dict['assignedNotifyFlag'] = None

        # set to None if attach_schedule_to_new_service_flag (nullable) is None
        # and model_fields_set contains the field
        if self.attach_schedule_to_new_service_flag is None and "attach_schedule_to_new_service_flag" in self.model_fields_set:
            _dict['attachScheduleToNewServiceFlag'] = None

        # set to None if bill_complete_flag (nullable) is None
        # and model_fields_set contains the field
        if self.bill_complete_flag is None and "bill_complete_flag" in self.model_fields_set:
            _dict['billComplete_Flag'] = None

        # set to None if bill_service_separately_flag (nullable) is None
        # and model_fields_set contains the field
        if self.bill_service_separately_flag is None and "bill_service_separately_flag" in self.model_fields_set:
            _dict['billServiceSeparatelyFlag'] = None

        # set to None if bill_unapproved_time_and_expenses_flag (nullable) is None
        # and model_fields_set contains the field
        if self.bill_unapproved_time_and_expenses_flag is None and "bill_unapproved_time_and_expenses_flag" in self.model_fields_set:
            _dict['billUnapprovedTimeAndExpensesFlag'] = None

        # set to None if billing_amount (nullable) is None
        # and model_fields_set contains the field
        if self.billing_amount is None and "billing_amount" in self.model_fields_set:
            _dict['billingAmount'] = None

        # set to None if email_cc_flag (nullable) is None
        # and model_fields_set contains the field
        if self.email_cc_flag is None and "email_cc_flag" in self.model_fields_set:
            _dict['emailCCFlag'] = None

        # set to None if email_contact_flag (nullable) is None
        # and model_fields_set contains the field
        if self.email_contact_flag is None and "email_contact_flag" in self.model_fields_set:
            _dict['emailContactFlag'] = None

        # set to None if email_resource_flag (nullable) is None
        # and model_fields_set contains the field
        if self.email_resource_flag is None and "email_resource_flag" in self.model_fields_set:
            _dict['emailResourceFlag'] = None

        # set to None if expense_billable_flag (nullable) is None
        # and model_fields_set contains the field
        if self.expense_billable_flag is None and "expense_billable_flag" in self.model_fields_set:
            _dict['expenseBillableFlag'] = None

        # set to None if expense_invoice_flag (nullable) is None
        # and model_fields_set contains the field
        if self.expense_invoice_flag is None and "expense_invoice_flag" in self.model_fields_set:
            _dict['expenseInvoiceFlag'] = None

        # set to None if hours_budget (nullable) is None
        # and model_fields_set contains the field
        if self.hours_budget is None and "hours_budget" in self.model_fields_set:
            _dict['hoursBudget'] = None

        # set to None if override_flag (nullable) is None
        # and model_fields_set contains the field
        if self.override_flag is None and "override_flag" in self.model_fields_set:
            _dict['overrideFlag'] = None

        # set to None if product_invoice_flag (nullable) is None
        # and model_fields_set contains the field
        if self.product_invoice_flag is None and "product_invoice_flag" in self.model_fields_set:
            _dict['productInvoiceFlag'] = None

        # set to None if restrict_downpayment_flag (nullable) is None
        # and model_fields_set contains the field
        if self.restrict_downpayment_flag is None and "restrict_downpayment_flag" in self.model_fields_set:
            _dict['restrictDownpaymentFlag'] = None

        # set to None if schedule_days_before (nullable) is None
        # and model_fields_set contains the field
        if self.schedule_days_before is None and "schedule_days_before" in self.model_fields_set:
            _dict['scheduleDaysBefore'] = None

        # set to None if service_days_before (nullable) is None
        # and model_fields_set contains the field
        if self.service_days_before is None and "service_days_before" in self.model_fields_set:
            _dict['serviceDaysBefore'] = None

        # set to None if template_flag (nullable) is None
        # and model_fields_set contains the field
        if self.template_flag is None and "template_flag" in self.model_fields_set:
            _dict['templateFlag'] = None

        # set to None if time_billable_flag (nullable) is None
        # and model_fields_set contains the field
        if self.time_billable_flag is None and "time_billable_flag" in self.model_fields_set:
            _dict['timeBillableFlag'] = None

        # set to None if time_invoice_flag (nullable) is None
        # and model_fields_set contains the field
        if self.time_invoice_flag is None and "time_invoice_flag" in self.model_fields_set:
            _dict['timeInvoiceFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ServiceTemplate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ServiceTemplate) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "agreement": AgreementReference.from_dict(obj.get("agreement")) if obj.get("agreement") is not None else None,
            "assignedBy": MemberReference.from_dict(obj.get("assignedBy")) if obj.get("assignedBy") is not None else None,
            "assignedNotifyFlag": obj.get("assignedNotifyFlag"),
            "attachScheduleToNewServiceFlag": obj.get("attachScheduleToNewServiceFlag"),
            "billComplete_Flag": obj.get("billComplete_Flag"),
            "billServiceSeparatelyFlag": obj.get("billServiceSeparatelyFlag"),
            "billUnapprovedTimeAndExpensesFlag": obj.get("billUnapprovedTimeAndExpensesFlag"),
            "billingAmount": obj.get("billingAmount"),
            "billingMethod": obj.get("billingMethod"),
            "board": BoardReference.from_dict(obj.get("board")) if obj.get("board") is not None else None,
            "company": CompanyReference.from_dict(obj.get("company")) if obj.get("company") is not None else None,
            "contact": ContactReference.from_dict(obj.get("contact")) if obj.get("contact") is not None else None,
            "department": SystemDepartmentReference.from_dict(obj.get("department")) if obj.get("department") is not None else None,
            "emailCC": obj.get("emailCC"),
            "emailCCFlag": obj.get("emailCCFlag"),
            "emailContactFlag": obj.get("emailContactFlag"),
            "emailResourceFlag": obj.get("emailResourceFlag"),
            "expenseBillableFlag": obj.get("expenseBillableFlag"),
            "expenseInvoiceFlag": obj.get("expenseInvoiceFlag"),
            "hoursBudget": obj.get("hoursBudget"),
            "id": obj.get("id"),
            "impact": obj.get("impact"),
            "internalAnalysis": obj.get("internalAnalysis"),
            "item": ServiceItemReference.from_dict(obj.get("item")) if obj.get("item") is not None else None,
            "location": SystemLocationReference.from_dict(obj.get("location")) if obj.get("location") is not None else None,
            "name": obj.get("name"),
            "overrideFlag": obj.get("overrideFlag"),
            "priority": PriorityReference.from_dict(obj.get("priority")) if obj.get("priority") is not None else None,
            "problem": obj.get("problem"),
            "productInvoiceFlag": obj.get("productInvoiceFlag"),
            "purchaseOrderNumber": obj.get("purchaseOrderNumber"),
            "reference": obj.get("reference"),
            "restrictDownpaymentFlag": obj.get("restrictDownpaymentFlag"),
            "scheduleDaysBefore": obj.get("scheduleDaysBefore"),
            "serviceDaysBefore": obj.get("serviceDaysBefore"),
            "serviceLocation": ServiceLocationReference.from_dict(obj.get("serviceLocation")) if obj.get("serviceLocation") is not None else None,
            "severity": obj.get("severity"),
            "site": SiteReference.from_dict(obj.get("site")) if obj.get("site") is not None else None,
            "source": ServiceSourceReference.from_dict(obj.get("source")) if obj.get("source") is not None else None,
            "status": ServiceStatusReference.from_dict(obj.get("status")) if obj.get("status") is not None else None,
            "subtype": ServiceSubTypeReference.from_dict(obj.get("subtype")) if obj.get("subtype") is not None else None,
            "summary": obj.get("summary"),
            "team": ServiceTeamReference.from_dict(obj.get("team")) if obj.get("team") is not None else None,
            "templateFlag": obj.get("templateFlag"),
            "timeBillableFlag": obj.get("timeBillableFlag"),
            "timeInvoiceFlag": obj.get("timeInvoiceFlag"),
            "type": ServiceTypeReference.from_dict(obj.get("type")) if obj.get("type") is not None else None
        })
        return _obj

