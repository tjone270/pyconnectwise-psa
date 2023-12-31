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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, field_validator
from pydantic import Field
from connectwise_psa.models.member_reference import MemberReference
from connectwise_psa.models.skill_reference import SkillReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class MemberSkill(BaseModel):
    """
    MemberSkill
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    certified_flag: Optional[StrictBool] = Field(default=None, alias="certifiedFlag")
    id: Optional[StrictInt] = None
    member: Optional[MemberReference] = None
    notes: Optional[StrictStr] = None
    skill: SkillReference
    skill_level: Optional[StrictStr] = Field(alias="skillLevel")
    years_experience: Optional[StrictInt] = Field(default=None, alias="yearsExperience")
    __properties: ClassVar[List[str]] = ["_info", "certifiedFlag", "id", "member", "notes", "skill", "skillLevel", "yearsExperience"]

    @field_validator('skill_level')
    def skill_level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Beginner', 'Intermediate', 'Advanced', 'Expert'):
            raise ValueError("must be one of enum values ('Beginner', 'Intermediate', 'Advanced', 'Expert')")
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
        """Create an instance of MemberSkill from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of skill
        if self.skill:
            _dict['skill'] = self.skill.to_dict()
        # set to None if certified_flag (nullable) is None
        # and model_fields_set contains the field
        if self.certified_flag is None and "certified_flag" in self.model_fields_set:
            _dict['certifiedFlag'] = None

        # set to None if skill_level (nullable) is None
        # and model_fields_set contains the field
        if self.skill_level is None and "skill_level" in self.model_fields_set:
            _dict['skillLevel'] = None

        # set to None if years_experience (nullable) is None
        # and model_fields_set contains the field
        if self.years_experience is None and "years_experience" in self.model_fields_set:
            _dict['yearsExperience'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of MemberSkill from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in MemberSkill) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "certifiedFlag": obj.get("certifiedFlag"),
            "id": obj.get("id"),
            "member": MemberReference.from_dict(obj.get("member")) if obj.get("member") is not None else None,
            "notes": obj.get("notes"),
            "skill": SkillReference.from_dict(obj.get("skill")) if obj.get("skill") is not None else None,
            "skillLevel": obj.get("skillLevel"),
            "yearsExperience": obj.get("yearsExperience")
        })
        return _obj


