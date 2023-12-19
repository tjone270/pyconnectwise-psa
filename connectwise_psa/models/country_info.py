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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CountryInfo(BaseModel):
    """
    CountryInfo
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    city_caption: Optional[StrictStr] = Field(default=None, alias="cityCaption")
    default_flag: Optional[StrictBool] = Field(default=None, alias="defaultFlag")
    dialing_prefix: Optional[StrictStr] = Field(default=None, alias="dialingPrefix")
    id: Optional[StrictInt] = None
    localization_caption_one: Optional[StrictStr] = Field(default=None, alias="localizationCaptionOne")
    name: Optional[StrictStr] = None
    state_caption: Optional[StrictStr] = Field(default=None, alias="stateCaption")
    zip_caption: Optional[StrictStr] = Field(default=None, alias="zipCaption")
    __properties: ClassVar[List[str]] = ["_info", "cityCaption", "defaultFlag", "dialingPrefix", "id", "localizationCaptionOne", "name", "stateCaption", "zipCaption"]

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
        """Create an instance of CountryInfo from a JSON string"""
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
        # set to None if default_flag (nullable) is None
        # and model_fields_set contains the field
        if self.default_flag is None and "default_flag" in self.model_fields_set:
            _dict['defaultFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CountryInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in CountryInfo) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "cityCaption": obj.get("cityCaption"),
            "defaultFlag": obj.get("defaultFlag"),
            "dialingPrefix": obj.get("dialingPrefix"),
            "id": obj.get("id"),
            "localizationCaptionOne": obj.get("localizationCaptionOne"),
            "name": obj.get("name"),
            "stateCaption": obj.get("stateCaption"),
            "zipCaption": obj.get("zipCaption")
        })
        return _obj


