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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from connectwise_psa.models.expense_entry_tax_view_model import ExpenseEntryTaxViewModel
from connectwise_psa.models.expense_entry_widget_view_model import ExpenseEntryWidgetViewModel
from connectwise_psa.models.mileage_calculator_view_model import MileageCalculatorViewModel
from connectwise_psa.models.user_defined_field_value import UserDefinedFieldValue
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ExpenseEntryPodViewModel(BaseModel):
    """
    ExpenseEntryPodViewModel
    """ # noqa: E501
    expense_entry_pod_user_defined_field_values: Optional[List[UserDefinedFieldValue]] = Field(default=None, alias="expenseEntryPodUserDefinedFieldValues")
    expense_entry_widget: Optional[ExpenseEntryWidgetViewModel] = Field(default=None, alias="expenseEntryWidget")
    expense_taxes: Optional[List[ExpenseEntryTaxViewModel]] = Field(default=None, alias="expenseTaxes")
    mileage_calculator_vm: Optional[MileageCalculatorViewModel] = Field(default=None, alias="mileageCalculatorVM")
    notes: Optional[StrictStr] = None
    show_expense_tax: Optional[StrictBool] = Field(default=None, alias="showExpenseTax")
    __properties: ClassVar[List[str]] = ["expenseEntryPodUserDefinedFieldValues", "expenseEntryWidget", "expenseTaxes", "mileageCalculatorVM", "notes", "showExpenseTax"]

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
        """Create an instance of ExpenseEntryPodViewModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in expense_entry_pod_user_defined_field_values (list)
        _items = []
        if self.expense_entry_pod_user_defined_field_values:
            for _item in self.expense_entry_pod_user_defined_field_values:
                if _item:
                    _items.append(_item.to_dict())
            _dict['expenseEntryPodUserDefinedFieldValues'] = _items
        # override the default output from pydantic by calling `to_dict()` of expense_entry_widget
        if self.expense_entry_widget:
            _dict['expenseEntryWidget'] = self.expense_entry_widget.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in expense_taxes (list)
        _items = []
        if self.expense_taxes:
            for _item in self.expense_taxes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['expenseTaxes'] = _items
        # override the default output from pydantic by calling `to_dict()` of mileage_calculator_vm
        if self.mileage_calculator_vm:
            _dict['mileageCalculatorVM'] = self.mileage_calculator_vm.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ExpenseEntryPodViewModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ExpenseEntryPodViewModel) in the input: " + _key)

        _obj = cls.model_validate({
            "expenseEntryPodUserDefinedFieldValues": [UserDefinedFieldValue.from_dict(_item) for _item in obj.get("expenseEntryPodUserDefinedFieldValues")] if obj.get("expenseEntryPodUserDefinedFieldValues") is not None else None,
            "expenseEntryWidget": ExpenseEntryWidgetViewModel.from_dict(obj.get("expenseEntryWidget")) if obj.get("expenseEntryWidget") is not None else None,
            "expenseTaxes": [ExpenseEntryTaxViewModel.from_dict(_item) for _item in obj.get("expenseTaxes")] if obj.get("expenseTaxes") is not None else None,
            "mileageCalculatorVM": MileageCalculatorViewModel.from_dict(obj.get("mileageCalculatorVM")) if obj.get("mileageCalculatorVM") is not None else None,
            "notes": obj.get("notes"),
            "showExpenseTax": obj.get("showExpenseTax")
        })
        return _obj


