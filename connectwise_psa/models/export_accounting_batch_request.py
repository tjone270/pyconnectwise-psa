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
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ExportAccountingBatchRequest(BaseModel):
    """
    ExportAccountingBatchRequest
    """ # noqa: E501
    batch_identifier: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="batchIdentifier")
    excluded_expense_ids: Optional[List[StrictInt]] = Field(default=None, alias="excludedExpenseIds")
    excluded_invoice_ids: Optional[List[StrictInt]] = Field(default=None, alias="excludedInvoiceIds")
    excluded_product_ids: Optional[List[StrictStr]] = Field(default=None, alias="excludedProductIds")
    export_expenses_flag: Optional[StrictBool] = Field(default=None, description="Batch export must include invoices, expenses, or products (procurement).", alias="exportExpensesFlag")
    export_invoices_flag: Optional[StrictBool] = Field(default=None, description="Batch export must include invoices, expenses, or products (procurement).", alias="exportInvoicesFlag")
    export_payments_flag: Optional[StrictBool] = Field(default=None, description="Batch export must include invoices, expenses, or products (procurement).", alias="exportPaymentsFlag")
    export_products_flag: Optional[StrictBool] = Field(default=None, description="Batch export must include invoices, expenses, or products (procurement).", alias="exportProductsFlag")
    gl_interface_identifier: Optional[StrictStr] = Field(default=None, alias="glInterfaceIdentifier")
    included_expense_ids: Optional[List[StrictInt]] = Field(default=None, alias="includedExpenseIds")
    included_invoice_ids: Optional[List[StrictInt]] = Field(default=None, alias="includedInvoiceIds")
    included_payment_ids: Optional[List[StrictInt]] = Field(default=None, alias="includedPaymentIds")
    included_product_ids: Optional[List[StrictStr]] = Field(default=None, alias="includedProductIds")
    location_id: Optional[StrictInt] = Field(default=None, alias="locationId")
    summarize_invoices: Optional[StrictStr] = Field(default=None, alias="summarizeInvoices")
    thru_date: Optional[datetime] = Field(default=None, alias="thruDate")
    __properties: ClassVar[List[str]] = ["batchIdentifier", "excludedExpenseIds", "excludedInvoiceIds", "excludedProductIds", "exportExpensesFlag", "exportInvoicesFlag", "exportPaymentsFlag", "exportProductsFlag", "glInterfaceIdentifier", "includedExpenseIds", "includedInvoiceIds", "includedPaymentIds", "includedProductIds", "locationId", "summarizeInvoices", "thruDate"]

    @field_validator('summarize_invoices')
    def summarize_invoices_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Default', 'Condensed', 'Detailed'):
            raise ValueError("must be one of enum values ('Default', 'Condensed', 'Detailed')")
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
        """Create an instance of ExportAccountingBatchRequest from a JSON string"""
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
        # set to None if export_expenses_flag (nullable) is None
        # and model_fields_set contains the field
        if self.export_expenses_flag is None and "export_expenses_flag" in self.model_fields_set:
            _dict['exportExpensesFlag'] = None

        # set to None if export_invoices_flag (nullable) is None
        # and model_fields_set contains the field
        if self.export_invoices_flag is None and "export_invoices_flag" in self.model_fields_set:
            _dict['exportInvoicesFlag'] = None

        # set to None if export_payments_flag (nullable) is None
        # and model_fields_set contains the field
        if self.export_payments_flag is None and "export_payments_flag" in self.model_fields_set:
            _dict['exportPaymentsFlag'] = None

        # set to None if export_products_flag (nullable) is None
        # and model_fields_set contains the field
        if self.export_products_flag is None and "export_products_flag" in self.model_fields_set:
            _dict['exportProductsFlag'] = None

        # set to None if location_id (nullable) is None
        # and model_fields_set contains the field
        if self.location_id is None and "location_id" in self.model_fields_set:
            _dict['locationId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ExportAccountingBatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ExportAccountingBatchRequest) in the input: " + _key)

        _obj = cls.model_validate({
            "batchIdentifier": obj.get("batchIdentifier"),
            "excludedExpenseIds": obj.get("excludedExpenseIds"),
            "excludedInvoiceIds": obj.get("excludedInvoiceIds"),
            "excludedProductIds": obj.get("excludedProductIds"),
            "exportExpensesFlag": obj.get("exportExpensesFlag"),
            "exportInvoicesFlag": obj.get("exportInvoicesFlag"),
            "exportPaymentsFlag": obj.get("exportPaymentsFlag"),
            "exportProductsFlag": obj.get("exportProductsFlag"),
            "glInterfaceIdentifier": obj.get("glInterfaceIdentifier"),
            "includedExpenseIds": obj.get("includedExpenseIds"),
            "includedInvoiceIds": obj.get("includedInvoiceIds"),
            "includedPaymentIds": obj.get("includedPaymentIds"),
            "includedProductIds": obj.get("includedProductIds"),
            "locationId": obj.get("locationId"),
            "summarizeInvoices": obj.get("summarizeInvoices"),
            "thruDate": obj.get("thruDate")
        })
        return _obj


