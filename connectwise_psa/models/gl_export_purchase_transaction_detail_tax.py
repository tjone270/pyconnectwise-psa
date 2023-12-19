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
from connectwise_psa.models.currency_reference import CurrencyReference
from connectwise_psa.models.iv_item_reference import IvItemReference
from connectwise_psa.models.product_sub_category_reference import ProductSubCategoryReference
from connectwise_psa.models.shipment_method_reference import ShipmentMethodReference
from connectwise_psa.models.site_reference import SiteReference
from connectwise_psa.models.tax_code_reference import TaxCodeReference
from connectwise_psa.models.unit_of_measure_reference import UnitOfMeasureReference
from connectwise_psa.models.warehouse_bin_reference import WarehouseBinReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GLExportPurchaseTransactionDetailTax(BaseModel):
    """
    GLExportPurchaseTransactionDetailTax
    """ # noqa: E501
    account_number: Optional[StrictStr] = Field(default=None, alias="accountNumber")
    cogs_xref: Optional[StrictStr] = Field(default=None, alias="cogsXref")
    cost: Optional[Union[StrictFloat, StrictInt]] = None
    cost_account_number: Optional[StrictStr] = Field(default=None, alias="costAccountNumber")
    currency: Optional[CurrencyReference] = None
    document_date: Optional[StrictStr] = Field(default=None, alias="documentDate")
    drop_shipped_flag: Optional[StrictBool] = Field(default=None, alias="dropShippedFlag")
    gl_class: Optional[StrictStr] = Field(default=None, alias="glClass")
    gl_item_id: Optional[StrictStr] = Field(default=None, alias="glItemId")
    gl_type_id: Optional[StrictStr] = Field(default=None, alias="glTypeId")
    id: Optional[StrictInt] = None
    inventory_account_number: Optional[StrictStr] = Field(default=None, alias="inventoryAccountNumber")
    inventory_xref: Optional[StrictStr] = Field(default=None, alias="inventoryXref")
    item: Optional[IvItemReference] = None
    item_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="itemCost")
    item_description: Optional[StrictStr] = Field(default=None, alias="itemDescription")
    item_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="itemPrice")
    item_type_xref: Optional[StrictStr] = Field(default=None, alias="itemTypeXref")
    line_number: Optional[StrictInt] = Field(default=None, alias="lineNumber")
    location_xref: Optional[StrictStr] = Field(default=None, alias="locationXref")
    memo: Optional[StrictStr] = None
    price_level_xref: Optional[StrictStr] = Field(default=None, alias="priceLevelXref")
    purchase_header_tax_group: Optional[StrictStr] = Field(default=None, alias="purchaseHeaderTaxGroup")
    quantity: Optional[Union[StrictFloat, StrictInt]] = None
    sales_code: Optional[StrictStr] = Field(default=None, alias="salesCode")
    sales_description: Optional[StrictStr] = Field(default=None, alias="salesDescription")
    serial_numbers: Optional[StrictStr] = Field(default=None, alias="serialNumbers")
    serialized_flag: Optional[StrictBool] = Field(default=None, alias="serializedFlag")
    shipment_method: Optional[ShipmentMethodReference] = Field(default=None, alias="shipmentMethod")
    sub_category: Optional[ProductSubCategoryReference] = Field(default=None, alias="subCategory")
    tax_agency_xref: Optional[StrictStr] = Field(default=None, alias="taxAgencyXref")
    tax_code: Optional[TaxCodeReference] = Field(default=None, alias="taxCode")
    tax_note: Optional[StrictStr] = Field(default=None, alias="taxNote")
    tax_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="taxRate")
    tax_rate_percent: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="taxRatePercent")
    taxable_flag: Optional[StrictBool] = Field(default=None, alias="taxableFlag")
    total: Optional[Union[StrictFloat, StrictInt]] = None
    unit_of_measure: Optional[UnitOfMeasureReference] = Field(default=None, alias="unitOfMeasure")
    uom_schedule_xref: Optional[StrictStr] = Field(default=None, alias="uomScheduleXref")
    vendor_account_number: Optional[StrictStr] = Field(default=None, alias="vendorAccountNumber")
    vendor_number: Optional[StrictStr] = Field(default=None, alias="vendorNumber")
    warehouse_bin: Optional[WarehouseBinReference] = Field(default=None, alias="warehouseBin")
    warehouse_site: Optional[SiteReference] = Field(default=None, alias="warehouseSite")
    __properties: ClassVar[List[str]] = ["accountNumber", "cogsXref", "cost", "costAccountNumber", "currency", "documentDate", "dropShippedFlag", "glClass", "glItemId", "glTypeId", "id", "inventoryAccountNumber", "inventoryXref", "item", "itemCost", "itemDescription", "itemPrice", "itemTypeXref", "lineNumber", "locationXref", "memo", "priceLevelXref", "purchaseHeaderTaxGroup", "quantity", "salesCode", "salesDescription", "serialNumbers", "serializedFlag", "shipmentMethod", "subCategory", "taxAgencyXref", "taxCode", "taxNote", "taxRate", "taxRatePercent", "taxableFlag", "total", "unitOfMeasure", "uomScheduleXref", "vendorAccountNumber", "vendorNumber", "warehouseBin", "warehouseSite"]

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
        """Create an instance of GLExportPurchaseTransactionDetailTax from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of item
        if self.item:
            _dict['item'] = self.item.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipment_method
        if self.shipment_method:
            _dict['shipmentMethod'] = self.shipment_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sub_category
        if self.sub_category:
            _dict['subCategory'] = self.sub_category.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tax_code
        if self.tax_code:
            _dict['taxCode'] = self.tax_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unit_of_measure
        if self.unit_of_measure:
            _dict['unitOfMeasure'] = self.unit_of_measure.to_dict()
        # override the default output from pydantic by calling `to_dict()` of warehouse_bin
        if self.warehouse_bin:
            _dict['warehouseBin'] = self.warehouse_bin.to_dict()
        # override the default output from pydantic by calling `to_dict()` of warehouse_site
        if self.warehouse_site:
            _dict['warehouseSite'] = self.warehouse_site.to_dict()
        # set to None if cost (nullable) is None
        # and model_fields_set contains the field
        if self.cost is None and "cost" in self.model_fields_set:
            _dict['cost'] = None

        # set to None if drop_shipped_flag (nullable) is None
        # and model_fields_set contains the field
        if self.drop_shipped_flag is None and "drop_shipped_flag" in self.model_fields_set:
            _dict['dropShippedFlag'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if item_cost (nullable) is None
        # and model_fields_set contains the field
        if self.item_cost is None and "item_cost" in self.model_fields_set:
            _dict['itemCost'] = None

        # set to None if item_price (nullable) is None
        # and model_fields_set contains the field
        if self.item_price is None and "item_price" in self.model_fields_set:
            _dict['itemPrice'] = None

        # set to None if quantity (nullable) is None
        # and model_fields_set contains the field
        if self.quantity is None and "quantity" in self.model_fields_set:
            _dict['quantity'] = None

        # set to None if serialized_flag (nullable) is None
        # and model_fields_set contains the field
        if self.serialized_flag is None and "serialized_flag" in self.model_fields_set:
            _dict['serializedFlag'] = None

        # set to None if tax_rate (nullable) is None
        # and model_fields_set contains the field
        if self.tax_rate is None and "tax_rate" in self.model_fields_set:
            _dict['taxRate'] = None

        # set to None if tax_rate_percent (nullable) is None
        # and model_fields_set contains the field
        if self.tax_rate_percent is None and "tax_rate_percent" in self.model_fields_set:
            _dict['taxRatePercent'] = None

        # set to None if taxable_flag (nullable) is None
        # and model_fields_set contains the field
        if self.taxable_flag is None and "taxable_flag" in self.model_fields_set:
            _dict['taxableFlag'] = None

        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GLExportPurchaseTransactionDetailTax from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in GLExportPurchaseTransactionDetailTax) in the input: " + _key)

        _obj = cls.model_validate({
            "accountNumber": obj.get("accountNumber"),
            "cogsXref": obj.get("cogsXref"),
            "cost": obj.get("cost"),
            "costAccountNumber": obj.get("costAccountNumber"),
            "currency": CurrencyReference.from_dict(obj.get("currency")) if obj.get("currency") is not None else None,
            "documentDate": obj.get("documentDate"),
            "dropShippedFlag": obj.get("dropShippedFlag"),
            "glClass": obj.get("glClass"),
            "glItemId": obj.get("glItemId"),
            "glTypeId": obj.get("glTypeId"),
            "id": obj.get("id"),
            "inventoryAccountNumber": obj.get("inventoryAccountNumber"),
            "inventoryXref": obj.get("inventoryXref"),
            "item": IvItemReference.from_dict(obj.get("item")) if obj.get("item") is not None else None,
            "itemCost": obj.get("itemCost"),
            "itemDescription": obj.get("itemDescription"),
            "itemPrice": obj.get("itemPrice"),
            "itemTypeXref": obj.get("itemTypeXref"),
            "lineNumber": obj.get("lineNumber"),
            "locationXref": obj.get("locationXref"),
            "memo": obj.get("memo"),
            "priceLevelXref": obj.get("priceLevelXref"),
            "purchaseHeaderTaxGroup": obj.get("purchaseHeaderTaxGroup"),
            "quantity": obj.get("quantity"),
            "salesCode": obj.get("salesCode"),
            "salesDescription": obj.get("salesDescription"),
            "serialNumbers": obj.get("serialNumbers"),
            "serializedFlag": obj.get("serializedFlag"),
            "shipmentMethod": ShipmentMethodReference.from_dict(obj.get("shipmentMethod")) if obj.get("shipmentMethod") is not None else None,
            "subCategory": ProductSubCategoryReference.from_dict(obj.get("subCategory")) if obj.get("subCategory") is not None else None,
            "taxAgencyXref": obj.get("taxAgencyXref"),
            "taxCode": TaxCodeReference.from_dict(obj.get("taxCode")) if obj.get("taxCode") is not None else None,
            "taxNote": obj.get("taxNote"),
            "taxRate": obj.get("taxRate"),
            "taxRatePercent": obj.get("taxRatePercent"),
            "taxableFlag": obj.get("taxableFlag"),
            "total": obj.get("total"),
            "unitOfMeasure": UnitOfMeasureReference.from_dict(obj.get("unitOfMeasure")) if obj.get("unitOfMeasure") is not None else None,
            "uomScheduleXref": obj.get("uomScheduleXref"),
            "vendorAccountNumber": obj.get("vendorAccountNumber"),
            "vendorNumber": obj.get("vendorNumber"),
            "warehouseBin": WarehouseBinReference.from_dict(obj.get("warehouseBin")) if obj.get("warehouseBin") is not None else None,
            "warehouseSite": SiteReference.from_dict(obj.get("warehouseSite")) if obj.get("warehouseSite") is not None else None
        })
        return _obj


