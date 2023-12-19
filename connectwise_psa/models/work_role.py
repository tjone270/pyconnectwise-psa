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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WorkRole(BaseModel):
    """
    WorkRole
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    add_all_agreement_exclusions: Optional[StrictBool] = Field(default=None, description="Used only on create to add the work role to all agreement and agreement type exclusion lists", alias="addAllAgreementExclusions")
    add_all_locations: Optional[StrictBool] = Field(default=None, alias="addAllLocations")
    hourly_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="hourlyRate")
    id: Optional[StrictInt] = None
    inactive_flag: Optional[StrictBool] = Field(default=None, alias="inactiveFlag")
    integration_xref: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="integrationXref")
    location_ids: Optional[List[StrictInt]] = Field(default=None, alias="locationIds")
    name: StrictStr = Field(description=" Max length: 50;")
    remove_all_locations: Optional[StrictBool] = Field(default=None, alias="removeAllLocations")
    __properties: ClassVar[List[str]] = ["_info", "addAllAgreementExclusions", "addAllLocations", "hourlyRate", "id", "inactiveFlag", "integrationXref", "locationIds", "name", "removeAllLocations"]

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
        """Create an instance of WorkRole from a JSON string"""
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
        # set to None if add_all_agreement_exclusions (nullable) is None
        # and model_fields_set contains the field
        if self.add_all_agreement_exclusions is None and "add_all_agreement_exclusions" in self.model_fields_set:
            _dict['addAllAgreementExclusions'] = None

        # set to None if add_all_locations (nullable) is None
        # and model_fields_set contains the field
        if self.add_all_locations is None and "add_all_locations" in self.model_fields_set:
            _dict['addAllLocations'] = None

        # set to None if hourly_rate (nullable) is None
        # and model_fields_set contains the field
        if self.hourly_rate is None and "hourly_rate" in self.model_fields_set:
            _dict['hourlyRate'] = None

        # set to None if inactive_flag (nullable) is None
        # and model_fields_set contains the field
        if self.inactive_flag is None and "inactive_flag" in self.model_fields_set:
            _dict['inactiveFlag'] = None

        # set to None if remove_all_locations (nullable) is None
        # and model_fields_set contains the field
        if self.remove_all_locations is None and "remove_all_locations" in self.model_fields_set:
            _dict['removeAllLocations'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WorkRole from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in WorkRole) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "addAllAgreementExclusions": obj.get("addAllAgreementExclusions"),
            "addAllLocations": obj.get("addAllLocations"),
            "hourlyRate": obj.get("hourlyRate"),
            "id": obj.get("id"),
            "inactiveFlag": obj.get("inactiveFlag"),
            "integrationXref": obj.get("integrationXref"),
            "locationIds": obj.get("locationIds"),
            "name": obj.get("name"),
            "removeAllLocations": obj.get("removeAllLocations")
        })
        return _obj


