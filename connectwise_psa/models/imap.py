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
from connectwise_psa.models.email_connector_reference import EmailConnectorReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Imap(BaseModel):
    """
    Imap
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    email_connector: Optional[EmailConnectorReference] = Field(default=None, alias="emailConnector")
    failed_folder: StrictStr = Field(description=" Max length: 40;", alias="failedFolder")
    id: Optional[StrictInt] = None
    imap_name: StrictStr = Field(description=" Max length: 40;", alias="imapName")
    name: StrictStr = Field(description=" Max length: 200;")
    password: Optional[StrictStr] = Field(default=None, description=" Max length: 80;")
    port: Optional[StrictInt]
    processed_name: StrictStr = Field(description=" Max length: 40;", alias="processedName")
    server: StrictStr = Field(description=" Max length: 200;")
    ssl_flag: Optional[StrictBool] = Field(default=None, alias="sslFlag")
    user_name: StrictStr = Field(description=" Max length: 80;", alias="userName")
    __properties: ClassVar[List[str]] = ["_info", "emailConnector", "failedFolder", "id", "imapName", "name", "password", "port", "processedName", "server", "sslFlag", "userName"]

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
        """Create an instance of Imap from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of email_connector
        if self.email_connector:
            _dict['emailConnector'] = self.email_connector.to_dict()
        # set to None if port (nullable) is None
        # and model_fields_set contains the field
        if self.port is None and "port" in self.model_fields_set:
            _dict['port'] = None

        # set to None if ssl_flag (nullable) is None
        # and model_fields_set contains the field
        if self.ssl_flag is None and "ssl_flag" in self.model_fields_set:
            _dict['sslFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Imap from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Imap) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "emailConnector": EmailConnectorReference.from_dict(obj.get("emailConnector")) if obj.get("emailConnector") is not None else None,
            "failedFolder": obj.get("failedFolder"),
            "id": obj.get("id"),
            "imapName": obj.get("imapName"),
            "name": obj.get("name"),
            "password": obj.get("password"),
            "port": obj.get("port"),
            "processedName": obj.get("processedName"),
            "server": obj.get("server"),
            "sslFlag": obj.get("sslFlag"),
            "userName": obj.get("userName")
        })
        return _obj


