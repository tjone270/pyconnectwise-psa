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
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from connectwise_psa.models.invoice_reference import InvoiceReference
from connectwise_psa.models.wise_pay_payment import WisePayPayment
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UnpostedPayments(BaseModel):
    """
    UnpostedPayments
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    a_r_payment_account: Optional[StrictStr] = Field(default=None, alias="aRPaymentAccount")
    amount: Optional[Union[StrictFloat, StrictInt]] = None
    applied_by: Optional[StrictStr] = Field(default=None, alias="appliedBy")
    id: Optional[StrictInt] = None
    invoice: Optional[InvoiceReference] = None
    payment_account: Optional[StrictStr] = Field(default=None, alias="paymentAccount")
    payment_date: Optional[StrictStr] = Field(default=None, alias="paymentDate")
    payment_sync_date: Optional[StrictStr] = Field(default=None, alias="paymentSyncDate")
    payment_sync_status: Optional[StrictStr] = Field(default=None, alias="paymentSyncStatus")
    source: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    wise_pay_payment: Optional[WisePayPayment] = Field(default=None, alias="wisePayPayment")
    __properties: ClassVar[List[str]] = ["_info", "aRPaymentAccount", "amount", "appliedBy", "id", "invoice", "paymentAccount", "paymentDate", "paymentSyncDate", "paymentSyncStatus", "source", "type", "wisePayPayment"]

    @field_validator('source')
    def source_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Default', 'WisePay'):
            raise ValueError("must be one of enum values ('Default', 'WisePay')")
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
        """Create an instance of UnpostedPayments from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of invoice
        if self.invoice:
            _dict['invoice'] = self.invoice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of wise_pay_payment
        if self.wise_pay_payment:
            _dict['wisePayPayment'] = self.wise_pay_payment.to_dict()
        # set to None if amount (nullable) is None
        # and model_fields_set contains the field
        if self.amount is None and "amount" in self.model_fields_set:
            _dict['amount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UnpostedPayments from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in UnpostedPayments) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "aRPaymentAccount": obj.get("aRPaymentAccount"),
            "amount": obj.get("amount"),
            "appliedBy": obj.get("appliedBy"),
            "id": obj.get("id"),
            "invoice": InvoiceReference.from_dict(obj.get("invoice")) if obj.get("invoice") is not None else None,
            "paymentAccount": obj.get("paymentAccount"),
            "paymentDate": obj.get("paymentDate"),
            "paymentSyncDate": obj.get("paymentSyncDate"),
            "paymentSyncStatus": obj.get("paymentSyncStatus"),
            "source": obj.get("source"),
            "type": obj.get("type"),
            "wisePayPayment": WisePayPayment.from_dict(obj.get("wisePayPayment")) if obj.get("wisePayPayment") is not None else None
        })
        return _obj

