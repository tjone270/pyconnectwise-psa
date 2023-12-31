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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConfigurationQuestion(BaseModel):
    """
    ConfigurationQuestion
    """ # noqa: E501
    answer: Optional[Union[str, Any]] = None
    answer_id: Optional[StrictInt] = Field(default=None, alias="answerId")
    field_type: Optional[StrictStr] = Field(default=None, alias="fieldType")
    number_of_decimals: Optional[StrictInt] = Field(default=None, alias="numberOfDecimals")
    question: Optional[StrictStr] = None
    question_id: Optional[StrictInt] = Field(default=None, alias="questionId")
    required_flag: Optional[StrictBool] = Field(default=None, alias="requiredFlag")
    sequence_number: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="sequenceNumber")
    __properties: ClassVar[List[str]] = ["answer", "answerId", "fieldType", "numberOfDecimals", "question", "questionId", "requiredFlag", "sequenceNumber"]

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
        """Create an instance of ConfigurationQuestion from a JSON string"""
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
        # set to None if answer_id (nullable) is None
        # and model_fields_set contains the field
        if self.answer_id is None and "answer_id" in self.model_fields_set:
            _dict['answerId'] = None

        # set to None if field_type (nullable) is None
        # and model_fields_set contains the field
        if self.field_type is None and "field_type" in self.model_fields_set:
            _dict['fieldType'] = None

        # set to None if number_of_decimals (nullable) is None
        # and model_fields_set contains the field
        if self.number_of_decimals is None and "number_of_decimals" in self.model_fields_set:
            _dict['numberOfDecimals'] = None

        # set to None if question_id (nullable) is None
        # and model_fields_set contains the field
        if self.question_id is None and "question_id" in self.model_fields_set:
            _dict['questionId'] = None

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
        """Create an instance of ConfigurationQuestion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ConfigurationQuestion) in the input: " + _key)

        _obj = cls.model_validate({
            "answer": obj.get("answer"),
            "answerId": obj.get("answerId"),
            "fieldType": obj.get("fieldType"),
            "numberOfDecimals": obj.get("numberOfDecimals"),
            "question": obj.get("question"),
            "questionId": obj.get("questionId"),
            "requiredFlag": obj.get("requiredFlag"),
            "sequenceNumber": obj.get("sequenceNumber")
        })
        return _obj


