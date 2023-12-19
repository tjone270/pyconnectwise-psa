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
from connectwise_psa.models.document_type_reference import DocumentTypeReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class DocumentInfo(BaseModel):
    """
    DocumentInfo
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    created_on_date: Optional[StrictStr] = Field(default=None, alias="createdOnDate")
    document_type: Optional[DocumentTypeReference] = Field(default=None, alias="documentType")
    file_name: Optional[StrictStr] = Field(default=None, alias="fileName")
    guid: Optional[StrictStr] = None
    html_template_flag: Optional[StrictBool] = Field(default=None, alias="htmlTemplateFlag")
    id: Optional[StrictInt] = None
    image_flag: Optional[StrictBool] = Field(default=None, alias="imageFlag")
    link_flag: Optional[StrictBool] = Field(default=None, alias="linkFlag")
    owner: Optional[StrictStr] = None
    public_flag: Optional[StrictBool] = Field(default=None, alias="publicFlag")
    read_only_flag: Optional[StrictBool] = Field(default=None, alias="readOnlyFlag")
    server_file_name: Optional[StrictStr] = Field(default=None, alias="serverFileName")
    size: Optional[StrictInt] = None
    title: Optional[StrictStr] = None
    url_flag: Optional[StrictBool] = Field(default=None, alias="urlFlag")
    __properties: ClassVar[List[str]] = ["_info", "createdOnDate", "documentType", "fileName", "guid", "htmlTemplateFlag", "id", "imageFlag", "linkFlag", "owner", "publicFlag", "readOnlyFlag", "serverFileName", "size", "title", "urlFlag"]

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
        """Create an instance of DocumentInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of document_type
        if self.document_type:
            _dict['documentType'] = self.document_type.to_dict()
        # set to None if html_template_flag (nullable) is None
        # and model_fields_set contains the field
        if self.html_template_flag is None and "html_template_flag" in self.model_fields_set:
            _dict['htmlTemplateFlag'] = None

        # set to None if image_flag (nullable) is None
        # and model_fields_set contains the field
        if self.image_flag is None and "image_flag" in self.model_fields_set:
            _dict['imageFlag'] = None

        # set to None if link_flag (nullable) is None
        # and model_fields_set contains the field
        if self.link_flag is None and "link_flag" in self.model_fields_set:
            _dict['linkFlag'] = None

        # set to None if public_flag (nullable) is None
        # and model_fields_set contains the field
        if self.public_flag is None and "public_flag" in self.model_fields_set:
            _dict['publicFlag'] = None

        # set to None if read_only_flag (nullable) is None
        # and model_fields_set contains the field
        if self.read_only_flag is None and "read_only_flag" in self.model_fields_set:
            _dict['readOnlyFlag'] = None

        # set to None if size (nullable) is None
        # and model_fields_set contains the field
        if self.size is None and "size" in self.model_fields_set:
            _dict['size'] = None

        # set to None if url_flag (nullable) is None
        # and model_fields_set contains the field
        if self.url_flag is None and "url_flag" in self.model_fields_set:
            _dict['urlFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of DocumentInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in DocumentInfo) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "createdOnDate": obj.get("createdOnDate"),
            "documentType": DocumentTypeReference.from_dict(obj.get("documentType")) if obj.get("documentType") is not None else None,
            "fileName": obj.get("fileName"),
            "guid": obj.get("guid"),
            "htmlTemplateFlag": obj.get("htmlTemplateFlag"),
            "id": obj.get("id"),
            "imageFlag": obj.get("imageFlag"),
            "linkFlag": obj.get("linkFlag"),
            "owner": obj.get("owner"),
            "publicFlag": obj.get("publicFlag"),
            "readOnlyFlag": obj.get("readOnlyFlag"),
            "serverFileName": obj.get("serverFileName"),
            "size": obj.get("size"),
            "title": obj.get("title"),
            "urlFlag": obj.get("urlFlag")
        })
        return _obj


