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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Link(BaseModel):
    """
    Link
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    id: Optional[StrictInt] = None
    name: StrictStr = Field(description=" Max length: 50;")
    screen_link: Optional[StrictStr] = Field(default=None, alias="screenLink")
    table_reference_id: Optional[StrictInt] = Field(default=None, alias="tableReferenceId")
    url: Optional[StrictStr] = Field(default=None, description=" Max length: 1000;")
    __properties: ClassVar[List[str]] = ["_info", "id", "name", "screenLink", "tableReferenceId", "url"]

    @field_validator('screen_link')
    def screen_link_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Company', 'Contact', 'Service', 'Invoice', 'PurchaseOrder', 'SalesOrder'):
            raise ValueError("must be one of enum values ('Company', 'Contact', 'Service', 'Invoice', 'PurchaseOrder', 'SalesOrder')")
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
        """Create an instance of Link from a JSON string"""
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
        # set to None if screen_link (nullable) is None
        # and model_fields_set contains the field
        if self.screen_link is None and "screen_link" in self.model_fields_set:
            _dict['screenLink'] = None

        # set to None if table_reference_id (nullable) is None
        # and model_fields_set contains the field
        if self.table_reference_id is None and "table_reference_id" in self.model_fields_set:
            _dict['tableReferenceId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Link from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Link) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "screenLink": obj.get("screenLink"),
            "tableReferenceId": obj.get("tableReferenceId"),
            "url": obj.get("url")
        })
        return _obj


