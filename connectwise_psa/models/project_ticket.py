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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from connectwise_psa.models.agreement_reference import AgreementReference
from connectwise_psa.models.board_reference import BoardReference
from connectwise_psa.models.company_reference import CompanyReference
from connectwise_psa.models.contact_reference import ContactReference
from connectwise_psa.models.country_reference import CountryReference
from connectwise_psa.models.currency_reference import CurrencyReference
from connectwise_psa.models.custom_field_value import CustomFieldValue
from connectwise_psa.models.member_reference import MemberReference
from connectwise_psa.models.opportunity_reference import OpportunityReference
from connectwise_psa.models.priority_reference import PriorityReference
from connectwise_psa.models.project_phase_reference import ProjectPhaseReference
from connectwise_psa.models.project_reference import ProjectReference
from connectwise_psa.models.service_item_reference import ServiceItemReference
from connectwise_psa.models.service_location_reference import ServiceLocationReference
from connectwise_psa.models.service_source_reference import ServiceSourceReference
from connectwise_psa.models.service_status_reference import ServiceStatusReference
from connectwise_psa.models.service_sub_type_reference import ServiceSubTypeReference
from connectwise_psa.models.service_type_reference import ServiceTypeReference
from connectwise_psa.models.site_reference import SiteReference
from connectwise_psa.models.system_department_reference import SystemDepartmentReference
from connectwise_psa.models.system_location_reference import SystemLocationReference
from connectwise_psa.models.ticket_task import TicketTask
from connectwise_psa.models.work_role_reference import WorkRoleReference
from connectwise_psa.models.work_type_reference import WorkTypeReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ProjectTicket(BaseModel):
    """
    ProjectTicket
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    actual_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="actualHours")
    address_line1: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="addressLine1")
    address_line2: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="addressLine2")
    agreement: Optional[AgreementReference] = None
    allow_all_clients_portal_view: Optional[StrictBool] = Field(default=None, alias="allowAllClientsPortalView")
    approved: Optional[StrictBool] = None
    automatic_email_cc: Optional[StrictStr] = Field(default=None, description=" Max length: 1000;", alias="automaticEmailCc")
    automatic_email_cc_flag: Optional[StrictBool] = Field(default=None, alias="automaticEmailCcFlag")
    automatic_email_contact_flag: Optional[StrictBool] = Field(default=None, alias="automaticEmailContactFlag")
    automatic_email_resource_flag: Optional[StrictBool] = Field(default=None, alias="automaticEmailResourceFlag")
    bill_expenses: Optional[StrictStr] = Field(default=None, alias="billExpenses")
    bill_products: Optional[StrictStr] = Field(default=None, alias="billProducts")
    bill_time: Optional[StrictStr] = Field(default=None, alias="billTime")
    board: Optional[BoardReference] = None
    budget_hours: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="budgetHours")
    city: Optional[StrictStr] = Field(default=None, description=" Max length: 50;")
    closed_by: Optional[StrictStr] = Field(default=None, alias="closedBy")
    closed_date: Optional[StrictStr] = Field(default=None, alias="closedDate")
    closed_flag: Optional[StrictBool] = Field(default=None, alias="closedFlag")
    company: Optional[CompanyReference] = None
    contact: Optional[ContactReference] = None
    contact_email_address: Optional[StrictStr] = Field(default=None, description=" Max length: 250;", alias="contactEmailAddress")
    contact_email_lookup: Optional[StrictStr] = Field(default=None, alias="contactEmailLookup")
    contact_name: Optional[StrictStr] = Field(default=None, description=" Max length: 62;", alias="contactName")
    contact_phone_extension: Optional[StrictStr] = Field(default=None, description=" Max length: 15;", alias="contactPhoneExtension")
    contact_phone_number: Optional[StrictStr] = Field(default=None, description=" Max length: 20;", alias="contactPhoneNumber")
    country: Optional[CountryReference] = None
    currency: Optional[CurrencyReference] = None
    custom_fields: Optional[List[CustomFieldValue]] = Field(default=None, alias="customFields")
    customer_updated_flag: Optional[StrictBool] = Field(default=None, alias="customerUpdatedFlag")
    department: Optional[SystemDepartmentReference] = None
    duration: Optional[StrictInt] = None
    estimated_start_date: Optional[datetime] = Field(default=None, alias="estimatedStartDate")
    id: Optional[StrictInt] = None
    initial_description: Optional[StrictStr] = Field(default=None, description="Only available for POST, will not be returned in the response.", alias="initialDescription")
    initial_internal_analysis: Optional[StrictStr] = Field(default=None, description="Only available for POST, will not be returned in the response.", alias="initialInternalAnalysis")
    initial_resolution: Optional[StrictStr] = Field(default=None, description="Only available for POST, will not be returned in the response.", alias="initialResolution")
    is_issue_flag: Optional[StrictBool] = Field(default=None, alias="isIssueFlag")
    item: Optional[ServiceItemReference] = None
    knowledge_base_category_id: Optional[StrictInt] = Field(default=None, alias="knowledgeBaseCategoryId")
    knowledge_base_link_id: Optional[StrictInt] = Field(default=None, alias="knowledgeBaseLinkId")
    knowledge_base_link_type: Optional[StrictStr] = Field(default=None, alias="knowledgeBaseLinkType")
    knowledge_base_sub_category_id: Optional[StrictInt] = Field(default=None, alias="knowledgeBaseSubCategoryId")
    lag_days: Optional[StrictInt] = Field(default=None, alias="lagDays")
    lag_nonworking_days_flag: Optional[StrictBool] = Field(default=None, alias="lagNonworkingDaysFlag")
    location: Optional[SystemLocationReference] = None
    mobile_guid: Optional[StrictStr] = Field(default=None, alias="mobileGuid")
    opportunity: Optional[OpportunityReference] = None
    owner: Optional[MemberReference] = None
    phase: Optional[ProjectPhaseReference] = None
    predecessor_closed_flag: Optional[StrictBool] = Field(default=None, alias="predecessorClosedFlag")
    predecessor_id: Optional[StrictInt] = Field(default=None, alias="predecessorId")
    predecessor_type: Optional[StrictStr] = Field(default=None, alias="predecessorType")
    priority: Optional[PriorityReference] = None
    process_notifications: Optional[StrictBool] = Field(default=None, description="Can be set to false to skip notification processing when adding or updating a ticket (Defaults to True).", alias="processNotifications")
    project: Optional[ProjectReference] = None
    required_date: Optional[datetime] = Field(default=None, alias="requiredDate")
    resources: Optional[StrictStr] = None
    service_location: Optional[ServiceLocationReference] = Field(default=None, alias="serviceLocation")
    site: Optional[SiteReference] = None
    site_name: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="siteName")
    skip_callback: Optional[StrictBool] = Field(default=None, alias="skipCallback")
    source: Optional[ServiceSourceReference] = None
    state_identifier: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="stateIdentifier")
    status: Optional[ServiceStatusReference] = None
    sub_billing_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="subBillingAmount")
    sub_billing_method: Optional[StrictStr] = Field(default=None, alias="subBillingMethod")
    sub_date_accepted: Optional[StrictStr] = Field(default=None, alias="subDateAccepted")
    sub_type: Optional[ServiceSubTypeReference] = Field(default=None, alias="subType")
    summary: StrictStr = Field(description=" Max length: 100;")
    tasks: Optional[List[TicketTask]] = None
    type: Optional[ServiceTypeReference] = None
    wbs_code: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="wbsCode")
    work_role: Optional[WorkRoleReference] = Field(default=None, alias="workRole")
    work_type: Optional[WorkTypeReference] = Field(default=None, alias="workType")
    zip: Optional[StrictStr] = Field(default=None, description=" Max length: 12;")
    __properties: ClassVar[List[str]] = ["_info", "actualHours", "addressLine1", "addressLine2", "agreement", "allowAllClientsPortalView", "approved", "automaticEmailCc", "automaticEmailCcFlag", "automaticEmailContactFlag", "automaticEmailResourceFlag", "billExpenses", "billProducts", "billTime", "board", "budgetHours", "city", "closedBy", "closedDate", "closedFlag", "company", "contact", "contactEmailAddress", "contactEmailLookup", "contactName", "contactPhoneExtension", "contactPhoneNumber", "country", "currency", "customFields", "customerUpdatedFlag", "department", "duration", "estimatedStartDate", "id", "initialDescription", "initialInternalAnalysis", "initialResolution", "isIssueFlag", "item", "knowledgeBaseCategoryId", "knowledgeBaseLinkId", "knowledgeBaseLinkType", "knowledgeBaseSubCategoryId", "lagDays", "lagNonworkingDaysFlag", "location", "mobileGuid", "opportunity", "owner", "phase", "predecessorClosedFlag", "predecessorId", "predecessorType", "priority", "processNotifications", "project", "requiredDate", "resources", "serviceLocation", "site", "siteName", "skipCallback", "source", "stateIdentifier", "status", "subBillingAmount", "subBillingMethod", "subDateAccepted", "subType", "summary", "tasks", "type", "wbsCode", "workRole", "workType", "zip"]

    @field_validator('bill_expenses')
    def bill_expenses_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Billable', 'DoNotBill', 'NoCharge', 'NoDefault'):
            raise ValueError("must be one of enum values ('Billable', 'DoNotBill', 'NoCharge', 'NoDefault')")
        return value

    @field_validator('bill_products')
    def bill_products_validate_enum(cls, value):
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

    @field_validator('knowledge_base_link_type')
    def knowledge_base_link_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Activity', 'ProjectIssue', 'KnowledgeBaseArticle', 'ProjectTicket', 'ServiceTicket', 'Time'):
            raise ValueError("must be one of enum values ('Activity', 'ProjectIssue', 'KnowledgeBaseArticle', 'ProjectTicket', 'ServiceTicket', 'Time')")
        return value

    @field_validator('predecessor_type')
    def predecessor_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Ticket', 'Phase'):
            raise ValueError("must be one of enum values ('Ticket', 'Phase')")
        return value

    @field_validator('sub_billing_method')
    def sub_billing_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ActualRates', 'FixedFee', 'NotToExceed', 'OverrideRate'):
            raise ValueError("must be one of enum values ('ActualRates', 'FixedFee', 'NotToExceed', 'OverrideRate')")
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
        """Create an instance of ProjectTicket from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of board
        if self.board:
            _dict['board'] = self.board.to_dict()
        # override the default output from pydantic by calling `to_dict()` of company
        if self.company:
            _dict['company'] = self.company.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contact
        if self.contact:
            _dict['contact'] = self.contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of country
        if self.country:
            _dict['country'] = self.country.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency
        if self.currency:
            _dict['currency'] = self.currency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in custom_fields (list)
        _items = []
        if self.custom_fields:
            for _item in self.custom_fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customFields'] = _items
        # override the default output from pydantic by calling `to_dict()` of department
        if self.department:
            _dict['department'] = self.department.to_dict()
        # override the default output from pydantic by calling `to_dict()` of item
        if self.item:
            _dict['item'] = self.item.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of opportunity
        if self.opportunity:
            _dict['opportunity'] = self.opportunity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of phase
        if self.phase:
            _dict['phase'] = self.phase.to_dict()
        # override the default output from pydantic by calling `to_dict()` of priority
        if self.priority:
            _dict['priority'] = self.priority.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of sub_type
        if self.sub_type:
            _dict['subType'] = self.sub_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tasks (list)
        _items = []
        if self.tasks:
            for _item in self.tasks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tasks'] = _items
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of work_role
        if self.work_role:
            _dict['workRole'] = self.work_role.to_dict()
        # override the default output from pydantic by calling `to_dict()` of work_type
        if self.work_type:
            _dict['workType'] = self.work_type.to_dict()
        # set to None if actual_hours (nullable) is None
        # and model_fields_set contains the field
        if self.actual_hours is None and "actual_hours" in self.model_fields_set:
            _dict['actualHours'] = None

        # set to None if allow_all_clients_portal_view (nullable) is None
        # and model_fields_set contains the field
        if self.allow_all_clients_portal_view is None and "allow_all_clients_portal_view" in self.model_fields_set:
            _dict['allowAllClientsPortalView'] = None

        # set to None if approved (nullable) is None
        # and model_fields_set contains the field
        if self.approved is None and "approved" in self.model_fields_set:
            _dict['approved'] = None

        # set to None if automatic_email_cc_flag (nullable) is None
        # and model_fields_set contains the field
        if self.automatic_email_cc_flag is None and "automatic_email_cc_flag" in self.model_fields_set:
            _dict['automaticEmailCcFlag'] = None

        # set to None if automatic_email_contact_flag (nullable) is None
        # and model_fields_set contains the field
        if self.automatic_email_contact_flag is None and "automatic_email_contact_flag" in self.model_fields_set:
            _dict['automaticEmailContactFlag'] = None

        # set to None if automatic_email_resource_flag (nullable) is None
        # and model_fields_set contains the field
        if self.automatic_email_resource_flag is None and "automatic_email_resource_flag" in self.model_fields_set:
            _dict['automaticEmailResourceFlag'] = None

        # set to None if bill_expenses (nullable) is None
        # and model_fields_set contains the field
        if self.bill_expenses is None and "bill_expenses" in self.model_fields_set:
            _dict['billExpenses'] = None

        # set to None if bill_products (nullable) is None
        # and model_fields_set contains the field
        if self.bill_products is None and "bill_products" in self.model_fields_set:
            _dict['billProducts'] = None

        # set to None if bill_time (nullable) is None
        # and model_fields_set contains the field
        if self.bill_time is None and "bill_time" in self.model_fields_set:
            _dict['billTime'] = None

        # set to None if budget_hours (nullable) is None
        # and model_fields_set contains the field
        if self.budget_hours is None and "budget_hours" in self.model_fields_set:
            _dict['budgetHours'] = None

        # set to None if closed_flag (nullable) is None
        # and model_fields_set contains the field
        if self.closed_flag is None and "closed_flag" in self.model_fields_set:
            _dict['closedFlag'] = None

        # set to None if customer_updated_flag (nullable) is None
        # and model_fields_set contains the field
        if self.customer_updated_flag is None and "customer_updated_flag" in self.model_fields_set:
            _dict['customerUpdatedFlag'] = None

        # set to None if duration (nullable) is None
        # and model_fields_set contains the field
        if self.duration is None and "duration" in self.model_fields_set:
            _dict['duration'] = None

        # set to None if is_issue_flag (nullable) is None
        # and model_fields_set contains the field
        if self.is_issue_flag is None and "is_issue_flag" in self.model_fields_set:
            _dict['isIssueFlag'] = None

        # set to None if knowledge_base_category_id (nullable) is None
        # and model_fields_set contains the field
        if self.knowledge_base_category_id is None and "knowledge_base_category_id" in self.model_fields_set:
            _dict['knowledgeBaseCategoryId'] = None

        # set to None if knowledge_base_link_id (nullable) is None
        # and model_fields_set contains the field
        if self.knowledge_base_link_id is None and "knowledge_base_link_id" in self.model_fields_set:
            _dict['knowledgeBaseLinkId'] = None

        # set to None if knowledge_base_link_type (nullable) is None
        # and model_fields_set contains the field
        if self.knowledge_base_link_type is None and "knowledge_base_link_type" in self.model_fields_set:
            _dict['knowledgeBaseLinkType'] = None

        # set to None if knowledge_base_sub_category_id (nullable) is None
        # and model_fields_set contains the field
        if self.knowledge_base_sub_category_id is None and "knowledge_base_sub_category_id" in self.model_fields_set:
            _dict['knowledgeBaseSubCategoryId'] = None

        # set to None if lag_days (nullable) is None
        # and model_fields_set contains the field
        if self.lag_days is None and "lag_days" in self.model_fields_set:
            _dict['lagDays'] = None

        # set to None if lag_nonworking_days_flag (nullable) is None
        # and model_fields_set contains the field
        if self.lag_nonworking_days_flag is None and "lag_nonworking_days_flag" in self.model_fields_set:
            _dict['lagNonworkingDaysFlag'] = None

        # set to None if mobile_guid (nullable) is None
        # and model_fields_set contains the field
        if self.mobile_guid is None and "mobile_guid" in self.model_fields_set:
            _dict['mobileGuid'] = None

        # set to None if predecessor_closed_flag (nullable) is None
        # and model_fields_set contains the field
        if self.predecessor_closed_flag is None and "predecessor_closed_flag" in self.model_fields_set:
            _dict['predecessorClosedFlag'] = None

        # set to None if predecessor_id (nullable) is None
        # and model_fields_set contains the field
        if self.predecessor_id is None and "predecessor_id" in self.model_fields_set:
            _dict['predecessorId'] = None

        # set to None if predecessor_type (nullable) is None
        # and model_fields_set contains the field
        if self.predecessor_type is None and "predecessor_type" in self.model_fields_set:
            _dict['predecessorType'] = None

        # set to None if process_notifications (nullable) is None
        # and model_fields_set contains the field
        if self.process_notifications is None and "process_notifications" in self.model_fields_set:
            _dict['processNotifications'] = None

        # set to None if skip_callback (nullable) is None
        # and model_fields_set contains the field
        if self.skip_callback is None and "skip_callback" in self.model_fields_set:
            _dict['skipCallback'] = None

        # set to None if sub_billing_amount (nullable) is None
        # and model_fields_set contains the field
        if self.sub_billing_amount is None and "sub_billing_amount" in self.model_fields_set:
            _dict['subBillingAmount'] = None

        # set to None if sub_billing_method (nullable) is None
        # and model_fields_set contains the field
        if self.sub_billing_method is None and "sub_billing_method" in self.model_fields_set:
            _dict['subBillingMethod'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProjectTicket from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ProjectTicket) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "actualHours": obj.get("actualHours"),
            "addressLine1": obj.get("addressLine1"),
            "addressLine2": obj.get("addressLine2"),
            "agreement": AgreementReference.from_dict(obj.get("agreement")) if obj.get("agreement") is not None else None,
            "allowAllClientsPortalView": obj.get("allowAllClientsPortalView"),
            "approved": obj.get("approved"),
            "automaticEmailCc": obj.get("automaticEmailCc"),
            "automaticEmailCcFlag": obj.get("automaticEmailCcFlag"),
            "automaticEmailContactFlag": obj.get("automaticEmailContactFlag"),
            "automaticEmailResourceFlag": obj.get("automaticEmailResourceFlag"),
            "billExpenses": obj.get("billExpenses"),
            "billProducts": obj.get("billProducts"),
            "billTime": obj.get("billTime"),
            "board": BoardReference.from_dict(obj.get("board")) if obj.get("board") is not None else None,
            "budgetHours": obj.get("budgetHours"),
            "city": obj.get("city"),
            "closedBy": obj.get("closedBy"),
            "closedDate": obj.get("closedDate"),
            "closedFlag": obj.get("closedFlag"),
            "company": CompanyReference.from_dict(obj.get("company")) if obj.get("company") is not None else None,
            "contact": ContactReference.from_dict(obj.get("contact")) if obj.get("contact") is not None else None,
            "contactEmailAddress": obj.get("contactEmailAddress"),
            "contactEmailLookup": obj.get("contactEmailLookup"),
            "contactName": obj.get("contactName"),
            "contactPhoneExtension": obj.get("contactPhoneExtension"),
            "contactPhoneNumber": obj.get("contactPhoneNumber"),
            "country": CountryReference.from_dict(obj.get("country")) if obj.get("country") is not None else None,
            "currency": CurrencyReference.from_dict(obj.get("currency")) if obj.get("currency") is not None else None,
            "customFields": [CustomFieldValue.from_dict(_item) for _item in obj.get("customFields")] if obj.get("customFields") is not None else None,
            "customerUpdatedFlag": obj.get("customerUpdatedFlag"),
            "department": SystemDepartmentReference.from_dict(obj.get("department")) if obj.get("department") is not None else None,
            "duration": obj.get("duration"),
            "estimatedStartDate": obj.get("estimatedStartDate"),
            "id": obj.get("id"),
            "initialDescription": obj.get("initialDescription"),
            "initialInternalAnalysis": obj.get("initialInternalAnalysis"),
            "initialResolution": obj.get("initialResolution"),
            "isIssueFlag": obj.get("isIssueFlag"),
            "item": ServiceItemReference.from_dict(obj.get("item")) if obj.get("item") is not None else None,
            "knowledgeBaseCategoryId": obj.get("knowledgeBaseCategoryId"),
            "knowledgeBaseLinkId": obj.get("knowledgeBaseLinkId"),
            "knowledgeBaseLinkType": obj.get("knowledgeBaseLinkType"),
            "knowledgeBaseSubCategoryId": obj.get("knowledgeBaseSubCategoryId"),
            "lagDays": obj.get("lagDays"),
            "lagNonworkingDaysFlag": obj.get("lagNonworkingDaysFlag"),
            "location": SystemLocationReference.from_dict(obj.get("location")) if obj.get("location") is not None else None,
            "mobileGuid": obj.get("mobileGuid"),
            "opportunity": OpportunityReference.from_dict(obj.get("opportunity")) if obj.get("opportunity") is not None else None,
            "owner": MemberReference.from_dict(obj.get("owner")) if obj.get("owner") is not None else None,
            "phase": ProjectPhaseReference.from_dict(obj.get("phase")) if obj.get("phase") is not None else None,
            "predecessorClosedFlag": obj.get("predecessorClosedFlag"),
            "predecessorId": obj.get("predecessorId"),
            "predecessorType": obj.get("predecessorType"),
            "priority": PriorityReference.from_dict(obj.get("priority")) if obj.get("priority") is not None else None,
            "processNotifications": obj.get("processNotifications"),
            "project": ProjectReference.from_dict(obj.get("project")) if obj.get("project") is not None else None,
            "requiredDate": obj.get("requiredDate"),
            "resources": obj.get("resources"),
            "serviceLocation": ServiceLocationReference.from_dict(obj.get("serviceLocation")) if obj.get("serviceLocation") is not None else None,
            "site": SiteReference.from_dict(obj.get("site")) if obj.get("site") is not None else None,
            "siteName": obj.get("siteName"),
            "skipCallback": obj.get("skipCallback"),
            "source": ServiceSourceReference.from_dict(obj.get("source")) if obj.get("source") is not None else None,
            "stateIdentifier": obj.get("stateIdentifier"),
            "status": ServiceStatusReference.from_dict(obj.get("status")) if obj.get("status") is not None else None,
            "subBillingAmount": obj.get("subBillingAmount"),
            "subBillingMethod": obj.get("subBillingMethod"),
            "subDateAccepted": obj.get("subDateAccepted"),
            "subType": ServiceSubTypeReference.from_dict(obj.get("subType")) if obj.get("subType") is not None else None,
            "summary": obj.get("summary"),
            "tasks": [TicketTask.from_dict(_item) for _item in obj.get("tasks")] if obj.get("tasks") is not None else None,
            "type": ServiceTypeReference.from_dict(obj.get("type")) if obj.get("type") is not None else None,
            "wbsCode": obj.get("wbsCode"),
            "workRole": WorkRoleReference.from_dict(obj.get("workRole")) if obj.get("workRole") is not None else None,
            "workType": WorkTypeReference.from_dict(obj.get("workType")) if obj.get("workType") is not None else None,
            "zip": obj.get("zip")
        })
        return _obj

