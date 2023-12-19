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
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WonRevenueReference(BaseModel):
    """
    WonRevenueReference
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    cost: Optional[Union[StrictFloat, StrictInt]] = None
    id: Optional[StrictInt] = None
    margin: Optional[Union[StrictFloat, StrictInt]] = None
    percentage: Optional[Union[StrictFloat, StrictInt]] = None
    revenue: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["_info", "cost", "id", "margin", "percentage", "revenue"]

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
        """Create an instance of WonRevenueReference from a JSON string"""
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
        # set to None if cost (nullable) is None
        # and model_fields_set contains the field
        if self.cost is None and "cost" in self.model_fields_set:
            _dict['cost'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if margin (nullable) is None
        # and model_fields_set contains the field
        if self.margin is None and "margin" in self.model_fields_set:
            _dict['margin'] = None

        # set to None if percentage (nullable) is None
        # and model_fields_set contains the field
        if self.percentage is None and "percentage" in self.model_fields_set:
            _dict['percentage'] = None

        # set to None if revenue (nullable) is None
        # and model_fields_set contains the field
        if self.revenue is None and "revenue" in self.model_fields_set:
            _dict['revenue'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WonRevenueReference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in WonRevenueReference) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "cost": obj.get("cost"),
            "id": obj.get("id"),
            "margin": obj.get("margin"),
            "percentage": obj.get("percentage"),
            "revenue": obj.get("revenue")
        })
        return _obj


