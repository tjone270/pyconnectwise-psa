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
from connectwise_psa.models.rma_status_email_template_reference import RmaStatusEmailTemplateReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RmaStatus(BaseModel):
    """
    RmaStatus
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    closed_flag: Optional[StrictBool] = Field(default=None, alias="closedFlag")
    default_flag: Optional[StrictBool] = Field(default=None, alias="defaultFlag")
    email_template: Optional[RmaStatusEmailTemplateReference] = Field(default=None, alias="emailTemplate")
    id: Optional[StrictInt] = None
    name: StrictStr = Field(description=" Max length: 50;")
    sort_order: Optional[StrictInt] = Field(default=None, alias="sortOrder")
    __properties: ClassVar[List[str]] = ["_info", "closedFlag", "defaultFlag", "emailTemplate", "id", "name", "sortOrder"]

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
        """Create an instance of RmaStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of email_template
        if self.email_template:
            _dict['emailTemplate'] = self.email_template.to_dict()
        # set to None if closed_flag (nullable) is None
        # and model_fields_set contains the field
        if self.closed_flag is None and "closed_flag" in self.model_fields_set:
            _dict['closedFlag'] = None

        # set to None if default_flag (nullable) is None
        # and model_fields_set contains the field
        if self.default_flag is None and "default_flag" in self.model_fields_set:
            _dict['defaultFlag'] = None

        # set to None if sort_order (nullable) is None
        # and model_fields_set contains the field
        if self.sort_order is None and "sort_order" in self.model_fields_set:
            _dict['sortOrder'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RmaStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in RmaStatus) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "closedFlag": obj.get("closedFlag"),
            "defaultFlag": obj.get("defaultFlag"),
            "emailTemplate": RmaStatusEmailTemplateReference.from_dict(obj.get("emailTemplate")) if obj.get("emailTemplate") is not None else None,
            "id": obj.get("id"),
            "name": obj.get("name"),
            "sortOrder": obj.get("sortOrder")
        })
        return _obj


