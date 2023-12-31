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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CommunicationType(BaseModel):
    """
    CommunicationType
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    android_xref: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="androidXref")
    default_flag: Optional[StrictBool] = Field(default=None, alias="defaultFlag")
    description: StrictStr
    email_flag: Optional[StrictBool] = Field(default=None, description="Gets or sets at least one flag is required to be true -- phone, fax, or email.", alias="emailFlag")
    exchange_xref: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="exchangeXref")
    fax_flag: Optional[StrictBool] = Field(default=None, description="Gets or sets at least one flag is required to be true -- phone, fax, or email.", alias="faxFlag")
    google_xref: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="googleXref")
    id: Optional[StrictInt] = None
    iphone_xref: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="iphoneXref")
    phone_flag: Optional[StrictBool] = Field(default=None, description="Gets or sets at least one flag is required to be true -- phone, fax, or email.", alias="phoneFlag")
    __properties: ClassVar[List[str]] = ["_info", "androidXref", "defaultFlag", "description", "emailFlag", "exchangeXref", "faxFlag", "googleXref", "id", "iphoneXref", "phoneFlag"]

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
        """Create an instance of CommunicationType from a JSON string"""
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
        # set to None if default_flag (nullable) is None
        # and model_fields_set contains the field
        if self.default_flag is None and "default_flag" in self.model_fields_set:
            _dict['defaultFlag'] = None

        # set to None if email_flag (nullable) is None
        # and model_fields_set contains the field
        if self.email_flag is None and "email_flag" in self.model_fields_set:
            _dict['emailFlag'] = None

        # set to None if fax_flag (nullable) is None
        # and model_fields_set contains the field
        if self.fax_flag is None and "fax_flag" in self.model_fields_set:
            _dict['faxFlag'] = None

        # set to None if phone_flag (nullable) is None
        # and model_fields_set contains the field
        if self.phone_flag is None and "phone_flag" in self.model_fields_set:
            _dict['phoneFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CommunicationType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in CommunicationType) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "androidXref": obj.get("androidXref"),
            "defaultFlag": obj.get("defaultFlag"),
            "description": obj.get("description"),
            "emailFlag": obj.get("emailFlag"),
            "exchangeXref": obj.get("exchangeXref"),
            "faxFlag": obj.get("faxFlag"),
            "googleXref": obj.get("googleXref"),
            "id": obj.get("id"),
            "iphoneXref": obj.get("iphoneXref"),
            "phoneFlag": obj.get("phoneFlag")
        })
        return _obj


