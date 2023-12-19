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

class MemberAccrual(BaseModel):
    """
    MemberAccrual
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    accrual_type: Optional[StrictStr] = Field(alias="accrualType")
    hours: Optional[Union[StrictFloat, StrictInt]]
    id: Optional[StrictInt] = None
    member: Optional[MemberReference] = None
    reason: StrictStr
    year: Optional[StrictInt]
    __properties: ClassVar[List[str]] = ["_info", "accrualType", "hours", "id", "member", "reason", "year"]

    @field_validator('accrual_type')
    def accrual_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Holiday', 'PTO', 'Sick', 'Vacation'):
            raise ValueError("must be one of enum values ('Holiday', 'PTO', 'Sick', 'Vacation')")
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
        """Create an instance of MemberAccrual from a JSON string"""
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
        # set to None if accrual_type (nullable) is None
        # and model_fields_set contains the field
        if self.accrual_type is None and "accrual_type" in self.model_fields_set:
            _dict['accrualType'] = None

        # set to None if hours (nullable) is None
        # and model_fields_set contains the field
        if self.hours is None and "hours" in self.model_fields_set:
            _dict['hours'] = None

        # set to None if year (nullable) is None
        # and model_fields_set contains the field
        if self.year is None and "year" in self.model_fields_set:
            _dict['year'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of MemberAccrual from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in MemberAccrual) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "accrualType": obj.get("accrualType"),
            "hours": obj.get("hours"),
            "id": obj.get("id"),
            "member": MemberReference.from_dict(obj.get("member")) if obj.get("member") is not None else None,
            "reason": obj.get("reason"),
            "year": obj.get("year")
        })
        return _obj


