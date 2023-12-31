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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from pydantic import Field
from connectwise_psa.models.custom_field_value import CustomFieldValue
from connectwise_psa.models.iv_item_reference import IvItemReference
from connectwise_psa.models.shipment_method_reference import ShipmentMethodReference
from connectwise_psa.models.unit_of_measure_reference import UnitOfMeasureReference
from connectwise_psa.models.warehouse_bin_reference import WarehouseBinReference
from connectwise_psa.models.warehouse_reference import WarehouseReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PurchaseOrderLineItem(BaseModel):
    """
    PurchaseOrderLineItem
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    backordered_flag: Optional[StrictBool] = Field(default=None, alias="backorderedFlag")
    canceled_by: Optional[StrictStr] = Field(default=None, alias="canceledBy")
    canceled_flag: Optional[StrictBool] = Field(default=None, alias="canceledFlag")
    canceled_reason: Optional[StrictStr] = Field(default=None, description=" Max length: 100;", alias="canceledReason")
    closed_flag: Optional[StrictBool] = Field(default=None, alias="closedFlag")
    custom_fields: Optional[List[CustomFieldValue]] = Field(default=None, alias="customFields")
    date_canceled: Optional[datetime] = Field(default=None, alias="dateCanceled")
    date_canceled_utc: Optional[datetime] = Field(default=None, alias="dateCanceledUtc")
    date_received: Optional[datetime] = Field(default=None, alias="dateReceived")
    description: StrictStr = Field(description=" Max length: 6000;")
    display_internal_notes_flag: Optional[StrictBool] = Field(default=None, alias="displayInternalNotesFlag")
    expected_ship_date: Optional[datetime] = Field(default=None, alias="expectedShipDate")
    id: Optional[StrictInt] = None
    internal_notes: Optional[StrictStr] = Field(default=None, description=" Max length: 1000;", alias="internalNotes")
    line_number: Optional[StrictInt] = Field(alias="lineNumber")
    packing_slip: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="packingSlip")
    product: Optional[IvItemReference] = None
    purchase_order_id: Optional[StrictInt] = Field(default=None, alias="purchaseOrderId")
    quantity: Optional[Union[StrictFloat, StrictInt]]
    received_quantity: Optional[StrictInt] = Field(default=None, alias="receivedQuantity")
    received_status: Optional[StrictStr] = Field(default=None, alias="receivedStatus")
    serial_numbers: Optional[StrictStr] = Field(default=None, alias="serialNumbers")
    ship_date: Optional[datetime] = Field(default=None, alias="shipDate")
    ship_set: Optional[StrictStr] = Field(default=None, description=" Max length: 10;", alias="shipSet")
    shipment_method: Optional[ShipmentMethodReference] = Field(default=None, alias="shipmentMethod")
    tax: Optional[Union[StrictFloat, StrictInt]] = None
    tracking_number: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="trackingNumber")
    unit_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unitCost")
    unit_of_measure: Optional[UnitOfMeasureReference] = Field(default=None, alias="unitOfMeasure")
    vendor_order_number: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="vendorOrderNumber")
    vendor_sku: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="vendorSku")
    warehouse: Optional[WarehouseReference] = None
    warehouse_bin: Optional[WarehouseBinReference] = Field(default=None, alias="warehouseBin")
    __properties: ClassVar[List[str]] = ["_info", "backorderedFlag", "canceledBy", "canceledFlag", "canceledReason", "closedFlag", "customFields", "dateCanceled", "dateCanceledUtc", "dateReceived", "description", "displayInternalNotesFlag", "expectedShipDate", "id", "internalNotes", "lineNumber", "packingSlip", "product", "purchaseOrderId", "quantity", "receivedQuantity", "receivedStatus", "serialNumbers", "shipDate", "shipSet", "shipmentMethod", "tax", "trackingNumber", "unitCost", "unitOfMeasure", "vendorOrderNumber", "vendorSku", "warehouse", "warehouseBin"]

    @field_validator('received_status')
    def received_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Waiting', 'FullyReceived', 'PartiallyReceiveCancelRest', 'PartiallyReceiveCloneRest'):
            raise ValueError("must be one of enum values ('Waiting', 'FullyReceived', 'PartiallyReceiveCancelRest', 'PartiallyReceiveCloneRest')")
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
        """Create an instance of PurchaseOrderLineItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in custom_fields (list)
        _items = []
        if self.custom_fields:
            for _item in self.custom_fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customFields'] = _items
        # override the default output from pydantic by calling `to_dict()` of product
        if self.product:
            _dict['product'] = self.product.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipment_method
        if self.shipment_method:
            _dict['shipmentMethod'] = self.shipment_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unit_of_measure
        if self.unit_of_measure:
            _dict['unitOfMeasure'] = self.unit_of_measure.to_dict()
        # override the default output from pydantic by calling `to_dict()` of warehouse
        if self.warehouse:
            _dict['warehouse'] = self.warehouse.to_dict()
        # override the default output from pydantic by calling `to_dict()` of warehouse_bin
        if self.warehouse_bin:
            _dict['warehouseBin'] = self.warehouse_bin.to_dict()
        # set to None if backordered_flag (nullable) is None
        # and model_fields_set contains the field
        if self.backordered_flag is None and "backordered_flag" in self.model_fields_set:
            _dict['backorderedFlag'] = None

        # set to None if canceled_flag (nullable) is None
        # and model_fields_set contains the field
        if self.canceled_flag is None and "canceled_flag" in self.model_fields_set:
            _dict['canceledFlag'] = None

        # set to None if closed_flag (nullable) is None
        # and model_fields_set contains the field
        if self.closed_flag is None and "closed_flag" in self.model_fields_set:
            _dict['closedFlag'] = None

        # set to None if display_internal_notes_flag (nullable) is None
        # and model_fields_set contains the field
        if self.display_internal_notes_flag is None and "display_internal_notes_flag" in self.model_fields_set:
            _dict['displayInternalNotesFlag'] = None

        # set to None if line_number (nullable) is None
        # and model_fields_set contains the field
        if self.line_number is None and "line_number" in self.model_fields_set:
            _dict['lineNumber'] = None

        # set to None if purchase_order_id (nullable) is None
        # and model_fields_set contains the field
        if self.purchase_order_id is None and "purchase_order_id" in self.model_fields_set:
            _dict['purchaseOrderId'] = None

        # set to None if quantity (nullable) is None
        # and model_fields_set contains the field
        if self.quantity is None and "quantity" in self.model_fields_set:
            _dict['quantity'] = None

        # set to None if received_quantity (nullable) is None
        # and model_fields_set contains the field
        if self.received_quantity is None and "received_quantity" in self.model_fields_set:
            _dict['receivedQuantity'] = None

        # set to None if received_status (nullable) is None
        # and model_fields_set contains the field
        if self.received_status is None and "received_status" in self.model_fields_set:
            _dict['receivedStatus'] = None

        # set to None if tax (nullable) is None
        # and model_fields_set contains the field
        if self.tax is None and "tax" in self.model_fields_set:
            _dict['tax'] = None

        # set to None if unit_cost (nullable) is None
        # and model_fields_set contains the field
        if self.unit_cost is None and "unit_cost" in self.model_fields_set:
            _dict['unitCost'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PurchaseOrderLineItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in PurchaseOrderLineItem) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "backorderedFlag": obj.get("backorderedFlag"),
            "canceledBy": obj.get("canceledBy"),
            "canceledFlag": obj.get("canceledFlag"),
            "canceledReason": obj.get("canceledReason"),
            "closedFlag": obj.get("closedFlag"),
            "customFields": [CustomFieldValue.from_dict(_item) for _item in obj.get("customFields")] if obj.get("customFields") is not None else None,
            "dateCanceled": obj.get("dateCanceled"),
            "dateCanceledUtc": obj.get("dateCanceledUtc"),
            "dateReceived": obj.get("dateReceived"),
            "description": obj.get("description"),
            "displayInternalNotesFlag": obj.get("displayInternalNotesFlag"),
            "expectedShipDate": obj.get("expectedShipDate"),
            "id": obj.get("id"),
            "internalNotes": obj.get("internalNotes"),
            "lineNumber": obj.get("lineNumber"),
            "packingSlip": obj.get("packingSlip"),
            "product": IvItemReference.from_dict(obj.get("product")) if obj.get("product") is not None else None,
            "purchaseOrderId": obj.get("purchaseOrderId"),
            "quantity": obj.get("quantity"),
            "receivedQuantity": obj.get("receivedQuantity"),
            "receivedStatus": obj.get("receivedStatus"),
            "serialNumbers": obj.get("serialNumbers"),
            "shipDate": obj.get("shipDate"),
            "shipSet": obj.get("shipSet"),
            "shipmentMethod": ShipmentMethodReference.from_dict(obj.get("shipmentMethod")) if obj.get("shipmentMethod") is not None else None,
            "tax": obj.get("tax"),
            "trackingNumber": obj.get("trackingNumber"),
            "unitCost": obj.get("unitCost"),
            "unitOfMeasure": UnitOfMeasureReference.from_dict(obj.get("unitOfMeasure")) if obj.get("unitOfMeasure") is not None else None,
            "vendorOrderNumber": obj.get("vendorOrderNumber"),
            "vendorSku": obj.get("vendorSku"),
            "warehouse": WarehouseReference.from_dict(obj.get("warehouse")) if obj.get("warehouse") is not None else None,
            "warehouseBin": WarehouseBinReference.from_dict(obj.get("warehouseBin")) if obj.get("warehouseBin") is not None else None
        })
        return _obj


