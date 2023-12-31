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
from connectwise_psa.models.company_reference import CompanyReference
from connectwise_psa.models.system_department_reference import SystemDepartmentReference
from connectwise_psa.models.system_location_reference import SystemLocationReference
from connectwise_psa.models.work_role_reference import WorkRoleReference
from connectwise_psa.models.work_type_reference import WorkTypeReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ChargeCode(BaseModel):
    """
    ChargeCode
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    allow_all_expense_type_flag: Optional[StrictBool] = Field(default=None, alias="allowAllExpenseTypeFlag")
    bill_time: Optional[StrictStr] = Field(default=None, alias="billTime")
    company: Optional[CompanyReference] = None
    department: Optional[SystemDepartmentReference] = None
    expense_entry_flag: Optional[StrictBool] = Field(default=None, alias="expenseEntryFlag")
    expense_type_ids: Optional[List[StrictInt]] = Field(default=None, alias="expenseTypeIds")
    id: Optional[StrictInt] = None
    integration_xref: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="integrationXref")
    location: Optional[SystemLocationReference] = None
    name: StrictStr = Field(description=" Max length: 50;")
    time_entry_flag: Optional[StrictBool] = Field(default=None, alias="timeEntryFlag")
    work_role: Optional[WorkRoleReference] = Field(default=None, alias="workRole")
    work_type: Optional[WorkTypeReference] = Field(default=None, alias="workType")
    __properties: ClassVar[List[str]] = ["_info", "allowAllExpenseTypeFlag", "billTime", "company", "department", "expenseEntryFlag", "expenseTypeIds", "id", "integrationXref", "location", "name", "timeEntryFlag", "workRole", "workType"]

    @field_validator('bill_time')
    def bill_time_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Billable', 'DoNotBill', 'NoCharge', 'NoDefault'):
            raise ValueError("must be one of enum values ('Billable', 'DoNotBill', 'NoCharge', 'NoDefault')")
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
        """Create an instance of ChargeCode from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of company
        if self.company:
            _dict['company'] = self.company.to_dict()
        # override the default output from pydantic by calling `to_dict()` of department
        if self.department:
            _dict['department'] = self.department.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of work_role
        if self.work_role:
            _dict['workRole'] = self.work_role.to_dict()
        # override the default output from pydantic by calling `to_dict()` of work_type
        if self.work_type:
            _dict['workType'] = self.work_type.to_dict()
        # set to None if allow_all_expense_type_flag (nullable) is None
        # and model_fields_set contains the field
        if self.allow_all_expense_type_flag is None and "allow_all_expense_type_flag" in self.model_fields_set:
            _dict['allowAllExpenseTypeFlag'] = None

        # set to None if bill_time (nullable) is None
        # and model_fields_set contains the field
        if self.bill_time is None and "bill_time" in self.model_fields_set:
            _dict['billTime'] = None

        # set to None if expense_entry_flag (nullable) is None
        # and model_fields_set contains the field
        if self.expense_entry_flag is None and "expense_entry_flag" in self.model_fields_set:
            _dict['expenseEntryFlag'] = None

        # set to None if time_entry_flag (nullable) is None
        # and model_fields_set contains the field
        if self.time_entry_flag is None and "time_entry_flag" in self.model_fields_set:
            _dict['timeEntryFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ChargeCode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ChargeCode) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "allowAllExpenseTypeFlag": obj.get("allowAllExpenseTypeFlag"),
            "billTime": obj.get("billTime"),
            "company": CompanyReference.from_dict(obj.get("company")) if obj.get("company") is not None else None,
            "department": SystemDepartmentReference.from_dict(obj.get("department")) if obj.get("department") is not None else None,
            "expenseEntryFlag": obj.get("expenseEntryFlag"),
            "expenseTypeIds": obj.get("expenseTypeIds"),
            "id": obj.get("id"),
            "integrationXref": obj.get("integrationXref"),
            "location": SystemLocationReference.from_dict(obj.get("location")) if obj.get("location") is not None else None,
            "name": obj.get("name"),
            "timeEntryFlag": obj.get("timeEntryFlag"),
            "workRole": WorkRoleReference.from_dict(obj.get("workRole")) if obj.get("workRole") is not None else None,
            "workType": WorkTypeReference.from_dict(obj.get("workType")) if obj.get("workType") is not None else None
        })
        return _obj


