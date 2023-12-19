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

class OpportunityToServiceTicketConversion(BaseModel):
    """
    OpportunityToServiceTicketConversion
    """ # noqa: E501
    include_all_documents_flag: Optional[StrictBool] = Field(default=None, alias="includeAllDocumentsFlag")
    include_all_notes_flag: Optional[StrictBool] = Field(default=None, alias="includeAllNotesFlag")
    include_all_products_flag: Optional[StrictBool] = Field(default=None, alias="includeAllProductsFlag")
    include_document_ids: Optional[List[StrictInt]] = Field(default=None, alias="includeDocumentIds")
    include_note_ids: Optional[List[StrictInt]] = Field(default=None, alias="includeNoteIds")
    include_product_ids: Optional[List[StrictInt]] = Field(default=None, alias="includeProductIds")
    summary: Optional[StrictStr] = None
    ticket_id: Optional[StrictInt] = Field(default=None, alias="ticketId")
    __properties: ClassVar[List[str]] = ["includeAllDocumentsFlag", "includeAllNotesFlag", "includeAllProductsFlag", "includeDocumentIds", "includeNoteIds", "includeProductIds", "summary", "ticketId"]

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
        """Create an instance of OpportunityToServiceTicketConversion from a JSON string"""
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
        # set to None if include_all_documents_flag (nullable) is None
        # and model_fields_set contains the field
        if self.include_all_documents_flag is None and "include_all_documents_flag" in self.model_fields_set:
            _dict['includeAllDocumentsFlag'] = None

        # set to None if include_all_notes_flag (nullable) is None
        # and model_fields_set contains the field
        if self.include_all_notes_flag is None and "include_all_notes_flag" in self.model_fields_set:
            _dict['includeAllNotesFlag'] = None

        # set to None if include_all_products_flag (nullable) is None
        # and model_fields_set contains the field
        if self.include_all_products_flag is None and "include_all_products_flag" in self.model_fields_set:
            _dict['includeAllProductsFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OpportunityToServiceTicketConversion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in OpportunityToServiceTicketConversion) in the input: " + _key)

        _obj = cls.model_validate({
            "includeAllDocumentsFlag": obj.get("includeAllDocumentsFlag"),
            "includeAllNotesFlag": obj.get("includeAllNotesFlag"),
            "includeAllProductsFlag": obj.get("includeAllProductsFlag"),
            "includeDocumentIds": obj.get("includeDocumentIds"),
            "includeNoteIds": obj.get("includeNoteIds"),
            "includeProductIds": obj.get("includeProductIds"),
            "summary": obj.get("summary"),
            "ticketId": obj.get("ticketId")
        })
        return _obj

