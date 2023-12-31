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
from pydantic import BaseModel
from pydantic import Field
from connectwise_psa.models.gl_export_adjustment_transaction import GLExportAdjustmentTransaction
from connectwise_psa.models.gl_export_customer import GLExportCustomer
from connectwise_psa.models.gl_export_expense import GLExportExpense
from connectwise_psa.models.gl_export_expense_bill import GLExportExpenseBill
from connectwise_psa.models.gl_export_inventory_transfer import GLExportInventoryTransfer
from connectwise_psa.models.gl_export_purchase_transaction import GLExportPurchaseTransaction
from connectwise_psa.models.gl_export_transaction import GLExportTransaction
from connectwise_psa.models.gl_export_vendor import GLExportVendor
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GLExport(BaseModel):
    """
    GLExport
    """ # noqa: E501
    adjustment_transactions: Optional[List[GLExportAdjustmentTransaction]] = Field(default=None, alias="adjustmentTransactions")
    customers: Optional[List[GLExportCustomer]] = None
    expense_bills: Optional[List[GLExportExpenseBill]] = Field(default=None, alias="expenseBills")
    expenses: Optional[List[GLExportExpense]] = None
    export_settings: Optional[Union[str, Any]] = Field(default=None, alias="exportSettings")
    inventory_transfers: Optional[List[GLExportInventoryTransfer]] = Field(default=None, alias="inventoryTransfers")
    purchase_transactions: Optional[List[GLExportPurchaseTransaction]] = Field(default=None, alias="purchaseTransactions")
    transactions: Optional[List[GLExportTransaction]] = None
    vendors: Optional[List[GLExportVendor]] = None
    __properties: ClassVar[List[str]] = ["adjustmentTransactions", "customers", "expenseBills", "expenses", "exportSettings", "inventoryTransfers", "purchaseTransactions", "transactions", "vendors"]

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
        """Create an instance of GLExport from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in adjustment_transactions (list)
        _items = []
        if self.adjustment_transactions:
            for _item in self.adjustment_transactions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['adjustmentTransactions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in customers (list)
        _items = []
        if self.customers:
            for _item in self.customers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in expense_bills (list)
        _items = []
        if self.expense_bills:
            for _item in self.expense_bills:
                if _item:
                    _items.append(_item.to_dict())
            _dict['expenseBills'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in expenses (list)
        _items = []
        if self.expenses:
            for _item in self.expenses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['expenses'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in inventory_transfers (list)
        _items = []
        if self.inventory_transfers:
            for _item in self.inventory_transfers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['inventoryTransfers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in purchase_transactions (list)
        _items = []
        if self.purchase_transactions:
            for _item in self.purchase_transactions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['purchaseTransactions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in transactions (list)
        _items = []
        if self.transactions:
            for _item in self.transactions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['transactions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in vendors (list)
        _items = []
        if self.vendors:
            for _item in self.vendors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vendors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GLExport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in GLExport) in the input: " + _key)

        _obj = cls.model_validate({
            "adjustmentTransactions": [GLExportAdjustmentTransaction.from_dict(_item) for _item in obj.get("adjustmentTransactions")] if obj.get("adjustmentTransactions") is not None else None,
            "customers": [GLExportCustomer.from_dict(_item) for _item in obj.get("customers")] if obj.get("customers") is not None else None,
            "expenseBills": [GLExportExpenseBill.from_dict(_item) for _item in obj.get("expenseBills")] if obj.get("expenseBills") is not None else None,
            "expenses": [GLExportExpense.from_dict(_item) for _item in obj.get("expenses")] if obj.get("expenses") is not None else None,
            "exportSettings": obj.get("exportSettings"),
            "inventoryTransfers": [GLExportInventoryTransfer.from_dict(_item) for _item in obj.get("inventoryTransfers")] if obj.get("inventoryTransfers") is not None else None,
            "purchaseTransactions": [GLExportPurchaseTransaction.from_dict(_item) for _item in obj.get("purchaseTransactions")] if obj.get("purchaseTransactions") is not None else None,
            "transactions": [GLExportTransaction.from_dict(_item) for _item in obj.get("transactions")] if obj.get("transactions") is not None else None,
            "vendors": [GLExportVendor.from_dict(_item) for _item in obj.get("vendors")] if obj.get("vendors") is not None else None
        })
        return _obj


