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
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from connectwise_psa.models.configuration_type_reference import ConfigurationTypeReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConfigurationTypeQuestion(BaseModel):
    """
    ConfigurationTypeQuestion
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    configuration_type: Optional[ConfigurationTypeReference] = Field(default=None, alias="configurationType")
    entry_type: Optional[StrictStr] = Field(alias="entryType")
    field_type: Optional[StrictStr] = Field(alias="fieldType")
    id: Optional[StrictInt] = None
    inactive_flag: Optional[StrictBool] = Field(default=None, alias="inactiveFlag")
    number_of_decimals: Optional[StrictInt] = Field(default=None, alias="numberOfDecimals")
    question: StrictStr = Field(description=" Max length: 1000;")
    required_flag: Optional[StrictBool] = Field(default=None, alias="requiredFlag")
    sequence_number: Optional[Union[StrictFloat, StrictInt]] = Field(alias="sequenceNumber")
    __properties: ClassVar[List[str]] = ["_info", "configurationType", "entryType", "fieldType", "id", "inactiveFlag", "numberOfDecimals", "question", "requiredFlag", "sequenceNumber"]

    @field_validator('entry_type')
    def entry_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Date', 'EntryField', 'List', 'Option'):
            raise ValueError("must be one of enum values ('Date', 'EntryField', 'List', 'Option')")
        return value

    @field_validator('field_type')
    def field_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('TextArea', 'Currency', 'Date', 'Hyperlink', 'IPAddress', 'Checkbox', 'Number', 'Percent', 'Text', 'Password'):
            raise ValueError("must be one of enum values ('TextArea', 'Currency', 'Date', 'Hyperlink', 'IPAddress', 'Checkbox', 'Number', 'Percent', 'Text', 'Password')")
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
        """Create an instance of ConfigurationTypeQuestion from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of configuration_type
        if self.configuration_type:
            _dict['configurationType'] = self.configuration_type.to_dict()
        # set to None if entry_type (nullable) is None
        # and model_fields_set contains the field
        if self.entry_type is None and "entry_type" in self.model_fields_set:
            _dict['entryType'] = None

        # set to None if field_type (nullable) is None
        # and model_fields_set contains the field
        if self.field_type is None and "field_type" in self.model_fields_set:
            _dict['fieldType'] = None

        # set to None if inactive_flag (nullable) is None
        # and model_fields_set contains the field
        if self.inactive_flag is None and "inactive_flag" in self.model_fields_set:
            _dict['inactiveFlag'] = None

        # set to None if number_of_decimals (nullable) is None
        # and model_fields_set contains the field
        if self.number_of_decimals is None and "number_of_decimals" in self.model_fields_set:
            _dict['numberOfDecimals'] = None

        # set to None if required_flag (nullable) is None
        # and model_fields_set contains the field
        if self.required_flag is None and "required_flag" in self.model_fields_set:
            _dict['requiredFlag'] = None

        # set to None if sequence_number (nullable) is None
        # and model_fields_set contains the field
        if self.sequence_number is None and "sequence_number" in self.model_fields_set:
            _dict['sequenceNumber'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ConfigurationTypeQuestion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ConfigurationTypeQuestion) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "configurationType": ConfigurationTypeReference.from_dict(obj.get("configurationType")) if obj.get("configurationType") is not None else None,
            "entryType": obj.get("entryType"),
            "fieldType": obj.get("fieldType"),
            "id": obj.get("id"),
            "inactiveFlag": obj.get("inactiveFlag"),
            "numberOfDecimals": obj.get("numberOfDecimals"),
            "question": obj.get("question"),
            "requiredFlag": obj.get("requiredFlag"),
            "sequenceNumber": obj.get("sequenceNumber")
        })
        return _obj

