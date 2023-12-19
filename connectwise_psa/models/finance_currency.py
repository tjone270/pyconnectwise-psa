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
from connectwise_psa.models.currency_code_reference import CurrencyCodeReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FinanceCurrency(BaseModel):
    """
    FinanceCurrency
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    currency_code: Optional[CurrencyCodeReference] = Field(default=None, alias="currencyCode")
    currency_identifier: StrictStr = Field(description=" Max length: 10;", alias="currencyIdentifier")
    decimal_separator: Optional[StrictStr] = Field(default=None, description=" Max length: 1;", alias="decimalSeparator")
    display_id_flag: Optional[StrictBool] = Field(default=None, alias="displayIdFlag")
    display_symbol_flag: Optional[StrictBool] = Field(default=None, alias="displaySymbolFlag")
    id: Optional[StrictInt] = None
    name: StrictStr = Field(description=" Max length: 50;")
    negative_parentheses_flag: Optional[StrictBool] = Field(default=None, alias="negativeParenthesesFlag")
    number_of_decimals: Optional[StrictInt] = Field(default=None, alias="numberOfDecimals")
    report_format: Optional[StrictStr] = Field(default=None, alias="reportFormat")
    right_align: Optional[StrictBool] = Field(default=None, alias="rightAlign")
    symbol: Optional[StrictStr] = Field(default=None, description=" Max length: 10;")
    thousands_separator: Optional[StrictStr] = Field(default=None, description=" Max length: 1;", alias="thousandsSeparator")
    __properties: ClassVar[List[str]] = ["_info", "currencyCode", "currencyIdentifier", "decimalSeparator", "displayIdFlag", "displaySymbolFlag", "id", "name", "negativeParenthesesFlag", "numberOfDecimals", "reportFormat", "rightAlign", "symbol", "thousandsSeparator"]

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
        """Create an instance of FinanceCurrency from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of currency_code
        if self.currency_code:
            _dict['currencyCode'] = self.currency_code.to_dict()
        # set to None if display_id_flag (nullable) is None
        # and model_fields_set contains the field
        if self.display_id_flag is None and "display_id_flag" in self.model_fields_set:
            _dict['displayIdFlag'] = None

        # set to None if display_symbol_flag (nullable) is None
        # and model_fields_set contains the field
        if self.display_symbol_flag is None and "display_symbol_flag" in self.model_fields_set:
            _dict['displaySymbolFlag'] = None

        # set to None if negative_parentheses_flag (nullable) is None
        # and model_fields_set contains the field
        if self.negative_parentheses_flag is None and "negative_parentheses_flag" in self.model_fields_set:
            _dict['negativeParenthesesFlag'] = None

        # set to None if number_of_decimals (nullable) is None
        # and model_fields_set contains the field
        if self.number_of_decimals is None and "number_of_decimals" in self.model_fields_set:
            _dict['numberOfDecimals'] = None

        # set to None if right_align (nullable) is None
        # and model_fields_set contains the field
        if self.right_align is None and "right_align" in self.model_fields_set:
            _dict['rightAlign'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FinanceCurrency from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in FinanceCurrency) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "currencyCode": CurrencyCodeReference.from_dict(obj.get("currencyCode")) if obj.get("currencyCode") is not None else None,
            "currencyIdentifier": obj.get("currencyIdentifier"),
            "decimalSeparator": obj.get("decimalSeparator"),
            "displayIdFlag": obj.get("displayIdFlag"),
            "displaySymbolFlag": obj.get("displaySymbolFlag"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "negativeParenthesesFlag": obj.get("negativeParenthesesFlag"),
            "numberOfDecimals": obj.get("numberOfDecimals"),
            "reportFormat": obj.get("reportFormat"),
            "rightAlign": obj.get("rightAlign"),
            "symbol": obj.get("symbol"),
            "thousandsSeparator": obj.get("thousandsSeparator")
        })
        return _obj


