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
from connectwise_psa.models.holiday_list_reference import HolidayListReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class HolidayInfo(BaseModel):
    """
    HolidayInfo
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    all_day_flag: Optional[StrictBool] = Field(default=None, description="Can be set to false to set a holiday for specific hours (Defaults to True).", alias="allDayFlag")
    var_date: Optional[StrictStr] = Field(default=None, alias="date")
    holiday_list: Optional[HolidayListReference] = Field(default=None, alias="holidayList")
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    time_end: Optional[StrictStr] = Field(default=None, alias="timeEnd")
    time_start: Optional[StrictStr] = Field(default=None, alias="timeStart")
    __properties: ClassVar[List[str]] = ["_info", "allDayFlag", "date", "holidayList", "id", "name", "timeEnd", "timeStart"]

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
        """Create an instance of HolidayInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of holiday_list
        if self.holiday_list:
            _dict['holidayList'] = self.holiday_list.to_dict()
        # set to None if all_day_flag (nullable) is None
        # and model_fields_set contains the field
        if self.all_day_flag is None and "all_day_flag" in self.model_fields_set:
            _dict['allDayFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of HolidayInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in HolidayInfo) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "allDayFlag": obj.get("allDayFlag"),
            "date": obj.get("date"),
            "holidayList": HolidayListReference.from_dict(obj.get("holidayList")) if obj.get("holidayList") is not None else None,
            "id": obj.get("id"),
            "name": obj.get("name"),
            "timeEnd": obj.get("timeEnd"),
            "timeStart": obj.get("timeStart")
        })
        return _obj


