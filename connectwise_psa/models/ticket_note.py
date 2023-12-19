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
from connectwise_psa.models.contact_reference import ContactReference
from connectwise_psa.models.member_reference import MemberReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TicketNote(BaseModel):
    """
    TicketNote
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    contact: Optional[ContactReference] = None
    customer_updated_flag: Optional[StrictBool] = Field(default=None, alias="customerUpdatedFlag")
    detail_description_flag: Optional[StrictBool] = Field(default=None, alias="detailDescriptionFlag")
    external_flag: Optional[StrictBool] = Field(default=None, alias="externalFlag")
    id: Optional[StrictInt] = None
    internal_analysis_flag: Optional[StrictBool] = Field(default=None, alias="internalAnalysisFlag")
    internal_flag: Optional[StrictBool] = Field(default=None, alias="internalFlag")
    issue_flag: Optional[StrictBool] = Field(default=None, alias="issueFlag")
    member: Optional[MemberReference] = None
    process_notifications: Optional[StrictBool] = Field(default=None, alias="processNotifications")
    resolution_flag: Optional[StrictBool] = Field(default=None, alias="resolutionFlag")
    text: Optional[StrictStr] = None
    ticket_id: Optional[StrictInt] = Field(default=None, alias="ticketId")
    __properties: ClassVar[List[str]] = ["_info", "contact", "customerUpdatedFlag", "detailDescriptionFlag", "externalFlag", "id", "internalAnalysisFlag", "internalFlag", "issueFlag", "member", "processNotifications", "resolutionFlag", "text", "ticketId"]

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
        """Create an instance of TicketNote from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of contact
        if self.contact:
            _dict['contact'] = self.contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of member
        if self.member:
            _dict['member'] = self.member.to_dict()
        # set to None if customer_updated_flag (nullable) is None
        # and model_fields_set contains the field
        if self.customer_updated_flag is None and "customer_updated_flag" in self.model_fields_set:
            _dict['customerUpdatedFlag'] = None

        # set to None if detail_description_flag (nullable) is None
        # and model_fields_set contains the field
        if self.detail_description_flag is None and "detail_description_flag" in self.model_fields_set:
            _dict['detailDescriptionFlag'] = None

        # set to None if external_flag (nullable) is None
        # and model_fields_set contains the field
        if self.external_flag is None and "external_flag" in self.model_fields_set:
            _dict['externalFlag'] = None

        # set to None if internal_analysis_flag (nullable) is None
        # and model_fields_set contains the field
        if self.internal_analysis_flag is None and "internal_analysis_flag" in self.model_fields_set:
            _dict['internalAnalysisFlag'] = None

        # set to None if internal_flag (nullable) is None
        # and model_fields_set contains the field
        if self.internal_flag is None and "internal_flag" in self.model_fields_set:
            _dict['internalFlag'] = None

        # set to None if issue_flag (nullable) is None
        # and model_fields_set contains the field
        if self.issue_flag is None and "issue_flag" in self.model_fields_set:
            _dict['issueFlag'] = None

        # set to None if process_notifications (nullable) is None
        # and model_fields_set contains the field
        if self.process_notifications is None and "process_notifications" in self.model_fields_set:
            _dict['processNotifications'] = None

        # set to None if resolution_flag (nullable) is None
        # and model_fields_set contains the field
        if self.resolution_flag is None and "resolution_flag" in self.model_fields_set:
            _dict['resolutionFlag'] = None

        # set to None if ticket_id (nullable) is None
        # and model_fields_set contains the field
        if self.ticket_id is None and "ticket_id" in self.model_fields_set:
            _dict['ticketId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TicketNote from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in TicketNote) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "contact": ContactReference.from_dict(obj.get("contact")) if obj.get("contact") is not None else None,
            "customerUpdatedFlag": obj.get("customerUpdatedFlag"),
            "detailDescriptionFlag": obj.get("detailDescriptionFlag"),
            "externalFlag": obj.get("externalFlag"),
            "id": obj.get("id"),
            "internalAnalysisFlag": obj.get("internalAnalysisFlag"),
            "internalFlag": obj.get("internalFlag"),
            "issueFlag": obj.get("issueFlag"),
            "member": MemberReference.from_dict(obj.get("member")) if obj.get("member") is not None else None,
            "processNotifications": obj.get("processNotifications"),
            "resolutionFlag": obj.get("resolutionFlag"),
            "text": obj.get("text"),
            "ticketId": obj.get("ticketId")
        })
        return _obj

