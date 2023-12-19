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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from connectwise_psa.models.product_item_reference import ProductItemReference
from connectwise_psa.models.shipment_method_reference import ShipmentMethodReference
from connectwise_psa.models.warehouse_bin_reference import WarehouseBinReference
from connectwise_psa.models.warehouse_reference import WarehouseReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ProductPickingShippingDetail(BaseModel):
    """
    ProductPickingShippingDetail
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    id: Optional[StrictInt] = None
    line_number: Optional[StrictInt] = Field(default=None, alias="lineNumber")
    picked_quantity: Optional[StrictInt] = Field(default=None, alias="pickedQuantity")
    product_item: Optional[ProductItemReference] = Field(default=None, alias="productItem")
    quantity: Optional[StrictInt] = None
    serial_number: Optional[StrictStr] = Field(default=None, alias="serialNumber")
    serial_number_ids: Optional[List[StrictInt]] = Field(default=None, alias="serialNumberIds")
    shipment_method: Optional[ShipmentMethodReference] = Field(default=None, alias="shipmentMethod")
    shipped_quantity: Optional[StrictInt] = Field(default=None, alias="shippedQuantity")
    tracking_number: Optional[StrictStr] = Field(default=None, alias="trackingNumber")
    warehouse: Optional[WarehouseReference] = None
    warehouse_bin: Optional[WarehouseBinReference] = Field(default=None, alias="warehouseBin")
    __properties: ClassVar[List[str]] = ["_info", "id", "lineNumber", "pickedQuantity", "productItem", "quantity", "serialNumber", "serialNumberIds", "shipmentMethod", "shippedQuantity", "trackingNumber", "warehouse", "warehouseBin"]

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
        """Create an instance of ProductPickingShippingDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of product_item
        if self.product_item:
            _dict['productItem'] = self.product_item.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipment_method
        if self.shipment_method:
            _dict['shipmentMethod'] = self.shipment_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of warehouse
        if self.warehouse:
            _dict['warehouse'] = self.warehouse.to_dict()
        # override the default output from pydantic by calling `to_dict()` of warehouse_bin
        if self.warehouse_bin:
            _dict['warehouseBin'] = self.warehouse_bin.to_dict()
        # set to None if line_number (nullable) is None
        # and model_fields_set contains the field
        if self.line_number is None and "line_number" in self.model_fields_set:
            _dict['lineNumber'] = None

        # set to None if picked_quantity (nullable) is None
        # and model_fields_set contains the field
        if self.picked_quantity is None and "picked_quantity" in self.model_fields_set:
            _dict['pickedQuantity'] = None

        # set to None if quantity (nullable) is None
        # and model_fields_set contains the field
        if self.quantity is None and "quantity" in self.model_fields_set:
            _dict['quantity'] = None

        # set to None if shipped_quantity (nullable) is None
        # and model_fields_set contains the field
        if self.shipped_quantity is None and "shipped_quantity" in self.model_fields_set:
            _dict['shippedQuantity'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProductPickingShippingDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ProductPickingShippingDetail) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "id": obj.get("id"),
            "lineNumber": obj.get("lineNumber"),
            "pickedQuantity": obj.get("pickedQuantity"),
            "productItem": ProductItemReference.from_dict(obj.get("productItem")) if obj.get("productItem") is not None else None,
            "quantity": obj.get("quantity"),
            "serialNumber": obj.get("serialNumber"),
            "serialNumberIds": obj.get("serialNumberIds"),
            "shipmentMethod": ShipmentMethodReference.from_dict(obj.get("shipmentMethod")) if obj.get("shipmentMethod") is not None else None,
            "shippedQuantity": obj.get("shippedQuantity"),
            "trackingNumber": obj.get("trackingNumber"),
            "warehouse": WarehouseReference.from_dict(obj.get("warehouse")) if obj.get("warehouse") is not None else None,
            "warehouseBin": WarehouseBinReference.from_dict(obj.get("warehouseBin")) if obj.get("warehouseBin") is not None else None
        })
        return _obj

