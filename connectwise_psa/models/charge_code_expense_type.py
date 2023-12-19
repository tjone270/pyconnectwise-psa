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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from connectwise_psa.models.charge_code_reference import ChargeCodeReference
from connectwise_psa.models.expense_type_reference import ExpenseTypeReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ChargeCodeExpenseType(BaseModel):
    """
    ChargeCodeExpenseType
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    charge_code: Optional[ChargeCodeReference] = Field(default=None, alias="chargeCode")
    id: Optional[StrictInt] = None
    type: Optional[ExpenseTypeReference] = None
    __properties: ClassVar[List[str]] = ["_info", "chargeCode", "id", "type"]

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
        """Create an instance of ChargeCodeExpenseType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of charge_code
        if self.charge_code:
            _dict['chargeCode'] = self.charge_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ChargeCodeExpenseType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ChargeCodeExpenseType) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "chargeCode": ChargeCodeReference.from_dict(obj.get("chargeCode")) if obj.get("chargeCode") is not None else None,
            "id": obj.get("id"),
            "type": ExpenseTypeReference.from_dict(obj.get("type")) if obj.get("type") is not None else None
        })
        return _obj

