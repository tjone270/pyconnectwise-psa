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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from connectwise_psa.models.system_location_reference import SystemLocationReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class QuoteLink(BaseModel):
    """
    QuoteLink
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    all_locations_flag: Optional[StrictBool] = Field(default=None, alias="allLocationsFlag")
    id: Optional[StrictInt] = None
    link: StrictStr = Field(description=" Max length: 2000;")
    location: Optional[SystemLocationReference] = None
    new_window_flag: Optional[StrictBool] = Field(default=None, alias="newWindowFlag")
    __properties: ClassVar[List[str]] = ["_info", "allLocationsFlag", "id", "link", "location", "newWindowFlag"]

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
        """Create an instance of QuoteLink from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # set to None if all_locations_flag (nullable) is None
        # and model_fields_set contains the field
        if self.all_locations_flag is None and "all_locations_flag" in self.model_fields_set:
            _dict['allLocationsFlag'] = None

        # set to None if new_window_flag (nullable) is None
        # and model_fields_set contains the field
        if self.new_window_flag is None and "new_window_flag" in self.model_fields_set:
            _dict['newWindowFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of QuoteLink from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in QuoteLink) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "allLocationsFlag": obj.get("allLocationsFlag"),
            "id": obj.get("id"),
            "link": obj.get("link"),
            "location": SystemLocationReference.from_dict(obj.get("location")) if obj.get("location") is not None else None,
            "newWindowFlag": obj.get("newWindowFlag")
        })
        return _obj

