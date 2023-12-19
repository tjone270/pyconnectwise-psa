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
from connectwise_psa.models.currency_reference import CurrencyReference
from connectwise_psa.models.system_location_reference import SystemLocationReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class BillingSetupInfo(BaseModel):
    """
    BillingSetupInfo
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    currency: Optional[CurrencyReference] = None
    id: Optional[StrictInt] = None
    location: Optional[SystemLocationReference] = None
    remit_name: Optional[StrictStr] = Field(default=None, alias="remitName")
    __properties: ClassVar[List[str]] = ["_info", "currency", "id", "location", "remitName"]

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
        """Create an instance of BillingSetupInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of currency
        if self.currency:
            _dict['currency'] = self.currency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of BillingSetupInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in BillingSetupInfo) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "currency": CurrencyReference.from_dict(obj.get("currency")) if obj.get("currency") is not None else None,
            "id": obj.get("id"),
            "location": SystemLocationReference.from_dict(obj.get("location")) if obj.get("location") is not None else None,
            "remitName": obj.get("remitName")
        })
        return _obj


