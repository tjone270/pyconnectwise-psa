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
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from connectwise_psa.models.member_reference import MemberReference
from connectwise_psa.models.reminder_reference import ReminderReference
from connectwise_psa.models.schedule_span_reference import ScheduleSpanReference
from connectwise_psa.models.schedule_status_reference import ScheduleStatusReference
from connectwise_psa.models.schedule_type_reference import ScheduleTypeReference
from connectwise_psa.models.service_location_reference import ServiceLocationReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ScheduleEntry(BaseModel):
    """
    ScheduleEntry
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    acknowledged_date: Optional[datetime] = Field(default=None, alias="acknowledgedDate")
    acknowledged_flag: Optional[StrictBool] = Field(default=None, alias="acknowledgedFlag")
    add_member_to_project_flag: Optional[StrictBool] = Field(default=None, alias="addMemberToProjectFlag")
    allow_schedule_conflicts_flag: Optional[StrictBool] = Field(default=None, alias="allowScheduleConflictsFlag")
    close_date: Optional[datetime] = Field(default=None, alias="closeDate")
    date_end: Optional[datetime] = Field(default=None, alias="dateEnd")
    date_start: Optional[datetime] = Field(default=None, alias="dateStart")
    done_flag: Optional[StrictBool] = Field(default=None, alias="doneFlag")
    hours: Optional[Union[StrictFloat, StrictInt]] = None
    id: Optional[StrictInt] = None
    meeting_flag: Optional[StrictBool] = Field(default=None, alias="meetingFlag")
    member: Optional[MemberReference] = None
    mobile_guid: Optional[StrictStr] = Field(default=None, alias="mobileGuid")
    name: Optional[StrictStr] = Field(default=None, description=" Max length: 250;")
    object_id: Optional[StrictInt] = Field(default=None, alias="objectId")
    owner_flag: Optional[StrictBool] = Field(default=None, alias="ownerFlag")
    project_role_id: Optional[StrictInt] = Field(default=None, alias="projectRoleId")
    reminder: Optional[ReminderReference] = None
    span: Optional[ScheduleSpanReference] = None
    status: Optional[ScheduleStatusReference] = None
    type: Optional[ScheduleTypeReference] = None
    where: Optional[ServiceLocationReference] = None
    __properties: ClassVar[List[str]] = ["_info", "acknowledgedDate", "acknowledgedFlag", "addMemberToProjectFlag", "allowScheduleConflictsFlag", "closeDate", "dateEnd", "dateStart", "doneFlag", "hours", "id", "meetingFlag", "member", "mobileGuid", "name", "objectId", "ownerFlag", "projectRoleId", "reminder", "span", "status", "type", "where"]

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
        """Create an instance of ScheduleEntry from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of reminder
        if self.reminder:
            _dict['reminder'] = self.reminder.to_dict()
        # override the default output from pydantic by calling `to_dict()` of span
        if self.span:
            _dict['span'] = self.span.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of where
        if self.where:
            _dict['where'] = self.where.to_dict()
        # set to None if acknowledged_flag (nullable) is None
        # and model_fields_set contains the field
        if self.acknowledged_flag is None and "acknowledged_flag" in self.model_fields_set:
            _dict['acknowledgedFlag'] = None

        # set to None if add_member_to_project_flag (nullable) is None
        # and model_fields_set contains the field
        if self.add_member_to_project_flag is None and "add_member_to_project_flag" in self.model_fields_set:
            _dict['addMemberToProjectFlag'] = None

        # set to None if allow_schedule_conflicts_flag (nullable) is None
        # and model_fields_set contains the field
        if self.allow_schedule_conflicts_flag is None and "allow_schedule_conflicts_flag" in self.model_fields_set:
            _dict['allowScheduleConflictsFlag'] = None

        # set to None if done_flag (nullable) is None
        # and model_fields_set contains the field
        if self.done_flag is None and "done_flag" in self.model_fields_set:
            _dict['doneFlag'] = None

        # set to None if hours (nullable) is None
        # and model_fields_set contains the field
        if self.hours is None and "hours" in self.model_fields_set:
            _dict['hours'] = None

        # set to None if meeting_flag (nullable) is None
        # and model_fields_set contains the field
        if self.meeting_flag is None and "meeting_flag" in self.model_fields_set:
            _dict['meetingFlag'] = None

        # set to None if mobile_guid (nullable) is None
        # and model_fields_set contains the field
        if self.mobile_guid is None and "mobile_guid" in self.model_fields_set:
            _dict['mobileGuid'] = None

        # set to None if object_id (nullable) is None
        # and model_fields_set contains the field
        if self.object_id is None and "object_id" in self.model_fields_set:
            _dict['objectId'] = None

        # set to None if owner_flag (nullable) is None
        # and model_fields_set contains the field
        if self.owner_flag is None and "owner_flag" in self.model_fields_set:
            _dict['ownerFlag'] = None

        # set to None if project_role_id (nullable) is None
        # and model_fields_set contains the field
        if self.project_role_id is None and "project_role_id" in self.model_fields_set:
            _dict['projectRoleId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ScheduleEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ScheduleEntry) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "acknowledgedDate": obj.get("acknowledgedDate"),
            "acknowledgedFlag": obj.get("acknowledgedFlag"),
            "addMemberToProjectFlag": obj.get("addMemberToProjectFlag"),
            "allowScheduleConflictsFlag": obj.get("allowScheduleConflictsFlag"),
            "closeDate": obj.get("closeDate"),
            "dateEnd": obj.get("dateEnd"),
            "dateStart": obj.get("dateStart"),
            "doneFlag": obj.get("doneFlag"),
            "hours": obj.get("hours"),
            "id": obj.get("id"),
            "meetingFlag": obj.get("meetingFlag"),
            "member": MemberReference.from_dict(obj.get("member")) if obj.get("member") is not None else None,
            "mobileGuid": obj.get("mobileGuid"),
            "name": obj.get("name"),
            "objectId": obj.get("objectId"),
            "ownerFlag": obj.get("ownerFlag"),
            "projectRoleId": obj.get("projectRoleId"),
            "reminder": ReminderReference.from_dict(obj.get("reminder")) if obj.get("reminder") is not None else None,
            "span": ScheduleSpanReference.from_dict(obj.get("span")) if obj.get("span") is not None else None,
            "status": ScheduleStatusReference.from_dict(obj.get("status")) if obj.get("status") is not None else None,
            "type": ScheduleTypeReference.from_dict(obj.get("type")) if obj.get("type") is not None else None,
            "where": ServiceLocationReference.from_dict(obj.get("where")) if obj.get("where") is not None else None
        })
        return _obj

