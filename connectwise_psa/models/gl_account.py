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
from connectwise_psa.models.mapped_record_reference import MappedRecordReference
from connectwise_psa.models.mapped_type_reference import MappedTypeReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GLAccount(BaseModel):
    """
    GLAccount
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
    gl_type: Optional[StrictStr] = Field(alias="glType")
    id: Optional[StrictInt] = None
    inventory: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    mapped_record: MappedRecordReference = Field(alias="mappedRecord")
    mapped_type: MappedTypeReference = Field(alias="mappedType")
    product_id: Optional[StrictStr] = Field(default=None, description=" Max length: 255;", alias="productId")
    sales_code: Optional[StrictStr] = Field(default=None, description=" Max length: 255;", alias="salesCode")
    segment1: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    segment10: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    segment2: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    segment3: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    segment4: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    segment5: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    segment6: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    segment7: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    segment8: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    segment9: Optional[StrictStr] = Field(default=None, description=" Max length: 255;")
    __properties: ClassVar[List[str]] = ["_info", "cogs1", "cogs10", "cogs2", "cogs3", "cogs4", "cogs5", "cogs6", "cogs7", "cogs8", "cogs9", "glType", "id", "inventory", "mappedRecord", "mappedType", "productId", "salesCode", "segment1", "segment10", "segment2", "segment3", "segment4", "segment5", "segment6", "segment7", "segment8", "segment9"]

    @field_validator('gl_type')
    def gl_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('AP', 'AR', 'EE', 'EI', 'EO', 'IA', 'IT', 'P', 'PF', 'R', 'RA', 'RD', 'RE', 'RP', 'ST', 'SD', 'ET', 'FT', 'PT', 'WP', 'WR'):
            raise ValueError("must be one of enum values ('AP', 'AR', 'EE', 'EI', 'EO', 'IA', 'IT', 'P', 'PF', 'R', 'RA', 'RD', 'RE', 'RP', 'ST', 'SD', 'ET', 'FT', 'PT', 'WP', 'WR')")
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
        """Create an instance of GLAccount from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of mapped_record
        if self.mapped_record:
            _dict['mappedRecord'] = self.mapped_record.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mapped_type
        if self.mapped_type:
            _dict['mappedType'] = self.mapped_type.to_dict()
        # set to None if gl_type (nullable) is None
        # and model_fields_set contains the field
        if self.gl_type is None and "gl_type" in self.model_fields_set:
            _dict['glType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GLAccount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in GLAccount) in the input: " + _key)

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
            "glType": obj.get("glType"),
            "id": obj.get("id"),
            "inventory": obj.get("inventory"),
            "mappedRecord": MappedRecordReference.from_dict(obj.get("mappedRecord")) if obj.get("mappedRecord") is not None else None,
            "mappedType": MappedTypeReference.from_dict(obj.get("mappedType")) if obj.get("mappedType") is not None else None,
            "productId": obj.get("productId"),
            "salesCode": obj.get("salesCode"),
            "segment1": obj.get("segment1"),
            "segment10": obj.get("segment10"),
            "segment2": obj.get("segment2"),
            "segment3": obj.get("segment3"),
            "segment4": obj.get("segment4"),
            "segment5": obj.get("segment5"),
            "segment6": obj.get("segment6"),
            "segment7": obj.get("segment7"),
            "segment8": obj.get("segment8"),
            "segment9": obj.get("segment9")
        })
        return _obj


