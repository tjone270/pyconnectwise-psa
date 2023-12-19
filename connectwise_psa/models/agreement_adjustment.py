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
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from connectwise_psa.models.custom_field_value import CustomFieldValue
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AgreementAdjustment(BaseModel):
    """
    AgreementAdjustment
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    agreement_id: Optional[StrictInt] = Field(default=None, alias="agreementId")
    amount: Optional[Union[StrictFloat, StrictInt]] = None
    custom_fields: Optional[List[CustomFieldValue]] = Field(default=None, alias="customFields")
    description: Optional[StrictStr] = Field(default=None, description=" Max length: 1000;")
    effective_date: Optional[datetime] = Field(default=None, alias="effectiveDate")
    id: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["_info", "agreementId", "amount", "customFields", "description", "effectiveDate", "id"]

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
        """Create an instance of AgreementAdjustment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in custom_fields (list)
        _items = []
        if self.custom_fields:
            for _item in self.custom_fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customFields'] = _items
        # set to None if agreement_id (nullable) is None
        # and model_fields_set contains the field
        if self.agreement_id is None and "agreement_id" in self.model_fields_set:
            _dict['agreementId'] = None

        # set to None if amount (nullable) is None
        # and model_fields_set contains the field
        if self.amount is None and "amount" in self.model_fields_set:
            _dict['amount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AgreementAdjustment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in AgreementAdjustment) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "agreementId": obj.get("agreementId"),
            "amount": obj.get("amount"),
            "customFields": [CustomFieldValue.from_dict(_item) for _item in obj.get("customFields")] if obj.get("customFields") is not None else None,
            "description": obj.get("description"),
            "effectiveDate": obj.get("effectiveDate"),
            "id": obj.get("id")
        })
        return _obj

