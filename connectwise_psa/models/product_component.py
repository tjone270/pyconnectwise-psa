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
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from connectwise_psa.models.catalog_item_reference import CatalogItemReference
from connectwise_psa.models.company_reference import CompanyReference
from connectwise_psa.models.product_item_reference import ProductItemReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ProductComponent(BaseModel):
    """
    ProductComponent
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    catalog_item: Optional[CatalogItemReference] = Field(default=None, alias="catalogItem")
    cost: Optional[Union[StrictFloat, StrictInt]] = None
    hide_description_flag: Optional[StrictBool] = Field(default=None, alias="hideDescriptionFlag")
    hide_extended_price_flag: Optional[StrictBool] = Field(default=None, alias="hideExtendedPriceFlag")
    hide_item_identifier_flag: Optional[StrictBool] = Field(default=None, alias="hideItemIdentifierFlag")
    hide_price_flag: Optional[StrictBool] = Field(default=None, alias="hidePriceFlag")
    hide_quantity_flag: Optional[StrictBool] = Field(default=None, alias="hideQuantityFlag")
    id: Optional[StrictInt] = None
    parent_product_item: Optional[ProductItemReference] = Field(default=None, alias="parentProductItem")
    price: Optional[Union[StrictFloat, StrictInt]] = None
    product_item: Optional[ProductItemReference] = Field(default=None, alias="productItem")
    quantity: Optional[Union[StrictFloat, StrictInt]]
    sequence_number: Optional[StrictInt] = Field(default=None, description=" Required On Updates;", alias="sequenceNumber")
    vendor: Optional[CompanyReference] = None
    __properties: ClassVar[List[str]] = ["_info", "catalogItem", "cost", "hideDescriptionFlag", "hideExtendedPriceFlag", "hideItemIdentifierFlag", "hidePriceFlag", "hideQuantityFlag", "id", "parentProductItem", "price", "productItem", "quantity", "sequenceNumber", "vendor"]

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
        """Create an instance of ProductComponent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of catalog_item
        if self.catalog_item:
            _dict['catalogItem'] = self.catalog_item.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parent_product_item
        if self.parent_product_item:
            _dict['parentProductItem'] = self.parent_product_item.to_dict()
        # override the default output from pydantic by calling `to_dict()` of product_item
        if self.product_item:
            _dict['productItem'] = self.product_item.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vendor
        if self.vendor:
            _dict['vendor'] = self.vendor.to_dict()
        # set to None if cost (nullable) is None
        # and model_fields_set contains the field
        if self.cost is None and "cost" in self.model_fields_set:
            _dict['cost'] = None

        # set to None if hide_description_flag (nullable) is None
        # and model_fields_set contains the field
        if self.hide_description_flag is None and "hide_description_flag" in self.model_fields_set:
            _dict['hideDescriptionFlag'] = None

        # set to None if hide_extended_price_flag (nullable) is None
        # and model_fields_set contains the field
        if self.hide_extended_price_flag is None and "hide_extended_price_flag" in self.model_fields_set:
            _dict['hideExtendedPriceFlag'] = None

        # set to None if hide_item_identifier_flag (nullable) is None
        # and model_fields_set contains the field
        if self.hide_item_identifier_flag is None and "hide_item_identifier_flag" in self.model_fields_set:
            _dict['hideItemIdentifierFlag'] = None

        # set to None if hide_price_flag (nullable) is None
        # and model_fields_set contains the field
        if self.hide_price_flag is None and "hide_price_flag" in self.model_fields_set:
            _dict['hidePriceFlag'] = None

        # set to None if hide_quantity_flag (nullable) is None
        # and model_fields_set contains the field
        if self.hide_quantity_flag is None and "hide_quantity_flag" in self.model_fields_set:
            _dict['hideQuantityFlag'] = None

        # set to None if price (nullable) is None
        # and model_fields_set contains the field
        if self.price is None and "price" in self.model_fields_set:
            _dict['price'] = None

        # set to None if quantity (nullable) is None
        # and model_fields_set contains the field
        if self.quantity is None and "quantity" in self.model_fields_set:
            _dict['quantity'] = None

        # set to None if sequence_number (nullable) is None
        # and model_fields_set contains the field
        if self.sequence_number is None and "sequence_number" in self.model_fields_set:
            _dict['sequenceNumber'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProductComponent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ProductComponent) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "catalogItem": CatalogItemReference.from_dict(obj.get("catalogItem")) if obj.get("catalogItem") is not None else None,
            "cost": obj.get("cost"),
            "hideDescriptionFlag": obj.get("hideDescriptionFlag"),
            "hideExtendedPriceFlag": obj.get("hideExtendedPriceFlag"),
            "hideItemIdentifierFlag": obj.get("hideItemIdentifierFlag"),
            "hidePriceFlag": obj.get("hidePriceFlag"),
            "hideQuantityFlag": obj.get("hideQuantityFlag"),
            "id": obj.get("id"),
            "parentProductItem": ProductItemReference.from_dict(obj.get("parentProductItem")) if obj.get("parentProductItem") is not None else None,
            "price": obj.get("price"),
            "productItem": ProductItemReference.from_dict(obj.get("productItem")) if obj.get("productItem") is not None else None,
            "quantity": obj.get("quantity"),
            "sequenceNumber": obj.get("sequenceNumber"),
            "vendor": CompanyReference.from_dict(obj.get("vendor")) if obj.get("vendor") is not None else None
        })
        return _obj


