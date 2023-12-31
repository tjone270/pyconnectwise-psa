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
from pydantic import BaseModel, StrictInt
from pydantic import Field
from connectwise_psa.models.member_reference import MemberReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class MemberDeactivationServiceTemplate(BaseModel):
    """
    MemberDeactivationServiceTemplate
    """ # noqa: E501
    count: Optional[StrictInt] = None
    re_assign_to_member: Optional[MemberReference] = Field(default=None, alias="reAssignToMember")
    __properties: ClassVar[List[str]] = ["count", "reAssignToMember"]

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
        """Create an instance of MemberDeactivationServiceTemplate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of re_assign_to_member
        if self.re_assign_to_member:
            _dict['reAssignToMember'] = self.re_assign_to_member.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of MemberDeactivationServiceTemplate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in MemberDeactivationServiceTemplate) in the input: " + _key)

        _obj = cls.model_validate({
            "count": obj.get("count"),
            "reAssignToMember": MemberReference.from_dict(obj.get("reAssignToMember")) if obj.get("reAssignToMember") is not None else None
        })
        return _obj


