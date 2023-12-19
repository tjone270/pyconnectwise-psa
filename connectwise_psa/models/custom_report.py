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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CustomReport(BaseModel):
    """
    CustomReport
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    agreement_flag: Optional[StrictBool] = Field(default=None, alias="agreementFlag")
    agreement_override: Optional[StrictStr] = Field(default=None, alias="agreementOverride")
    agreement_param_id: Optional[StrictInt] = Field(default=None, description="Parameter unique identifier for the Custom Report's Agreement parameter.", alias="agreementParamId")
    agreement_type_flag: Optional[StrictBool] = Field(default=None, alias="agreementTypeFlag")
    agreement_type_override: Optional[StrictStr] = Field(default=None, alias="agreementTypeOverride")
    agreement_type_param_id: Optional[StrictInt] = Field(default=None, description="Parameter unique identifier for the Custom Report's Agreement Type parameter.", alias="agreementTypeParamId")
    company_flag: Optional[StrictBool] = Field(default=None, alias="companyFlag")
    company_override: Optional[StrictStr] = Field(default=None, alias="companyOverride")
    company_param_id: Optional[StrictInt] = Field(default=None, description="Parameter unique identifier for the Custom Report's Company parameter.", alias="companyParamId")
    department_default_flag: Optional[StrictBool] = Field(default=None, alias="departmentDefaultFlag")
    department_flag: Optional[StrictBool] = Field(default=None, alias="departmentFlag")
    department_override: Optional[StrictStr] = Field(default=None, alias="departmentOverride")
    department_param_id: Optional[StrictInt] = Field(default=None, description="Parameter unique identifier for the Custom Report's Department parameter.", alias="departmentParamId")
    description: StrictStr = Field(description=" Max length: 150;")
    end_date_flag: Optional[StrictBool] = Field(default=None, alias="endDateFlag")
    end_date_override: Optional[StrictStr] = Field(default=None, alias="endDateOverride")
    end_date_param_id: Optional[StrictInt] = Field(default=None, description="Parameter unique identifier for the Custom Report's End Date parameter.", alias="endDateParamId")
    generated_flag: Optional[StrictBool] = Field(default=None, alias="generatedFlag")
    id: Optional[StrictInt] = None
    invoice_flag: Optional[StrictBool] = Field(default=None, alias="invoiceFlag")
    invoice_override: Optional[StrictStr] = Field(default=None, alias="invoiceOverride")
    invoice_param_id: Optional[StrictInt] = Field(default=None, description="Parameter unique identifier for the Custom Report's Invoice Type parameter.", alias="invoiceParamId")
    location_default_flag: Optional[StrictBool] = Field(default=None, alias="locationDefaultFlag")
    location_flag: Optional[StrictBool] = Field(default=None, alias="locationFlag")
    location_override: Optional[StrictStr] = Field(default=None, alias="locationOverride")
    location_param_id: Optional[StrictInt] = Field(default=None, description="Parameter unique identifier for the Custom Report's Location parameter.", alias="locationParamId")
    marketing_campaign_flag: Optional[StrictBool] = Field(default=None, alias="marketingCampaignFlag")
    marketing_campaign_override: Optional[StrictStr] = Field(default=None, alias="marketingCampaignOverride")
    marketing_campaign_param_id: Optional[StrictInt] = Field(default=None, description="Parameter unique identifier for the Custom Report's Marketing Campaign parameter.", alias="marketingCampaignParamId")
    member_flag: Optional[StrictBool] = Field(default=None, alias="memberFlag")
    member_override: Optional[StrictStr] = Field(default=None, alias="memberOverride")
    member_param_id: Optional[StrictInt] = Field(default=None, description="Parameter unique identifier for the Custom Report's Member parameter.", alias="memberParamId")
    module: Optional[StrictStr] = Field(description="The Module Name.")
    name: StrictStr = Field(description=" Max length: 100;")
    opp_type_flag: Optional[StrictBool] = Field(default=None, alias="oppTypeFlag")
    opp_type_override: Optional[StrictStr] = Field(default=None, alias="oppTypeOverride")
    opp_type_param_id: Optional[StrictInt] = Field(default=None, description="Parameter unique identifier for the Custom Report's Opportunity Type parameter.", alias="oppTypeParamId")
    opportunity_flag: Optional[StrictBool] = Field(default=None, alias="opportunityFlag")
    opportunity_override: Optional[StrictStr] = Field(default=None, alias="opportunityOverride")
    opportunity_param_id: Optional[StrictInt] = Field(default=None, description="Parameter unique identifier for the Custom Report's Opportunity parameter.", alias="opportunityParamId")
    parameter_name_separator: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="parameterNameSeparator")
    parameter_prefix: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="parameterPrefix")
    parameter_separator: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="parameterSeparator")
    parameter_suffix: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="parameterSuffix")
    project_flag: Optional[StrictBool] = Field(default=None, alias="projectFlag")
    project_override: Optional[StrictStr] = Field(default=None, alias="projectOverride")
    project_param_id: Optional[StrictInt] = Field(default=None, description="Parameter unique identifier for the Custom Report's Project parameter.", alias="projectParamId")
    project_type_flag: Optional[StrictBool] = Field(default=None, alias="projectTypeFlag")
    project_type_override: Optional[StrictStr] = Field(default=None, alias="projectTypeOverride")
    project_type_param_id: Optional[StrictInt] = Field(default=None, description="Parameter unique identifier for the Custom Report's Project Type parameter.", alias="projectTypeParamId")
    report_link: StrictStr = Field(alias="reportLink")
    service_board_default_flag: Optional[StrictBool] = Field(default=None, alias="serviceBoardDefaultFlag")
    service_board_flag: Optional[StrictBool] = Field(default=None, alias="serviceBoardFlag")
    service_board_override: Optional[StrictStr] = Field(default=None, alias="serviceBoardOverride")
    service_board_param_id: Optional[StrictInt] = Field(default=None, description="Parameter unique identifier for the Custom Report's Service Board parameter.", alias="serviceBoardParamId")
    service_status_flag: Optional[StrictBool] = Field(default=None, alias="serviceStatusFlag")
    service_status_override: Optional[StrictStr] = Field(default=None, alias="serviceStatusOverride")
    service_status_param_id: Optional[StrictInt] = Field(default=None, description="Parameter unique identifier for the Custom Report's Service Status parameter.", alias="serviceStatusParamId")
    service_type_flag: Optional[StrictBool] = Field(default=None, alias="serviceTypeFlag")
    service_type_override: Optional[StrictStr] = Field(default=None, alias="serviceTypeOverride")
    service_type_param_id: Optional[StrictInt] = Field(default=None, description="Parameter unique identifier for the Custom Report's Service Type parameter.", alias="serviceTypeParamId")
    start_date_flag: Optional[StrictBool] = Field(default=None, alias="startDateFlag")
    start_date_override: Optional[StrictStr] = Field(default=None, alias="startDateOverride")
    start_date_param_id: Optional[StrictInt] = Field(default=None, description="Parameter unique identifier for the Custom Report's Start Date parameter.", alias="startDateParamId")
    territory_default_flag: Optional[StrictBool] = Field(default=None, alias="territoryDefaultFlag")
    territory_flag: Optional[StrictBool] = Field(default=None, alias="territoryFlag")
    territory_override: Optional[StrictStr] = Field(default=None, alias="territoryOverride")
    territory_param_id: Optional[StrictInt] = Field(default=None, description="Parameter unique identifier for the Custom Report's Terriroty parameter.", alias="territoryParamId")
    work_role_flag: Optional[StrictBool] = Field(default=None, alias="workRoleFlag")
    work_role_override: Optional[StrictStr] = Field(default=None, alias="workRoleOverride")
    work_role_param_id: Optional[StrictInt] = Field(default=None, description="Parameter unique identifier for the Custom Report's Work Role parameter.", alias="workRoleParamId")
    work_type_flag: Optional[StrictBool] = Field(default=None, alias="workTypeFlag")
    work_type_override: Optional[StrictStr] = Field(default=None, alias="workTypeOverride")
    work_type_param_id: Optional[StrictInt] = Field(default=None, description="Parameter unique identifier for the Custom Report's Work Type parameter.", alias="workTypeParamId")
    __properties: ClassVar[List[str]] = ["_info", "agreementFlag", "agreementOverride", "agreementParamId", "agreementTypeFlag", "agreementTypeOverride", "agreementTypeParamId", "companyFlag", "companyOverride", "companyParamId", "departmentDefaultFlag", "departmentFlag", "departmentOverride", "departmentParamId", "description", "endDateFlag", "endDateOverride", "endDateParamId", "generatedFlag", "id", "invoiceFlag", "invoiceOverride", "invoiceParamId", "locationDefaultFlag", "locationFlag", "locationOverride", "locationParamId", "marketingCampaignFlag", "marketingCampaignOverride", "marketingCampaignParamId", "memberFlag", "memberOverride", "memberParamId", "module", "name", "oppTypeFlag", "oppTypeOverride", "oppTypeParamId", "opportunityFlag", "opportunityOverride", "opportunityParamId", "parameterNameSeparator", "parameterPrefix", "parameterSeparator", "parameterSuffix", "projectFlag", "projectOverride", "projectParamId", "projectTypeFlag", "projectTypeOverride", "projectTypeParamId", "reportLink", "serviceBoardDefaultFlag", "serviceBoardFlag", "serviceBoardOverride", "serviceBoardParamId", "serviceStatusFlag", "serviceStatusOverride", "serviceStatusParamId", "serviceTypeFlag", "serviceTypeOverride", "serviceTypeParamId", "startDateFlag", "startDateOverride", "startDateParamId", "territoryDefaultFlag", "territoryFlag", "territoryOverride", "territoryParamId", "workRoleFlag", "workRoleOverride", "workRoleParamId", "workTypeFlag", "workTypeOverride", "workTypeParamId"]

    @field_validator('module')
    def module_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Companies', 'Finance', 'Marketing', 'Procurement', 'Project', 'Sales', 'ServiceDesk', 'TimeExpense'):
            raise ValueError("must be one of enum values ('Companies', 'Finance', 'Marketing', 'Procurement', 'Project', 'Sales', 'ServiceDesk', 'TimeExpense')")
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
        """Create an instance of CustomReport from a JSON string"""
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
        # set to None if agreement_flag (nullable) is None
        # and model_fields_set contains the field
        if self.agreement_flag is None and "agreement_flag" in self.model_fields_set:
            _dict['agreementFlag'] = None

        # set to None if agreement_param_id (nullable) is None
        # and model_fields_set contains the field
        if self.agreement_param_id is None and "agreement_param_id" in self.model_fields_set:
            _dict['agreementParamId'] = None

        # set to None if agreement_type_flag (nullable) is None
        # and model_fields_set contains the field
        if self.agreement_type_flag is None and "agreement_type_flag" in self.model_fields_set:
            _dict['agreementTypeFlag'] = None

        # set to None if agreement_type_param_id (nullable) is None
        # and model_fields_set contains the field
        if self.agreement_type_param_id is None and "agreement_type_param_id" in self.model_fields_set:
            _dict['agreementTypeParamId'] = None

        # set to None if company_flag (nullable) is None
        # and model_fields_set contains the field
        if self.company_flag is None and "company_flag" in self.model_fields_set:
            _dict['companyFlag'] = None

        # set to None if company_param_id (nullable) is None
        # and model_fields_set contains the field
        if self.company_param_id is None and "company_param_id" in self.model_fields_set:
            _dict['companyParamId'] = None

        # set to None if department_default_flag (nullable) is None
        # and model_fields_set contains the field
        if self.department_default_flag is None and "department_default_flag" in self.model_fields_set:
            _dict['departmentDefaultFlag'] = None

        # set to None if department_flag (nullable) is None
        # and model_fields_set contains the field
        if self.department_flag is None and "department_flag" in self.model_fields_set:
            _dict['departmentFlag'] = None

        # set to None if department_param_id (nullable) is None
        # and model_fields_set contains the field
        if self.department_param_id is None and "department_param_id" in self.model_fields_set:
            _dict['departmentParamId'] = None

        # set to None if end_date_flag (nullable) is None
        # and model_fields_set contains the field
        if self.end_date_flag is None and "end_date_flag" in self.model_fields_set:
            _dict['endDateFlag'] = None

        # set to None if end_date_param_id (nullable) is None
        # and model_fields_set contains the field
        if self.end_date_param_id is None and "end_date_param_id" in self.model_fields_set:
            _dict['endDateParamId'] = None

        # set to None if generated_flag (nullable) is None
        # and model_fields_set contains the field
        if self.generated_flag is None and "generated_flag" in self.model_fields_set:
            _dict['generatedFlag'] = None

        # set to None if invoice_flag (nullable) is None
        # and model_fields_set contains the field
        if self.invoice_flag is None and "invoice_flag" in self.model_fields_set:
            _dict['invoiceFlag'] = None

        # set to None if invoice_param_id (nullable) is None
        # and model_fields_set contains the field
        if self.invoice_param_id is None and "invoice_param_id" in self.model_fields_set:
            _dict['invoiceParamId'] = None

        # set to None if location_default_flag (nullable) is None
        # and model_fields_set contains the field
        if self.location_default_flag is None and "location_default_flag" in self.model_fields_set:
            _dict['locationDefaultFlag'] = None

        # set to None if location_flag (nullable) is None
        # and model_fields_set contains the field
        if self.location_flag is None and "location_flag" in self.model_fields_set:
            _dict['locationFlag'] = None

        # set to None if location_param_id (nullable) is None
        # and model_fields_set contains the field
        if self.location_param_id is None and "location_param_id" in self.model_fields_set:
            _dict['locationParamId'] = None

        # set to None if marketing_campaign_flag (nullable) is None
        # and model_fields_set contains the field
        if self.marketing_campaign_flag is None and "marketing_campaign_flag" in self.model_fields_set:
            _dict['marketingCampaignFlag'] = None

        # set to None if marketing_campaign_param_id (nullable) is None
        # and model_fields_set contains the field
        if self.marketing_campaign_param_id is None and "marketing_campaign_param_id" in self.model_fields_set:
            _dict['marketingCampaignParamId'] = None

        # set to None if member_flag (nullable) is None
        # and model_fields_set contains the field
        if self.member_flag is None and "member_flag" in self.model_fields_set:
            _dict['memberFlag'] = None

        # set to None if member_param_id (nullable) is None
        # and model_fields_set contains the field
        if self.member_param_id is None and "member_param_id" in self.model_fields_set:
            _dict['memberParamId'] = None

        # set to None if module (nullable) is None
        # and model_fields_set contains the field
        if self.module is None and "module" in self.model_fields_set:
            _dict['module'] = None

        # set to None if opp_type_flag (nullable) is None
        # and model_fields_set contains the field
        if self.opp_type_flag is None and "opp_type_flag" in self.model_fields_set:
            _dict['oppTypeFlag'] = None

        # set to None if opp_type_param_id (nullable) is None
        # and model_fields_set contains the field
        if self.opp_type_param_id is None and "opp_type_param_id" in self.model_fields_set:
            _dict['oppTypeParamId'] = None

        # set to None if opportunity_flag (nullable) is None
        # and model_fields_set contains the field
        if self.opportunity_flag is None and "opportunity_flag" in self.model_fields_set:
            _dict['opportunityFlag'] = None

        # set to None if opportunity_param_id (nullable) is None
        # and model_fields_set contains the field
        if self.opportunity_param_id is None and "opportunity_param_id" in self.model_fields_set:
            _dict['opportunityParamId'] = None

        # set to None if project_flag (nullable) is None
        # and model_fields_set contains the field
        if self.project_flag is None and "project_flag" in self.model_fields_set:
            _dict['projectFlag'] = None

        # set to None if project_param_id (nullable) is None
        # and model_fields_set contains the field
        if self.project_param_id is None and "project_param_id" in self.model_fields_set:
            _dict['projectParamId'] = None

        # set to None if project_type_flag (nullable) is None
        # and model_fields_set contains the field
        if self.project_type_flag is None and "project_type_flag" in self.model_fields_set:
            _dict['projectTypeFlag'] = None

        # set to None if project_type_param_id (nullable) is None
        # and model_fields_set contains the field
        if self.project_type_param_id is None and "project_type_param_id" in self.model_fields_set:
            _dict['projectTypeParamId'] = None

        # set to None if service_board_default_flag (nullable) is None
        # and model_fields_set contains the field
        if self.service_board_default_flag is None and "service_board_default_flag" in self.model_fields_set:
            _dict['serviceBoardDefaultFlag'] = None

        # set to None if service_board_flag (nullable) is None
        # and model_fields_set contains the field
        if self.service_board_flag is None and "service_board_flag" in self.model_fields_set:
            _dict['serviceBoardFlag'] = None

        # set to None if service_board_param_id (nullable) is None
        # and model_fields_set contains the field
        if self.service_board_param_id is None and "service_board_param_id" in self.model_fields_set:
            _dict['serviceBoardParamId'] = None

        # set to None if service_status_flag (nullable) is None
        # and model_fields_set contains the field
        if self.service_status_flag is None and "service_status_flag" in self.model_fields_set:
            _dict['serviceStatusFlag'] = None

        # set to None if service_status_param_id (nullable) is None
        # and model_fields_set contains the field
        if self.service_status_param_id is None and "service_status_param_id" in self.model_fields_set:
            _dict['serviceStatusParamId'] = None

        # set to None if service_type_flag (nullable) is None
        # and model_fields_set contains the field
        if self.service_type_flag is None and "service_type_flag" in self.model_fields_set:
            _dict['serviceTypeFlag'] = None

        # set to None if service_type_param_id (nullable) is None
        # and model_fields_set contains the field
        if self.service_type_param_id is None and "service_type_param_id" in self.model_fields_set:
            _dict['serviceTypeParamId'] = None

        # set to None if start_date_flag (nullable) is None
        # and model_fields_set contains the field
        if self.start_date_flag is None and "start_date_flag" in self.model_fields_set:
            _dict['startDateFlag'] = None

        # set to None if start_date_param_id (nullable) is None
        # and model_fields_set contains the field
        if self.start_date_param_id is None and "start_date_param_id" in self.model_fields_set:
            _dict['startDateParamId'] = None

        # set to None if territory_default_flag (nullable) is None
        # and model_fields_set contains the field
        if self.territory_default_flag is None and "territory_default_flag" in self.model_fields_set:
            _dict['territoryDefaultFlag'] = None

        # set to None if territory_flag (nullable) is None
        # and model_fields_set contains the field
        if self.territory_flag is None and "territory_flag" in self.model_fields_set:
            _dict['territoryFlag'] = None

        # set to None if territory_param_id (nullable) is None
        # and model_fields_set contains the field
        if self.territory_param_id is None and "territory_param_id" in self.model_fields_set:
            _dict['territoryParamId'] = None

        # set to None if work_role_flag (nullable) is None
        # and model_fields_set contains the field
        if self.work_role_flag is None and "work_role_flag" in self.model_fields_set:
            _dict['workRoleFlag'] = None

        # set to None if work_role_param_id (nullable) is None
        # and model_fields_set contains the field
        if self.work_role_param_id is None and "work_role_param_id" in self.model_fields_set:
            _dict['workRoleParamId'] = None

        # set to None if work_type_flag (nullable) is None
        # and model_fields_set contains the field
        if self.work_type_flag is None and "work_type_flag" in self.model_fields_set:
            _dict['workTypeFlag'] = None

        # set to None if work_type_param_id (nullable) is None
        # and model_fields_set contains the field
        if self.work_type_param_id is None and "work_type_param_id" in self.model_fields_set:
            _dict['workTypeParamId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CustomReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in CustomReport) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "agreementFlag": obj.get("agreementFlag"),
            "agreementOverride": obj.get("agreementOverride"),
            "agreementParamId": obj.get("agreementParamId"),
            "agreementTypeFlag": obj.get("agreementTypeFlag"),
            "agreementTypeOverride": obj.get("agreementTypeOverride"),
            "agreementTypeParamId": obj.get("agreementTypeParamId"),
            "companyFlag": obj.get("companyFlag"),
            "companyOverride": obj.get("companyOverride"),
            "companyParamId": obj.get("companyParamId"),
            "departmentDefaultFlag": obj.get("departmentDefaultFlag"),
            "departmentFlag": obj.get("departmentFlag"),
            "departmentOverride": obj.get("departmentOverride"),
            "departmentParamId": obj.get("departmentParamId"),
            "description": obj.get("description"),
            "endDateFlag": obj.get("endDateFlag"),
            "endDateOverride": obj.get("endDateOverride"),
            "endDateParamId": obj.get("endDateParamId"),
            "generatedFlag": obj.get("generatedFlag"),
            "id": obj.get("id"),
            "invoiceFlag": obj.get("invoiceFlag"),
            "invoiceOverride": obj.get("invoiceOverride"),
            "invoiceParamId": obj.get("invoiceParamId"),
            "locationDefaultFlag": obj.get("locationDefaultFlag"),
            "locationFlag": obj.get("locationFlag"),
            "locationOverride": obj.get("locationOverride"),
            "locationParamId": obj.get("locationParamId"),
            "marketingCampaignFlag": obj.get("marketingCampaignFlag"),
            "marketingCampaignOverride": obj.get("marketingCampaignOverride"),
            "marketingCampaignParamId": obj.get("marketingCampaignParamId"),
            "memberFlag": obj.get("memberFlag"),
            "memberOverride": obj.get("memberOverride"),
            "memberParamId": obj.get("memberParamId"),
            "module": obj.get("module"),
            "name": obj.get("name"),
            "oppTypeFlag": obj.get("oppTypeFlag"),
            "oppTypeOverride": obj.get("oppTypeOverride"),
            "oppTypeParamId": obj.get("oppTypeParamId"),
            "opportunityFlag": obj.get("opportunityFlag"),
            "opportunityOverride": obj.get("opportunityOverride"),
            "opportunityParamId": obj.get("opportunityParamId"),
            "parameterNameSeparator": obj.get("parameterNameSeparator"),
            "parameterPrefix": obj.get("parameterPrefix"),
            "parameterSeparator": obj.get("parameterSeparator"),
            "parameterSuffix": obj.get("parameterSuffix"),
            "projectFlag": obj.get("projectFlag"),
            "projectOverride": obj.get("projectOverride"),
            "projectParamId": obj.get("projectParamId"),
            "projectTypeFlag": obj.get("projectTypeFlag"),
            "projectTypeOverride": obj.get("projectTypeOverride"),
            "projectTypeParamId": obj.get("projectTypeParamId"),
            "reportLink": obj.get("reportLink"),
            "serviceBoardDefaultFlag": obj.get("serviceBoardDefaultFlag"),
            "serviceBoardFlag": obj.get("serviceBoardFlag"),
            "serviceBoardOverride": obj.get("serviceBoardOverride"),
            "serviceBoardParamId": obj.get("serviceBoardParamId"),
            "serviceStatusFlag": obj.get("serviceStatusFlag"),
            "serviceStatusOverride": obj.get("serviceStatusOverride"),
            "serviceStatusParamId": obj.get("serviceStatusParamId"),
            "serviceTypeFlag": obj.get("serviceTypeFlag"),
            "serviceTypeOverride": obj.get("serviceTypeOverride"),
            "serviceTypeParamId": obj.get("serviceTypeParamId"),
            "startDateFlag": obj.get("startDateFlag"),
            "startDateOverride": obj.get("startDateOverride"),
            "startDateParamId": obj.get("startDateParamId"),
            "territoryDefaultFlag": obj.get("territoryDefaultFlag"),
            "territoryFlag": obj.get("territoryFlag"),
            "territoryOverride": obj.get("territoryOverride"),
            "territoryParamId": obj.get("territoryParamId"),
            "workRoleFlag": obj.get("workRoleFlag"),
            "workRoleOverride": obj.get("workRoleOverride"),
            "workRoleParamId": obj.get("workRoleParamId"),
            "workTypeFlag": obj.get("workTypeFlag"),
            "workTypeOverride": obj.get("workTypeOverride"),
            "workTypeParamId": obj.get("workTypeParamId")
        })
        return _obj


