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

class MarketplaceImport(BaseModel):
    """
    MarketplaceImport
    """ # noqa: E501
    id: Optional[StrictInt] = None
    marketplace_import_type: Optional[StrictStr] = Field(default=None, alias="marketplaceImportType")
    marketplace_object: Optional[List[Any]] = Field(default=None, alias="marketplaceObject")
    required_fields: Optional[List[StrictStr]] = Field(default=None, alias="requiredFields")
    __properties: ClassVar[List[str]] = ["id", "marketplaceImportType", "marketplaceObject", "requiredFields"]

    @field_validator('marketplace_import_type')
    def marketplace_import_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Agreements', 'Configurations', 'CRMSurveys', 'CustomReports', 'CustomerPortalTypes', 'HTMLEmailTemplates', 'Products', 'ProjectBoards', 'ProjectTemplates', 'ReportWriterReports', 'ServiceBoards', 'TicketTemplates', 'Views'):
            raise ValueError("must be one of enum values ('Agreements', 'Configurations', 'CRMSurveys', 'CustomReports', 'CustomerPortalTypes', 'HTMLEmailTemplates', 'Products', 'ProjectBoards', 'ProjectTemplates', 'ReportWriterReports', 'ServiceBoards', 'TicketTemplates', 'Views')")
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
        """Create an instance of MarketplaceImport from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of MarketplaceImport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in MarketplaceImport) in the input: " + _key)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "marketplaceImportType": obj.get("marketplaceImportType"),
            "marketplaceObject": obj.get("marketplaceObject"),
            "requiredFields": obj.get("requiredFields")
        })
        return _obj


