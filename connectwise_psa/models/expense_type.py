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
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ExpenseType(BaseModel):
    """
    ExpenseType
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    advanced_amount_flag: Optional[StrictBool] = Field(default=None, alias="advancedAmountFlag")
    amount_caption: StrictStr = Field(alias="amountCaption")
    bill_expenses: Optional[StrictStr] = Field(alias="billExpenses")
    default_flag: Optional[StrictBool] = Field(default=None, alias="defaultFlag")
    id: Optional[StrictInt] = None
    inactive_flag: Optional[StrictBool] = Field(default=None, alias="inactiveFlag")
    integration_x_ref: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="integrationXRef")
    invoice_markup_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="invoiceMarkupAmount")
    invoice_markup_option: Optional[StrictStr] = Field(alias="invoiceMarkupOption")
    max_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="maxAmount")
    mileage_flag: Optional[StrictBool] = Field(default=None, alias="mileageFlag")
    name: StrictStr = Field(description=" Max length: 30;")
    quantity_flag: Optional[StrictBool] = Field(default=None, alias="quantityFlag")
    reimbursement_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="reimbursementRate")
    __properties: ClassVar[List[str]] = ["_info", "advancedAmountFlag", "amountCaption", "billExpenses", "defaultFlag", "id", "inactiveFlag", "integrationXRef", "invoiceMarkupAmount", "invoiceMarkupOption", "maxAmount", "mileageFlag", "name", "quantityFlag", "reimbursementRate"]

    @field_validator('bill_expenses')
    def bill_expenses_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Billable', 'DoNotBill', 'NoCharge', 'NoDefault'):
            raise ValueError("must be one of enum values ('Billable', 'DoNotBill', 'NoCharge', 'NoDefault')")
        return value

    @field_validator('invoice_markup_option')
    def invoice_markup_option_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Amount', 'Mile', 'Percent'):
            raise ValueError("must be one of enum values ('Amount', 'Mile', 'Percent')")
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
        """Create an instance of ExpenseType from a JSON string"""
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
        # set to None if advanced_amount_flag (nullable) is None
        # and model_fields_set contains the field
        if self.advanced_amount_flag is None and "advanced_amount_flag" in self.model_fields_set:
            _dict['advancedAmountFlag'] = None

        # set to None if bill_expenses (nullable) is None
        # and model_fields_set contains the field
        if self.bill_expenses is None and "bill_expenses" in self.model_fields_set:
            _dict['billExpenses'] = None

        # set to None if default_flag (nullable) is None
        # and model_fields_set contains the field
        if self.default_flag is None and "default_flag" in self.model_fields_set:
            _dict['defaultFlag'] = None

        # set to None if inactive_flag (nullable) is None
        # and model_fields_set contains the field
        if self.inactive_flag is None and "inactive_flag" in self.model_fields_set:
            _dict['inactiveFlag'] = None

        # set to None if invoice_markup_amount (nullable) is None
        # and model_fields_set contains the field
        if self.invoice_markup_amount is None and "invoice_markup_amount" in self.model_fields_set:
            _dict['invoiceMarkupAmount'] = None

        # set to None if invoice_markup_option (nullable) is None
        # and model_fields_set contains the field
        if self.invoice_markup_option is None and "invoice_markup_option" in self.model_fields_set:
            _dict['invoiceMarkupOption'] = None

        # set to None if max_amount (nullable) is None
        # and model_fields_set contains the field
        if self.max_amount is None and "max_amount" in self.model_fields_set:
            _dict['maxAmount'] = None

        # set to None if mileage_flag (nullable) is None
        # and model_fields_set contains the field
        if self.mileage_flag is None and "mileage_flag" in self.model_fields_set:
            _dict['mileageFlag'] = None

        # set to None if quantity_flag (nullable) is None
        # and model_fields_set contains the field
        if self.quantity_flag is None and "quantity_flag" in self.model_fields_set:
            _dict['quantityFlag'] = None

        # set to None if reimbursement_rate (nullable) is None
        # and model_fields_set contains the field
        if self.reimbursement_rate is None and "reimbursement_rate" in self.model_fields_set:
            _dict['reimbursementRate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ExpenseType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ExpenseType) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "advancedAmountFlag": obj.get("advancedAmountFlag"),
            "amountCaption": obj.get("amountCaption"),
            "billExpenses": obj.get("billExpenses"),
            "defaultFlag": obj.get("defaultFlag"),
            "id": obj.get("id"),
            "inactiveFlag": obj.get("inactiveFlag"),
            "integrationXRef": obj.get("integrationXRef"),
            "invoiceMarkupAmount": obj.get("invoiceMarkupAmount"),
            "invoiceMarkupOption": obj.get("invoiceMarkupOption"),
            "maxAmount": obj.get("maxAmount"),
            "mileageFlag": obj.get("mileageFlag"),
            "name": obj.get("name"),
            "quantityFlag": obj.get("quantityFlag"),
            "reimbursementRate": obj.get("reimbursementRate")
        })
        return _obj


