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
from connectwise_psa.models.board_reference import BoardReference
from connectwise_psa.models.member_reference import MemberReference
from connectwise_psa.models.service_team_reference import ServiceTeamReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TeamMember(BaseModel):
    """
    TeamMember
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    board: Optional[BoardReference] = None
    id: Optional[StrictInt] = None
    member: Optional[MemberReference] = None
    team: Optional[ServiceTeamReference] = None
    team_leader_flag: Optional[StrictBool] = Field(default=None, alias="teamLeaderFlag")
    __properties: ClassVar[List[str]] = ["_info", "board", "id", "member", "team", "teamLeaderFlag"]

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
        """Create an instance of TeamMember from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of board
        if self.board:
            _dict['board'] = self.board.to_dict()
        # override the default output from pydantic by calling `to_dict()` of member
        if self.member:
            _dict['member'] = self.member.to_dict()
        # override the default output from pydantic by calling `to_dict()` of team
        if self.team:
            _dict['team'] = self.team.to_dict()
        # set to None if team_leader_flag (nullable) is None
        # and model_fields_set contains the field
        if self.team_leader_flag is None and "team_leader_flag" in self.model_fields_set:
            _dict['teamLeaderFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TeamMember from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in TeamMember) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "board": BoardReference.from_dict(obj.get("board")) if obj.get("board") is not None else None,
            "id": obj.get("id"),
            "member": MemberReference.from_dict(obj.get("member")) if obj.get("member") is not None else None,
            "team": ServiceTeamReference.from_dict(obj.get("team")) if obj.get("team") is not None else None,
            "teamLeaderFlag": obj.get("teamLeaderFlag")
        })
        return _obj


