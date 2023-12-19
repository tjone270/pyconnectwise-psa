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
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from connectwise_psa.models.board_reference import BoardReference
from connectwise_psa.models.security_role_reference import SecurityRoleReference
from connectwise_psa.models.structure_reference import StructureReference
from connectwise_psa.models.system_department_reference import SystemDepartmentReference
from connectwise_psa.models.system_location_reference import SystemLocationReference
from connectwise_psa.models.time_zone_setup_reference import TimeZoneSetupReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ApiMember(BaseModel):
    """
    ApiMember
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    block_cost_flag: Optional[StrictBool] = Field(default=None, alias="blockCostFlag")
    block_price_flag: Optional[StrictBool] = Field(default=None, alias="blockPriceFlag")
    default_department: Optional[SystemDepartmentReference] = Field(default=None, alias="defaultDepartment")
    default_location: Optional[SystemLocationReference] = Field(default=None, alias="defaultLocation")
    email_address: Optional[StrictStr] = Field(default=None, description=" Max length: 250;", alias="emailAddress")
    excluded_service_board_ids: Optional[List[StrictInt]] = Field(default=None, alias="excludedServiceBoardIds")
    id: Optional[StrictInt] = None
    identifier: StrictStr = Field(description=" Max length: 15;")
    inactive_date: Optional[datetime] = Field(default=None, alias="inactiveDate")
    inactive_flag: Optional[StrictBool] = Field(default=None, alias="inactiveFlag")
    name: Optional[StrictStr] = Field(default=None, description=" Max length: 30; Required On Updates;")
    notes: Optional[StrictStr] = None
    sales_default_location: Optional[SystemLocationReference] = Field(default=None, alias="salesDefaultLocation")
    security_location: Optional[SystemLocationReference] = Field(default=None, alias="securityLocation")
    security_role: Optional[SecurityRoleReference] = Field(default=None, alias="securityRole")
    service_default_board: Optional[BoardReference] = Field(default=None, alias="serviceDefaultBoard")
    structure_level: Optional[StructureReference] = Field(default=None, alias="structureLevel")
    time_zone: Optional[TimeZoneSetupReference] = Field(default=None, alias="timeZone")
    __properties: ClassVar[List[str]] = ["_info", "blockCostFlag", "blockPriceFlag", "defaultDepartment", "defaultLocation", "emailAddress", "excludedServiceBoardIds", "id", "identifier", "inactiveDate", "inactiveFlag", "name", "notes", "salesDefaultLocation", "securityLocation", "securityRole", "serviceDefaultBoard", "structureLevel", "timeZone"]

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
        """Create an instance of ApiMember from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of default_department
        if self.default_department:
            _dict['defaultDepartment'] = self.default_department.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_location
        if self.default_location:
            _dict['defaultLocation'] = self.default_location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sales_default_location
        if self.sales_default_location:
            _dict['salesDefaultLocation'] = self.sales_default_location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of security_location
        if self.security_location:
            _dict['securityLocation'] = self.security_location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of security_role
        if self.security_role:
            _dict['securityRole'] = self.security_role.to_dict()
        # override the default output from pydantic by calling `to_dict()` of service_default_board
        if self.service_default_board:
            _dict['serviceDefaultBoard'] = self.service_default_board.to_dict()
        # override the default output from pydantic by calling `to_dict()` of structure_level
        if self.structure_level:
            _dict['structureLevel'] = self.structure_level.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time_zone
        if self.time_zone:
            _dict['timeZone'] = self.time_zone.to_dict()
        # set to None if block_cost_flag (nullable) is None
        # and model_fields_set contains the field
        if self.block_cost_flag is None and "block_cost_flag" in self.model_fields_set:
            _dict['blockCostFlag'] = None

        # set to None if block_price_flag (nullable) is None
        # and model_fields_set contains the field
        if self.block_price_flag is None and "block_price_flag" in self.model_fields_set:
            _dict['blockPriceFlag'] = None

        # set to None if inactive_flag (nullable) is None
        # and model_fields_set contains the field
        if self.inactive_flag is None and "inactive_flag" in self.model_fields_set:
            _dict['inactiveFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ApiMember from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ApiMember) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "blockCostFlag": obj.get("blockCostFlag"),
            "blockPriceFlag": obj.get("blockPriceFlag"),
            "defaultDepartment": SystemDepartmentReference.from_dict(obj.get("defaultDepartment")) if obj.get("defaultDepartment") is not None else None,
            "defaultLocation": SystemLocationReference.from_dict(obj.get("defaultLocation")) if obj.get("defaultLocation") is not None else None,
            "emailAddress": obj.get("emailAddress"),
            "excludedServiceBoardIds": obj.get("excludedServiceBoardIds"),
            "id": obj.get("id"),
            "identifier": obj.get("identifier"),
            "inactiveDate": obj.get("inactiveDate"),
            "inactiveFlag": obj.get("inactiveFlag"),
            "name": obj.get("name"),
            "notes": obj.get("notes"),
            "salesDefaultLocation": SystemLocationReference.from_dict(obj.get("salesDefaultLocation")) if obj.get("salesDefaultLocation") is not None else None,
            "securityLocation": SystemLocationReference.from_dict(obj.get("securityLocation")) if obj.get("securityLocation") is not None else None,
            "securityRole": SecurityRoleReference.from_dict(obj.get("securityRole")) if obj.get("securityRole") is not None else None,
            "serviceDefaultBoard": BoardReference.from_dict(obj.get("serviceDefaultBoard")) if obj.get("serviceDefaultBoard") is not None else None,
            "structureLevel": StructureReference.from_dict(obj.get("structureLevel")) if obj.get("structureLevel") is not None else None,
            "timeZone": TimeZoneSetupReference.from_dict(obj.get("timeZone")) if obj.get("timeZone") is not None else None
        })
        return _obj


