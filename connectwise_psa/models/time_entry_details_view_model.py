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
from connectwise_psa.models.generic_name_id_dto import GenericNameIdDTO
from connectwise_psa.models.user_defined_field_value import UserDefinedFieldValue
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TimeEntryDetailsViewModel(BaseModel):
    """
    TimeEntryDetailsViewModel
    """ # noqa: E501
    activity_end_time: Optional[datetime] = Field(default=None, alias="activityEndTime")
    activity_start_time: Optional[datetime] = Field(default=None, alias="activityStartTime")
    billable: Optional[GenericNameIdDTO] = None
    deduct: Optional[Union[StrictFloat, StrictInt]] = None
    end_time: Optional[datetime] = Field(default=None, alias="endTime")
    hours: Optional[Union[StrictFloat, StrictInt]] = None
    internal_notes: Optional[StrictStr] = Field(default=None, alias="internalNotes")
    member_time_zone_offset: Optional[StrictInt] = Field(default=None, alias="memberTimeZoneOffset")
    notes: Optional[StrictStr] = None
    notes_markdown: Optional[StrictStr] = Field(default=None, alias="notes_Markdown")
    start_time: Optional[datetime] = Field(default=None, alias="startTime")
    time_details_pod_user_defined_fields: Optional[List[UserDefinedFieldValue]] = Field(default=None, alias="timeDetailsPodUserDefinedFields")
    work_type: Optional[GenericNameIdDTO] = Field(default=None, alias="workType")
    __properties: ClassVar[List[str]] = ["activityEndTime", "activityStartTime", "billable", "deduct", "endTime", "hours", "internalNotes", "memberTimeZoneOffset", "notes", "notes_Markdown", "startTime", "timeDetailsPodUserDefinedFields", "workType"]

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
        """Create an instance of TimeEntryDetailsViewModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of billable
        if self.billable:
            _dict['billable'] = self.billable.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in time_details_pod_user_defined_fields (list)
        _items = []
        if self.time_details_pod_user_defined_fields:
            for _item in self.time_details_pod_user_defined_fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['timeDetailsPodUserDefinedFields'] = _items
        # override the default output from pydantic by calling `to_dict()` of work_type
        if self.work_type:
            _dict['workType'] = self.work_type.to_dict()
        # set to None if deduct (nullable) is None
        # and model_fields_set contains the field
        if self.deduct is None and "deduct" in self.model_fields_set:
            _dict['deduct'] = None

        # set to None if hours (nullable) is None
        # and model_fields_set contains the field
        if self.hours is None and "hours" in self.model_fields_set:
            _dict['hours'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TimeEntryDetailsViewModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in TimeEntryDetailsViewModel) in the input: " + _key)

        _obj = cls.model_validate({
            "activityEndTime": obj.get("activityEndTime"),
            "activityStartTime": obj.get("activityStartTime"),
            "billable": GenericNameIdDTO.from_dict(obj.get("billable")) if obj.get("billable") is not None else None,
            "deduct": obj.get("deduct"),
            "endTime": obj.get("endTime"),
            "hours": obj.get("hours"),
            "internalNotes": obj.get("internalNotes"),
            "memberTimeZoneOffset": obj.get("memberTimeZoneOffset"),
            "notes": obj.get("notes"),
            "notes_Markdown": obj.get("notes_Markdown"),
            "startTime": obj.get("startTime"),
            "timeDetailsPodUserDefinedFields": [UserDefinedFieldValue.from_dict(_item) for _item in obj.get("timeDetailsPodUserDefinedFields")] if obj.get("timeDetailsPodUserDefinedFields") is not None else None,
            "workType": GenericNameIdDTO.from_dict(obj.get("workType")) if obj.get("workType") is not None else None
        })
        return _obj


