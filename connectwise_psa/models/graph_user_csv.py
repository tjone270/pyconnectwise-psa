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
from connectwise_psa.models.manager import Manager
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GraphUserCsv(BaseModel):
    """
    GraphUserCsv
    """ # noqa: E501
    account_enabled: Optional[StrictBool] = Field(default=None, alias="accountEnabled")
    address: Optional[StrictStr] = None
    city: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    department: Optional[StrictStr] = None
    display_name: Optional[StrictStr] = Field(default=None, alias="displayName")
    employee_type: Optional[StrictStr] = Field(default=None, alias="employeeType")
    first_name: Optional[StrictStr] = Field(default=None, alias="firstName")
    id: Optional[StrictStr] = None
    is_matched_contact: Optional[StrictBool] = Field(default=None, alias="isMatchedContact")
    job_title: Optional[StrictStr] = Field(default=None, alias="jobTitle")
    last_name: Optional[StrictStr] = Field(default=None, alias="lastName")
    mail: Optional[StrictStr] = None
    manage_contact_name: Optional[StrictStr] = Field(default=None, alias="manageContactName")
    manage_contact_rec_id: Optional[StrictInt] = Field(default=None, alias="manageContactRecId")
    manager: Optional[Manager] = None
    mobile_phone: Optional[StrictStr] = Field(default=None, alias="mobilePhone")
    nick_name: Optional[StrictStr] = Field(default=None, alias="nickName")
    postal_code: Optional[StrictStr] = Field(default=None, alias="postalCode")
    principal_name: Optional[StrictStr] = Field(default=None, alias="principalName")
    proxy_addresses: Optional[List[StrictStr]] = Field(default=None, alias="proxyAddresses")
    state: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["accountEnabled", "address", "city", "country", "department", "displayName", "employeeType", "firstName", "id", "isMatchedContact", "jobTitle", "lastName", "mail", "manageContactName", "manageContactRecId", "manager", "mobilePhone", "nickName", "postalCode", "principalName", "proxyAddresses", "state"]

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
        """Create an instance of GraphUserCsv from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of manager
        if self.manager:
            _dict['manager'] = self.manager.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GraphUserCsv from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in GraphUserCsv) in the input: " + _key)

        _obj = cls.model_validate({
            "accountEnabled": obj.get("accountEnabled"),
            "address": obj.get("address"),
            "city": obj.get("city"),
            "country": obj.get("country"),
            "department": obj.get("department"),
            "displayName": obj.get("displayName"),
            "employeeType": obj.get("employeeType"),
            "firstName": obj.get("firstName"),
            "id": obj.get("id"),
            "isMatchedContact": obj.get("isMatchedContact"),
            "jobTitle": obj.get("jobTitle"),
            "lastName": obj.get("lastName"),
            "mail": obj.get("mail"),
            "manageContactName": obj.get("manageContactName"),
            "manageContactRecId": obj.get("manageContactRecId"),
            "manager": Manager.from_dict(obj.get("manager")) if obj.get("manager") is not None else None,
            "mobilePhone": obj.get("mobilePhone"),
            "nickName": obj.get("nickName"),
            "postalCode": obj.get("postalCode"),
            "principalName": obj.get("principalName"),
            "proxyAddresses": obj.get("proxyAddresses"),
            "state": obj.get("state")
        })
        return _obj


