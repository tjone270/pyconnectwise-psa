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

class GLCaption(BaseModel):
    """
    GLCaption
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    cogs1: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    cogs10: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    cogs2: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    cogs3: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    cogs4: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    cogs5: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    cogs6: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    cogs7: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    cogs8: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    cogs9: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    id: Optional[StrictInt] = None
    segment1: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    segment10: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    segment10type: Optional[StrictStr] = None
    segment1type: Optional[StrictStr] = None
    segment2: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    segment2type: Optional[StrictStr] = None
    segment3: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    segment3type: Optional[StrictStr] = None
    segment4: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    segment4type: Optional[StrictStr] = None
    segment5: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    segment5type: Optional[StrictStr] = None
    segment6: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    segment6type: Optional[StrictStr] = None
    segment7: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    segment7type: Optional[StrictStr] = None
    segment8: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    segment8type: Optional[StrictStr] = None
    segment9: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    segment9type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["_info", "cogs1", "cogs10", "cogs2", "cogs3", "cogs4", "cogs5", "cogs6", "cogs7", "cogs8", "cogs9", "id", "segment1", "segment10", "segment10type", "segment1type", "segment2", "segment2type", "segment3", "segment3type", "segment4", "segment4type", "segment5", "segment5type", "segment6", "segment6type", "segment7", "segment7type", "segment8", "segment8type", "segment9", "segment9type"]

    @field_validator('segment10type')
    def segment10type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Account', 'Class'):
            raise ValueError("must be one of enum values ('Account', 'Class')")
        return value

    @field_validator('segment1type')
    def segment1type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Account', 'Class'):
            raise ValueError("must be one of enum values ('Account', 'Class')")
        return value

    @field_validator('segment2type')
    def segment2type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Account', 'Class'):
            raise ValueError("must be one of enum values ('Account', 'Class')")
        return value

    @field_validator('segment3type')
    def segment3type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Account', 'Class'):
            raise ValueError("must be one of enum values ('Account', 'Class')")
        return value

    @field_validator('segment4type')
    def segment4type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Account', 'Class'):
            raise ValueError("must be one of enum values ('Account', 'Class')")
        return value

    @field_validator('segment5type')
    def segment5type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Account', 'Class'):
            raise ValueError("must be one of enum values ('Account', 'Class')")
        return value

    @field_validator('segment6type')
    def segment6type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Account', 'Class'):
            raise ValueError("must be one of enum values ('Account', 'Class')")
        return value

    @field_validator('segment7type')
    def segment7type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Account', 'Class'):
            raise ValueError("must be one of enum values ('Account', 'Class')")
        return value

    @field_validator('segment8type')
    def segment8type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Account', 'Class'):
            raise ValueError("must be one of enum values ('Account', 'Class')")
        return value

    @field_validator('segment9type')
    def segment9type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Account', 'Class'):
            raise ValueError("must be one of enum values ('Account', 'Class')")
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
        """Create an instance of GLCaption from a JSON string"""
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
        # set to None if segment10type (nullable) is None
        # and model_fields_set contains the field
        if self.segment10type is None and "segment10type" in self.model_fields_set:
            _dict['segment10type'] = None

        # set to None if segment1type (nullable) is None
        # and model_fields_set contains the field
        if self.segment1type is None and "segment1type" in self.model_fields_set:
            _dict['segment1type'] = None

        # set to None if segment2type (nullable) is None
        # and model_fields_set contains the field
        if self.segment2type is None and "segment2type" in self.model_fields_set:
            _dict['segment2type'] = None

        # set to None if segment3type (nullable) is None
        # and model_fields_set contains the field
        if self.segment3type is None and "segment3type" in self.model_fields_set:
            _dict['segment3type'] = None

        # set to None if segment4type (nullable) is None
        # and model_fields_set contains the field
        if self.segment4type is None and "segment4type" in self.model_fields_set:
            _dict['segment4type'] = None

        # set to None if segment5type (nullable) is None
        # and model_fields_set contains the field
        if self.segment5type is None and "segment5type" in self.model_fields_set:
            _dict['segment5type'] = None

        # set to None if segment6type (nullable) is None
        # and model_fields_set contains the field
        if self.segment6type is None and "segment6type" in self.model_fields_set:
            _dict['segment6type'] = None

        # set to None if segment7type (nullable) is None
        # and model_fields_set contains the field
        if self.segment7type is None and "segment7type" in self.model_fields_set:
            _dict['segment7type'] = None

        # set to None if segment8type (nullable) is None
        # and model_fields_set contains the field
        if self.segment8type is None and "segment8type" in self.model_fields_set:
            _dict['segment8type'] = None

        # set to None if segment9type (nullable) is None
        # and model_fields_set contains the field
        if self.segment9type is None and "segment9type" in self.model_fields_set:
            _dict['segment9type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GLCaption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in GLCaption) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "cogs1": obj.get("cogs1"),
            "cogs10": obj.get("cogs10"),
            "cogs2": obj.get("cogs2"),
            "cogs3": obj.get("cogs3"),
            "cogs4": obj.get("cogs4"),
            "cogs5": obj.get("cogs5"),
            "cogs6": obj.get("cogs6"),
            "cogs7": obj.get("cogs7"),
            "cogs8": obj.get("cogs8"),
            "cogs9": obj.get("cogs9"),
            "id": obj.get("id"),
            "segment1": obj.get("segment1"),
            "segment10": obj.get("segment10"),
            "segment10type": obj.get("segment10type"),
            "segment1type": obj.get("segment1type"),
            "segment2": obj.get("segment2"),
            "segment2type": obj.get("segment2type"),
            "segment3": obj.get("segment3"),
            "segment3type": obj.get("segment3type"),
            "segment4": obj.get("segment4"),
            "segment4type": obj.get("segment4type"),
            "segment5": obj.get("segment5"),
            "segment5type": obj.get("segment5type"),
            "segment6": obj.get("segment6"),
            "segment6type": obj.get("segment6type"),
            "segment7": obj.get("segment7"),
            "segment7type": obj.get("segment7type"),
            "segment8": obj.get("segment8"),
            "segment8type": obj.get("segment8type"),
            "segment9": obj.get("segment9"),
            "segment9type": obj.get("segment9type")
        })
        return _obj


