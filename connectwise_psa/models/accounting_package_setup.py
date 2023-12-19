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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, field_validator
from pydantic import Field
from connectwise_psa.models.accounting_package_reference import AccountingPackageReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AccountingPackageSetup(BaseModel):
    """
    AccountingPackageSetup
    """ # noqa: E501
    accounting_package: Optional[AccountingPackageReference] = Field(default=None, alias="accountingPackage")
    direct_transfer_flag: Optional[StrictBool] = Field(default=None, alias="directTransferFlag")
    enable_tax_groups_flag: Optional[StrictBool] = Field(default=None, alias="enableTaxGroupsFlag")
    expense_format: Optional[StrictStr] = Field(default=None, alias="expenseFormat")
    id: Optional[StrictInt] = None
    include_cogs_drop_ship_flag: Optional[StrictBool] = Field(default=None, alias="includeCogsDropShipFlag")
    include_cogs_entries_flag: Optional[StrictBool] = Field(default=None, alias="includeCogsEntriesFlag")
    include_expenses_flag: Optional[StrictBool] = Field(default=None, alias="includeExpensesFlag")
    include_invoices_flag: Optional[StrictBool] = Field(default=None, alias="includeInvoicesFlag")
    include_items_flag: Optional[StrictBool] = Field(default=None, alias="includeItemsFlag")
    include_sales_tax_flag: Optional[StrictBool] = Field(default=None, alias="includeSalesTaxFlag")
    inventory_soh_flag: Optional[StrictBool] = Field(default=None, alias="inventorySOHFlag")
    invoice_format: Optional[StrictStr] = Field(default=None, alias="invoiceFormat")
    send_component_amount_flag: Optional[StrictBool] = Field(default=None, alias="sendComponentAmountFlag")
    send_uom_flag: Optional[StrictBool] = Field(default=None, alias="sendUomFlag")
    suppress_memo_flag: Optional[StrictBool] = Field(default=None, alias="suppressMemoFlag")
    sync_payment_info_flag: Optional[StrictBool] = Field(default=None, alias="syncPaymentInfoFlag")
    sync_wise_pay_payment_info_flag: Optional[StrictBool] = Field(default=None, alias="syncWisePayPaymentInfoFlag")
    transfer_expenses_as_bill_flag: Optional[StrictBool] = Field(default=None, alias="transferExpensesAsBillFlag")
    wise_pay_lab_flag: Optional[StrictBool] = Field(default=None, alias="wisePayLabFlag")
    zero_dollar_tax_amounts_flag: Optional[StrictBool] = Field(default=None, alias="zeroDollarTaxAmountsFlag")
    __properties: ClassVar[List[str]] = ["accountingPackage", "directTransferFlag", "enableTaxGroupsFlag", "expenseFormat", "id", "includeCogsDropShipFlag", "includeCogsEntriesFlag", "includeExpensesFlag", "includeInvoicesFlag", "includeItemsFlag", "includeSalesTaxFlag", "inventorySOHFlag", "invoiceFormat", "sendComponentAmountFlag", "sendUomFlag", "suppressMemoFlag", "syncPaymentInfoFlag", "syncWisePayPaymentInfoFlag", "transferExpensesAsBillFlag", "wisePayLabFlag", "zeroDollarTaxAmountsFlag"]

    @field_validator('expense_format')
    def expense_format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Default', 'Condensed'):
            raise ValueError("must be one of enum values ('Default', 'Condensed')")
        return value

    @field_validator('invoice_format')
    def invoice_format_validate_enum(cls, value):
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
        """Create an instance of AccountingPackageSetup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of accounting_package
        if self.accounting_package:
            _dict['accountingPackage'] = self.accounting_package.to_dict()
        # set to None if direct_transfer_flag (nullable) is None
        # and model_fields_set contains the field
        if self.direct_transfer_flag is None and "direct_transfer_flag" in self.model_fields_set:
            _dict['directTransferFlag'] = None

        # set to None if enable_tax_groups_flag (nullable) is None
        # and model_fields_set contains the field
        if self.enable_tax_groups_flag is None and "enable_tax_groups_flag" in self.model_fields_set:
            _dict['enableTaxGroupsFlag'] = None

        # set to None if expense_format (nullable) is None
        # and model_fields_set contains the field
        if self.expense_format is None and "expense_format" in self.model_fields_set:
            _dict['expenseFormat'] = None

        # set to None if include_cogs_drop_ship_flag (nullable) is None
        # and model_fields_set contains the field
        if self.include_cogs_drop_ship_flag is None and "include_cogs_drop_ship_flag" in self.model_fields_set:
            _dict['includeCogsDropShipFlag'] = None

        # set to None if include_cogs_entries_flag (nullable) is None
        # and model_fields_set contains the field
        if self.include_cogs_entries_flag is None and "include_cogs_entries_flag" in self.model_fields_set:
            _dict['includeCogsEntriesFlag'] = None

        # set to None if include_expenses_flag (nullable) is None
        # and model_fields_set contains the field
        if self.include_expenses_flag is None and "include_expenses_flag" in self.model_fields_set:
            _dict['includeExpensesFlag'] = None

        # set to None if include_invoices_flag (nullable) is None
        # and model_fields_set contains the field
        if self.include_invoices_flag is None and "include_invoices_flag" in self.model_fields_set:
            _dict['includeInvoicesFlag'] = None

        # set to None if include_items_flag (nullable) is None
        # and model_fields_set contains the field
        if self.include_items_flag is None and "include_items_flag" in self.model_fields_set:
            _dict['includeItemsFlag'] = None

        # set to None if include_sales_tax_flag (nullable) is None
        # and model_fields_set contains the field
        if self.include_sales_tax_flag is None and "include_sales_tax_flag" in self.model_fields_set:
            _dict['includeSalesTaxFlag'] = None

        # set to None if inventory_soh_flag (nullable) is None
        # and model_fields_set contains the field
        if self.inventory_soh_flag is None and "inventory_soh_flag" in self.model_fields_set:
            _dict['inventorySOHFlag'] = None

        # set to None if invoice_format (nullable) is None
        # and model_fields_set contains the field
        if self.invoice_format is None and "invoice_format" in self.model_fields_set:
            _dict['invoiceFormat'] = None

        # set to None if send_component_amount_flag (nullable) is None
        # and model_fields_set contains the field
        if self.send_component_amount_flag is None and "send_component_amount_flag" in self.model_fields_set:
            _dict['sendComponentAmountFlag'] = None

        # set to None if send_uom_flag (nullable) is None
        # and model_fields_set contains the field
        if self.send_uom_flag is None and "send_uom_flag" in self.model_fields_set:
            _dict['sendUomFlag'] = None

        # set to None if suppress_memo_flag (nullable) is None
        # and model_fields_set contains the field
        if self.suppress_memo_flag is None and "suppress_memo_flag" in self.model_fields_set:
            _dict['suppressMemoFlag'] = None

        # set to None if sync_payment_info_flag (nullable) is None
        # and model_fields_set contains the field
        if self.sync_payment_info_flag is None and "sync_payment_info_flag" in self.model_fields_set:
            _dict['syncPaymentInfoFlag'] = None

        # set to None if sync_wise_pay_payment_info_flag (nullable) is None
        # and model_fields_set contains the field
        if self.sync_wise_pay_payment_info_flag is None and "sync_wise_pay_payment_info_flag" in self.model_fields_set:
            _dict['syncWisePayPaymentInfoFlag'] = None

        # set to None if transfer_expenses_as_bill_flag (nullable) is None
        # and model_fields_set contains the field
        if self.transfer_expenses_as_bill_flag is None and "transfer_expenses_as_bill_flag" in self.model_fields_set:
            _dict['transferExpensesAsBillFlag'] = None

        # set to None if wise_pay_lab_flag (nullable) is None
        # and model_fields_set contains the field
        if self.wise_pay_lab_flag is None and "wise_pay_lab_flag" in self.model_fields_set:
            _dict['wisePayLabFlag'] = None

        # set to None if zero_dollar_tax_amounts_flag (nullable) is None
        # and model_fields_set contains the field
        if self.zero_dollar_tax_amounts_flag is None and "zero_dollar_tax_amounts_flag" in self.model_fields_set:
            _dict['zeroDollarTaxAmountsFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AccountingPackageSetup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in AccountingPackageSetup) in the input: " + _key)

        _obj = cls.model_validate({
            "accountingPackage": AccountingPackageReference.from_dict(obj.get("accountingPackage")) if obj.get("accountingPackage") is not None else None,
            "directTransferFlag": obj.get("directTransferFlag"),
            "enableTaxGroupsFlag": obj.get("enableTaxGroupsFlag"),
            "expenseFormat": obj.get("expenseFormat"),
            "id": obj.get("id"),
            "includeCogsDropShipFlag": obj.get("includeCogsDropShipFlag"),
            "includeCogsEntriesFlag": obj.get("includeCogsEntriesFlag"),
            "includeExpensesFlag": obj.get("includeExpensesFlag"),
            "includeInvoicesFlag": obj.get("includeInvoicesFlag"),
            "includeItemsFlag": obj.get("includeItemsFlag"),
            "includeSalesTaxFlag": obj.get("includeSalesTaxFlag"),
            "inventorySOHFlag": obj.get("inventorySOHFlag"),
            "invoiceFormat": obj.get("invoiceFormat"),
            "sendComponentAmountFlag": obj.get("sendComponentAmountFlag"),
            "sendUomFlag": obj.get("sendUomFlag"),
            "suppressMemoFlag": obj.get("suppressMemoFlag"),
            "syncPaymentInfoFlag": obj.get("syncPaymentInfoFlag"),
            "syncWisePayPaymentInfoFlag": obj.get("syncWisePayPaymentInfoFlag"),
            "transferExpensesAsBillFlag": obj.get("transferExpensesAsBillFlag"),
            "wisePayLabFlag": obj.get("wisePayLabFlag"),
            "zeroDollarTaxAmountsFlag": obj.get("zeroDollarTaxAmountsFlag")
        })
        return _obj


