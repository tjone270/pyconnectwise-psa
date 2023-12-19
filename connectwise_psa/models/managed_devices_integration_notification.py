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
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
from connectwise_psa.models.managed_devices_integration_reference import ManagedDevicesIntegrationReference
from connectwise_psa.models.member_reference import MemberReference
from connectwise_psa.models.notification_recipient_reference import NotificationRecipientReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ManagedDevicesIntegrationNotification(BaseModel):
    """
    ManagedDevicesIntegrationNotification
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    id: Optional[StrictInt] = None
    log_type: Optional[StrictStr] = Field(alias="logType")
    managed_devices_integration: Optional[ManagedDevicesIntegrationReference] = Field(default=None, alias="managedDevicesIntegration")
    member: Optional[MemberReference] = None
    notify_who: Optional[NotificationRecipientReference] = Field(default=None, alias="notifyWho")
    __properties: ClassVar[List[str]] = ["_info", "id", "logType", "managedDevicesIntegration", "member", "notifyWho"]

    @field_validator('log_type')
    def log_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('All', 'Error', 'NewManagedSolution', 'NewDeviceType', 'NewConfiguration', 'NewAddition', 'Info'):
            raise ValueError("must be one of enum values ('All', 'Error', 'NewManagedSolution', 'NewDeviceType', 'NewConfiguration', 'NewAddition', 'Info')")
        return value

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
        """Create an instance of ManagedDevicesIntegrationNotification from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of managed_devices_integration
        if self.managed_devices_integration:
            _dict['managedDevicesIntegration'] = self.managed_devices_integration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of member
        if self.member:
            _dict['member'] = self.member.to_dict()
        # override the default output from pydantic by calling `to_dict()` of notify_who
        if self.notify_who:
            _dict['notifyWho'] = self.notify_who.to_dict()
        # set to None if log_type (nullable) is None
        # and model_fields_set contains the field
        if self.log_type is None and "log_type" in self.model_fields_set:
            _dict['logType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ManagedDevicesIntegrationNotification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ManagedDevicesIntegrationNotification) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "id": obj.get("id"),
            "logType": obj.get("logType"),
            "managedDevicesIntegration": ManagedDevicesIntegrationReference.from_dict(obj.get("managedDevicesIntegration")) if obj.get("managedDevicesIntegration") is not None else None,
            "member": MemberReference.from_dict(obj.get("member")) if obj.get("member") is not None else None,
            "notifyWho": NotificationRecipientReference.from_dict(obj.get("notifyWho")) if obj.get("notifyWho") is not None else None
        })
        return _obj


