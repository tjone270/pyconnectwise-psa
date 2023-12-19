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
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from connectwise_psa.models.member_reference import MemberReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ExpenseReport(BaseModel):
    """
    ExpenseReport
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    date_end: Optional[StrictStr] = Field(default=None, alias="dateEnd")
    date_start: Optional[StrictStr] = Field(default=None, alias="dateStart")
    due_date: Optional[StrictStr] = Field(default=None, alias="dueDate")
    id: Optional[StrictInt] = None
    member: Optional[MemberReference] = None
    period: Optional[StrictInt] = None
    status: Optional[StrictStr] = None
    total: Optional[Union[StrictFloat, StrictInt]] = None
    year: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["_info", "dateEnd", "dateStart", "dueDate", "id", "member", "period", "status", "total", "year"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Open', 'Rejected', 'PendingApproval', 'ErrorsCorrected', 'PendingProjectApproval', 'ApprovedByTierOne', 'RejectBySecondTier', 'ApprovedByTierTwo', 'ReadyToBill', 'Billed', 'WrittenOff', 'BilledAgreement'):
            raise ValueError("must be one of enum values ('Open', 'Rejected', 'PendingApproval', 'ErrorsCorrected', 'PendingProjectApproval', 'ApprovedByTierOne', 'RejectBySecondTier', 'ApprovedByTierTwo', 'ReadyToBill', 'Billed', 'WrittenOff', 'BilledAgreement')")
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
        """Create an instance of ExpenseReport from a JSON string"""
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
        # set to None if period (nullable) is None
        # and model_fields_set contains the field
        if self.period is None and "period" in self.model_fields_set:
            _dict['period'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        # set to None if year (nullable) is None
        # and model_fields_set contains the field
        if self.year is None and "year" in self.model_fields_set:
            _dict['year'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ExpenseReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ExpenseReport) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "dateEnd": obj.get("dateEnd"),
            "dateStart": obj.get("dateStart"),
            "dueDate": obj.get("dueDate"),
            "id": obj.get("id"),
            "member": MemberReference.from_dict(obj.get("member")) if obj.get("member") is not None else None,
            "period": obj.get("period"),
            "status": obj.get("status"),
            "total": obj.get("total"),
            "year": obj.get("year")
        })
        return _obj

