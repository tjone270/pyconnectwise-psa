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
from connectwise_psa.models.gl_export_inventory_transfer_offset import GLExportInventoryTransferOffset
from connectwise_psa.models.iv_item_reference import IvItemReference
from connectwise_psa.models.product_sub_category_reference import ProductSubCategoryReference
from connectwise_psa.models.unit_of_measure_reference import UnitOfMeasureReference
from connectwise_psa.models.warehouse_bin_reference import WarehouseBinReference
from connectwise_psa.models.warehouse_reference import WarehouseReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GLExportInventoryTransfer(BaseModel):
    """
    GLExportInventoryTransfer
    """ # noqa: E501
    account_number: Optional[StrictStr] = Field(default=None, alias="accountNumber")
    bin: Optional[WarehouseBinReference] = None
    cogs_xref: Optional[StrictStr] = Field(default=None, alias="cogsXref")
    cost: Optional[Union[StrictFloat, StrictInt]] = None
    cost_account_number: Optional[StrictStr] = Field(default=None, alias="costAccountNumber")
    currency: Optional[CurrencyReference] = None
    description: Optional[StrictStr] = None
    document_date: Optional[StrictStr] = Field(default=None, alias="documentDate")
    document_type: Optional[StrictStr] = Field(default=None, alias="documentType")
    gl_class: Optional[StrictStr] = Field(default=None, alias="glClass")
    gl_item_id: Optional[StrictStr] = Field(default=None, alias="glItemId")
    gl_type_id: Optional[StrictStr] = Field(default=None, alias="glTypeId")
    id: Optional[StrictStr] = None
    inventory_account_number: Optional[StrictStr] = Field(default=None, alias="inventoryAccountNumber")
    inventory_xref: Optional[StrictStr] = Field(default=None, alias="inventoryXref")
    item: Optional[IvItemReference] = None
    item_description: Optional[StrictStr] = Field(default=None, alias="itemDescription")
    item_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="itemPrice")
    item_type_xref: Optional[StrictStr] = Field(default=None, alias="itemTypeXref")
    location_xref: Optional[StrictStr] = Field(default=None, alias="locationXref")
    memo: Optional[StrictStr] = None
    offset: Optional[GLExportInventoryTransferOffset] = None
    price_level_xref: Optional[StrictStr] = Field(default=None, alias="priceLevelXref")
    quantity: Optional[Union[StrictFloat, StrictInt]] = None
    sales_code: Optional[StrictStr] = Field(default=None, alias="salesCode")
    sales_description: Optional[StrictStr] = Field(default=None, alias="salesDescription")
    serial_numbers: Optional[StrictStr] = Field(default=None, alias="serialNumbers")
    serialized_flag: Optional[StrictBool] = Field(default=None, alias="serializedFlag")
    sub_category: Optional[ProductSubCategoryReference] = Field(default=None, alias="subCategory")
    tax_note: Optional[StrictStr] = Field(default=None, alias="taxNote")
    taxable: Optional[StrictBool] = None
    total: Optional[Union[StrictFloat, StrictInt]] = None
    transfer_from_bin: Optional[WarehouseBinReference] = Field(default=None, alias="transferFromBin")
    transfer_from_location_xref: Optional[StrictStr] = Field(default=None, alias="transferFromLocationXref")
    transfer_id: Optional[StrictInt] = Field(default=None, alias="transferId")
    transfer_to_bin: Optional[WarehouseBinReference] = Field(default=None, alias="transferToBin")
    transfer_to_location_xref: Optional[StrictStr] = Field(default=None, alias="transferToLocationXref")
    unit_of_measure: Optional[UnitOfMeasureReference] = Field(default=None, alias="unitOfMeasure")
    uom_schedule_xref: Optional[StrictStr] = Field(default=None, alias="uomScheduleXref")
    warehouse: Optional[WarehouseReference] = None
    __properties: ClassVar[List[str]] = ["accountNumber", "bin", "cogsXref", "cost", "costAccountNumber", "currency", "description", "documentDate", "documentType", "glClass", "glItemId", "glTypeId", "id", "inventoryAccountNumber", "inventoryXref", "item", "itemDescription", "itemPrice", "itemTypeXref", "locationXref", "memo", "offset", "priceLevelXref", "quantity", "salesCode", "salesDescription", "serialNumbers", "serializedFlag", "subCategory", "taxNote", "taxable", "total", "transferFromBin", "transferFromLocationXref", "transferId", "transferToBin", "transferToLocationXref", "unitOfMeasure", "uomScheduleXref", "warehouse"]

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
        """Create an instance of GLExportInventoryTransfer from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bin
        if self.bin:
            _dict['bin'] = self.bin.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency
        if self.currency:
            _dict['currency'] = self.currency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of item
        if self.item:
            _dict['item'] = self.item.to_dict()
        # override the default output from pydantic by calling `to_dict()` of offset
        if self.offset:
            _dict['offset'] = self.offset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sub_category
        if self.sub_category:
            _dict['subCategory'] = self.sub_category.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transfer_from_bin
        if self.transfer_from_bin:
            _dict['transferFromBin'] = self.transfer_from_bin.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transfer_to_bin
        if self.transfer_to_bin:
            _dict['transferToBin'] = self.transfer_to_bin.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unit_of_measure
        if self.unit_of_measure:
            _dict['unitOfMeasure'] = self.unit_of_measure.to_dict()
        # override the default output from pydantic by calling `to_dict()` of warehouse
        if self.warehouse:
            _dict['warehouse'] = self.warehouse.to_dict()
        # set to None if cost (nullable) is None
        # and model_fields_set contains the field
        if self.cost is None and "cost" in self.model_fields_set:
            _dict['cost'] = None

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

        # set to None if taxable (nullable) is None
        # and model_fields_set contains the field
        if self.taxable is None and "taxable" in self.model_fields_set:
            _dict['taxable'] = None

        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        # set to None if transfer_id (nullable) is None
        # and model_fields_set contains the field
        if self.transfer_id is None and "transfer_id" in self.model_fields_set:
            _dict['transferId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GLExportInventoryTransfer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in GLExportInventoryTransfer) in the input: " + _key)

        _obj = cls.model_validate({
            "accountNumber": obj.get("accountNumber"),
            "bin": WarehouseBinReference.from_dict(obj.get("bin")) if obj.get("bin") is not None else None,
            "cogsXref": obj.get("cogsXref"),
            "cost": obj.get("cost"),
            "costAccountNumber": obj.get("costAccountNumber"),
            "currency": CurrencyReference.from_dict(obj.get("currency")) if obj.get("currency") is not None else None,
            "description": obj.get("description"),
            "documentDate": obj.get("documentDate"),
            "documentType": obj.get("documentType"),
            "glClass": obj.get("glClass"),
            "glItemId": obj.get("glItemId"),
            "glTypeId": obj.get("glTypeId"),
            "id": obj.get("id"),
            "inventoryAccountNumber": obj.get("inventoryAccountNumber"),
            "inventoryXref": obj.get("inventoryXref"),
            "item": IvItemReference.from_dict(obj.get("item")) if obj.get("item") is not None else None,
            "itemDescription": obj.get("itemDescription"),
            "itemPrice": obj.get("itemPrice"),
            "itemTypeXref": obj.get("itemTypeXref"),
            "locationXref": obj.get("locationXref"),
            "memo": obj.get("memo"),
            "offset": GLExportInventoryTransferOffset.from_dict(obj.get("offset")) if obj.get("offset") is not None else None,
            "priceLevelXref": obj.get("priceLevelXref"),
            "quantity": obj.get("quantity"),
            "salesCode": obj.get("salesCode"),
            "salesDescription": obj.get("salesDescription"),
            "serialNumbers": obj.get("serialNumbers"),
            "serializedFlag": obj.get("serializedFlag"),
            "subCategory": ProductSubCategoryReference.from_dict(obj.get("subCategory")) if obj.get("subCategory") is not None else None,
            "taxNote": obj.get("taxNote"),
            "taxable": obj.get("taxable"),
            "total": obj.get("total"),
            "transferFromBin": WarehouseBinReference.from_dict(obj.get("transferFromBin")) if obj.get("transferFromBin") is not None else None,
            "transferFromLocationXref": obj.get("transferFromLocationXref"),
            "transferId": obj.get("transferId"),
            "transferToBin": WarehouseBinReference.from_dict(obj.get("transferToBin")) if obj.get("transferToBin") is not None else None,
            "transferToLocationXref": obj.get("transferToLocationXref"),
            "unitOfMeasure": UnitOfMeasureReference.from_dict(obj.get("unitOfMeasure")) if obj.get("unitOfMeasure") is not None else None,
            "uomScheduleXref": obj.get("uomScheduleXref"),
            "warehouse": WarehouseReference.from_dict(obj.get("warehouse")) if obj.get("warehouse") is not None else None
        })
        return _obj


