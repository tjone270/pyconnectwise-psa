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

class NotificationRecipient(BaseModel):
    """
    NotificationRecipient
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    agreement_flag: Optional[StrictBool] = Field(default=None, alias="agreementFlag")
    config_flag: Optional[StrictBool] = Field(default=None, alias="configFlag")
    external_flag: Optional[StrictBool] = Field(default=None, alias="externalFlag")
    id: Optional[StrictInt] = None
    identifier: Optional[StrictStr] = None
    invoice_flag: Optional[StrictBool] = Field(default=None, alias="invoiceFlag")
    knowledge_base_flag: Optional[StrictBool] = Field(default=None, alias="knowledgeBaseFlag")
    member_flag: Optional[StrictBool] = Field(default=None, alias="memberFlag")
    msp_flag: Optional[StrictBool] = Field(default=None, alias="mspFlag")
    name: Optional[StrictStr] = None
    procurement_flag: Optional[StrictBool] = Field(default=None, alias="procurementFlag")
    project_flag: Optional[StrictBool] = Field(default=None, alias="projectFlag")
    sales_flag: Optional[StrictBool] = Field(default=None, alias="salesFlag")
    service_flag: Optional[StrictBool] = Field(default=None, alias="serviceFlag")
    track_flag: Optional[StrictBool] = Field(default=None, alias="trackFlag")
    __properties: ClassVar[List[str]] = ["_info", "agreementFlag", "configFlag", "externalFlag", "id", "identifier", "invoiceFlag", "knowledgeBaseFlag", "memberFlag", "mspFlag", "name", "procurementFlag", "projectFlag", "salesFlag", "serviceFlag", "trackFlag"]

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
        """Create an instance of NotificationRecipient from a JSON string"""
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
        # set to None if agreement_flag (nullable) is None
        # and model_fields_set contains the field
        if self.agreement_flag is None and "agreement_flag" in self.model_fields_set:
            _dict['agreementFlag'] = None

        # set to None if config_flag (nullable) is None
        # and model_fields_set contains the field
        if self.config_flag is None and "config_flag" in self.model_fields_set:
            _dict['configFlag'] = None

        # set to None if external_flag (nullable) is None
        # and model_fields_set contains the field
        if self.external_flag is None and "external_flag" in self.model_fields_set:
            _dict['externalFlag'] = None

        # set to None if invoice_flag (nullable) is None
        # and model_fields_set contains the field
        if self.invoice_flag is None and "invoice_flag" in self.model_fields_set:
            _dict['invoiceFlag'] = None

        # set to None if knowledge_base_flag (nullable) is None
        # and model_fields_set contains the field
        if self.knowledge_base_flag is None and "knowledge_base_flag" in self.model_fields_set:
            _dict['knowledgeBaseFlag'] = None

        # set to None if member_flag (nullable) is None
        # and model_fields_set contains the field
        if self.member_flag is None and "member_flag" in self.model_fields_set:
            _dict['memberFlag'] = None

        # set to None if msp_flag (nullable) is None
        # and model_fields_set contains the field
        if self.msp_flag is None and "msp_flag" in self.model_fields_set:
            _dict['mspFlag'] = None

        # set to None if procurement_flag (nullable) is None
        # and model_fields_set contains the field
        if self.procurement_flag is None and "procurement_flag" in self.model_fields_set:
            _dict['procurementFlag'] = None

        # set to None if project_flag (nullable) is None
        # and model_fields_set contains the field
        if self.project_flag is None and "project_flag" in self.model_fields_set:
            _dict['projectFlag'] = None

        # set to None if sales_flag (nullable) is None
        # and model_fields_set contains the field
        if self.sales_flag is None and "sales_flag" in self.model_fields_set:
            _dict['salesFlag'] = None

        # set to None if service_flag (nullable) is None
        # and model_fields_set contains the field
        if self.service_flag is None and "service_flag" in self.model_fields_set:
            _dict['serviceFlag'] = None

        # set to None if track_flag (nullable) is None
        # and model_fields_set contains the field
        if self.track_flag is None and "track_flag" in self.model_fields_set:
            _dict['trackFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of NotificationRecipient from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in NotificationRecipient) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "agreementFlag": obj.get("agreementFlag"),
            "configFlag": obj.get("configFlag"),
            "externalFlag": obj.get("externalFlag"),
            "id": obj.get("id"),
            "identifier": obj.get("identifier"),
            "invoiceFlag": obj.get("invoiceFlag"),
            "knowledgeBaseFlag": obj.get("knowledgeBaseFlag"),
            "memberFlag": obj.get("memberFlag"),
            "mspFlag": obj.get("mspFlag"),
            "name": obj.get("name"),
            "procurementFlag": obj.get("procurementFlag"),
            "projectFlag": obj.get("projectFlag"),
            "salesFlag": obj.get("salesFlag"),
            "serviceFlag": obj.get("serviceFlag"),
            "trackFlag": obj.get("trackFlag")
        })
        return _obj


