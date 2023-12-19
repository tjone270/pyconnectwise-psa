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
from connectwise_psa.models.holiday_list_reference import HolidayListReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Calendar(BaseModel):
    """
    Calendar
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    friday_end_time: Optional[StrictStr] = Field(default=None, alias="fridayEndTime")
    friday_start_time: Optional[StrictStr] = Field(default=None, alias="fridayStartTime")
    holiday_list: Optional[HolidayListReference] = Field(default=None, alias="holidayList")
    id: Optional[StrictInt] = None
    monday_end_time: Optional[StrictStr] = Field(default=None, alias="mondayEndTime")
    monday_start_time: Optional[StrictStr] = Field(default=None, alias="mondayStartTime")
    name: StrictStr
    saturday_end_time: Optional[StrictStr] = Field(default=None, alias="saturdayEndTime")
    saturday_start_time: Optional[StrictStr] = Field(default=None, alias="saturdayStartTime")
    sunday_end_time: Optional[StrictStr] = Field(default=None, alias="sundayEndTime")
    sunday_start_time: Optional[StrictStr] = Field(default=None, alias="sundayStartTime")
    thursday_end_time: Optional[StrictStr] = Field(default=None, alias="thursdayEndTime")
    thursday_start_time: Optional[StrictStr] = Field(default=None, alias="thursdayStartTime")
    tuesday_end_time: Optional[StrictStr] = Field(default=None, alias="tuesdayEndTime")
    tuesday_start_time: Optional[StrictStr] = Field(default=None, alias="tuesdayStartTime")
    wednesday_end_time: Optional[StrictStr] = Field(default=None, alias="wednesdayEndTime")
    wednesday_start_time: Optional[StrictStr] = Field(default=None, alias="wednesdayStartTime")
    __properties: ClassVar[List[str]] = ["_info", "fridayEndTime", "fridayStartTime", "holidayList", "id", "mondayEndTime", "mondayStartTime", "name", "saturdayEndTime", "saturdayStartTime", "sundayEndTime", "sundayStartTime", "thursdayEndTime", "thursdayStartTime", "tuesdayEndTime", "tuesdayStartTime", "wednesdayEndTime", "wednesdayStartTime"]

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
        """Create an instance of Calendar from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Calendar from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Calendar) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "fridayEndTime": obj.get("fridayEndTime"),
            "fridayStartTime": obj.get("fridayStartTime"),
            "holidayList": HolidayListReference.from_dict(obj.get("holidayList")) if obj.get("holidayList") is not None else None,
            "id": obj.get("id"),
            "mondayEndTime": obj.get("mondayEndTime"),
            "mondayStartTime": obj.get("mondayStartTime"),
            "name": obj.get("name"),
            "saturdayEndTime": obj.get("saturdayEndTime"),
            "saturdayStartTime": obj.get("saturdayStartTime"),
            "sundayEndTime": obj.get("sundayEndTime"),
            "sundayStartTime": obj.get("sundayStartTime"),
            "thursdayEndTime": obj.get("thursdayEndTime"),
            "thursdayStartTime": obj.get("thursdayStartTime"),
            "tuesdayEndTime": obj.get("tuesdayEndTime"),
            "tuesdayStartTime": obj.get("tuesdayStartTime"),
            "wednesdayEndTime": obj.get("wednesdayEndTime"),
            "wednesdayStartTime": obj.get("wednesdayStartTime")
        })
        return _obj

