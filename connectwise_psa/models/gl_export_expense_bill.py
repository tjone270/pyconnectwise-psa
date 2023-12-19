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
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from connectwise_psa.models.currency_reference import CurrencyReference
from connectwise_psa.models.gl_export_expense_bill_detail import GLExportExpenseBillDetail
from connectwise_psa.models.member_reference import MemberReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GLExportExpenseBill(BaseModel):
    """
    GLExportExpenseBill
    """ # noqa: E501
    ap_account_number: Optional[StrictStr] = Field(default=None, alias="apAccountNumber")
    currency: Optional[CurrencyReference] = None
    detail: Optional[List[GLExportExpenseBillDetail]] = None
    document_date: Optional[StrictStr] = Field(default=None, alias="documentDate")
    document_number: Optional[StrictStr] = Field(default=None, alias="documentNumber")
    document_type: Optional[StrictStr] = Field(default=None, alias="documentType")
    gl_class: Optional[StrictStr] = Field(default=None, alias="glClass")
    id: Optional[StrictInt] = None
    member: Optional[MemberReference] = None
    memo: Optional[StrictStr] = None
    total: Optional[Union[StrictFloat, StrictInt]] = None
    vendor_number: Optional[StrictStr] = Field(default=None, alias="vendorNumber")
    __properties: ClassVar[List[str]] = ["apAccountNumber", "currency", "detail", "documentDate", "documentNumber", "documentType", "glClass", "id", "member", "memo", "total", "vendorNumber"]

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
        """Create an instance of GLExportExpenseBill from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of currency
        if self.currency:
            _dict['currency'] = self.currency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in detail (list)
        _items = []
        if self.detail:
            for _item in self.detail:
                if _item:
                    _items.append(_item.to_dict())
            _dict['detail'] = _items
        # override the default output from pydantic by calling `to_dict()` of member
        if self.member:
            _dict['member'] = self.member.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GLExportExpenseBill from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in GLExportExpenseBill) in the input: " + _key)

        _obj = cls.model_validate({
            "apAccountNumber": obj.get("apAccountNumber"),
            "currency": CurrencyReference.from_dict(obj.get("currency")) if obj.get("currency") is not None else None,
            "detail": [GLExportExpenseBillDetail.from_dict(_item) for _item in obj.get("detail")] if obj.get("detail") is not None else None,
            "documentDate": obj.get("documentDate"),
            "documentNumber": obj.get("documentNumber"),
            "documentType": obj.get("documentType"),
            "glClass": obj.get("glClass"),
            "id": obj.get("id"),
            "member": MemberReference.from_dict(obj.get("member")) if obj.get("member") is not None else None,
            "memo": obj.get("memo"),
            "total": obj.get("total"),
            "vendorNumber": obj.get("vendorNumber")
        })
        return _obj

