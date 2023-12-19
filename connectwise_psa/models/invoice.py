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
from connectwise_psa.models.agreement_reference import AgreementReference
from connectwise_psa.models.billing_setup_reference import BillingSetupReference
from connectwise_psa.models.billing_status_reference import BillingStatusReference
from connectwise_psa.models.billing_terms_reference import BillingTermsReference
from connectwise_psa.models.company_reference import CompanyReference
from connectwise_psa.models.currency_reference import CurrencyReference
from connectwise_psa.models.custom_field_value import CustomFieldValue
from connectwise_psa.models.invoice_template_detail_reference import InvoiceTemplateDetailReference
from connectwise_psa.models.project_phase_reference import ProjectPhaseReference
from connectwise_psa.models.project_reference import ProjectReference
from connectwise_psa.models.sales_order_reference import SalesOrderReference
from connectwise_psa.models.site_reference import SiteReference
from connectwise_psa.models.tax_code_reference import TaxCodeReference
from connectwise_psa.models.ticket_reference import TicketReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Invoice(BaseModel):
    """
    Invoice
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    account_number: Optional[StrictStr] = Field(default=None, alias="accountNumber")
    add_to_batch_email_list: Optional[StrictBool] = Field(default=None, alias="addToBatchEmailList")
    adjusted_by: Optional[StrictStr] = Field(default=None, alias="adjustedBy")
    adjustment_reason: Optional[StrictStr] = Field(default=None, alias="adjustmentReason")
    agreement: Optional[AgreementReference] = None
    agreement_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="agreementAmount")
    apply_to_id: Optional[StrictInt] = Field(default=None, alias="applyToId")
    apply_to_type: Optional[StrictStr] = Field(default=None, alias="applyToType")
    attention: Optional[StrictStr] = Field(default=None, description=" Max length: 60;")
    balance: Optional[Union[StrictFloat, StrictInt]] = None
    bill_to_company: Optional[CompanyReference] = Field(default=None, alias="billToCompany")
    billing_setup_reference: Optional[BillingSetupReference] = Field(default=None, alias="billingSetupReference")
    billing_site: Optional[SiteReference] = Field(default=None, alias="billingSite")
    billing_site_address_line1: Optional[StrictStr] = Field(default=None, alias="billingSiteAddressLine1")
    billing_site_address_line2: Optional[StrictStr] = Field(default=None, alias="billingSiteAddressLine2")
    billing_site_city: Optional[StrictStr] = Field(default=None, alias="billingSiteCity")
    billing_site_country: Optional[StrictStr] = Field(default=None, alias="billingSiteCountry")
    billing_site_state: Optional[StrictStr] = Field(default=None, alias="billingSiteState")
    billing_site_zip: Optional[StrictStr] = Field(default=None, alias="billingSiteZip")
    billing_terms: Optional[BillingTermsReference] = Field(default=None, alias="billingTerms")
    bottom_comment: Optional[StrictStr] = Field(default=None, alias="bottomComment")
    company: Optional[CompanyReference] = None
    credits: Optional[Union[StrictFloat, StrictInt]] = None
    currency: Optional[CurrencyReference] = None
    custom_fields: Optional[List[CustomFieldValue]] = Field(default=None, alias="customFields")
    customer_po: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="customerPO")
    var_date: Optional[datetime] = Field(default=None, alias="date")
    department_id: Optional[StrictInt] = Field(default=None, description="departmentId is only required for special invoices.", alias="departmentId")
    downpayment_applied: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="downpaymentApplied")
    downpayment_previously_taxed_flag: Optional[StrictBool] = Field(default=None, alias="downpaymentPreviouslyTaxedFlag")
    due_date: Optional[datetime] = Field(default=None, alias="dueDate")
    email_template_id: Optional[StrictInt] = Field(default=None, description="Can be obtained via InvoiceEmailTemplate report.", alias="emailTemplateId")
    expense_total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="expenseTotal")
    id: Optional[StrictInt] = None
    internal_notes: Optional[StrictStr] = Field(default=None, alias="internalNotes")
    invoice_number: Optional[StrictStr] = Field(default=None, description=" Max length: 15; Required On Updates;", alias="invoiceNumber")
    invoice_template: Optional[InvoiceTemplateDetailReference] = Field(default=None, alias="invoiceTemplate")
    location_id: Optional[StrictInt] = Field(default=None, description=" Required On Updates;", alias="locationId")
    override_down_payment_amount_flag: Optional[StrictBool] = Field(default=None, alias="overrideDownPaymentAmountFlag")
    payments: Optional[Union[StrictFloat, StrictInt]] = None
    phase: Optional[ProjectPhaseReference] = None
    previous_progress_applied: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="previousProgressApplied")
    product_total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="productTotal")
    project: Optional[ProjectReference] = None
    reference: Optional[StrictStr] = Field(default=None, description=" Max length: 50;")
    remaining_downpayment: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="remainingDownpayment")
    restrict_downpayment_flag: Optional[StrictBool] = Field(default=None, alias="restrictDownpaymentFlag")
    sales_order: Optional[SalesOrderReference] = Field(default=None, alias="salesOrder")
    sales_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="salesTax")
    service_adjustment_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="serviceAdjustmentAmount")
    service_total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="serviceTotal")
    ship_to_attention: Optional[StrictStr] = Field(default=None, description=" Max length: 60;", alias="shipToAttention")
    ship_to_company: Optional[CompanyReference] = Field(default=None, alias="shipToCompany")
    shipping_site: Optional[SiteReference] = Field(default=None, alias="shippingSite")
    shipping_site_address_line1: Optional[StrictStr] = Field(default=None, alias="shippingSiteAddressLine1")
    shipping_site_address_line2: Optional[StrictStr] = Field(default=None, alias="shippingSiteAddressLine2")
    shipping_site_city: Optional[StrictStr] = Field(default=None, alias="shippingSiteCity")
    shipping_site_country: Optional[StrictStr] = Field(default=None, alias="shippingSiteCountry")
    shipping_site_state: Optional[StrictStr] = Field(default=None, alias="shippingSiteState")
    shipping_site_zip: Optional[StrictStr] = Field(default=None, alias="shippingSiteZip")
    special_invoice_flag: Optional[StrictBool] = Field(default=None, alias="specialInvoiceFlag")
    status: Optional[BillingStatusReference] = None
    subtotal: Optional[Union[StrictFloat, StrictInt]] = None
    tax_code: Optional[TaxCodeReference] = Field(default=None, alias="taxCode")
    taxable_flag: Optional[StrictBool] = Field(default=None, alias="taxableFlag")
    template_setup_id: Optional[StrictInt] = Field(default=None, description="Can be obtained via InvoiceTemplate report.", alias="templateSetupId")
    territory_id: Optional[StrictInt] = Field(default=None, alias="territoryId")
    ticket: Optional[TicketReference] = None
    top_comment: Optional[StrictStr] = Field(default=None, alias="topComment")
    total: Optional[Union[StrictFloat, StrictInt]] = None
    type: Optional[StrictStr]
    __properties: ClassVar[List[str]] = ["_info", "accountNumber", "addToBatchEmailList", "adjustedBy", "adjustmentReason", "agreement", "agreementAmount", "applyToId", "applyToType", "attention", "balance", "billToCompany", "billingSetupReference", "billingSite", "billingSiteAddressLine1", "billingSiteAddressLine2", "billingSiteCity", "billingSiteCountry", "billingSiteState", "billingSiteZip", "billingTerms", "bottomComment", "company", "credits", "currency", "customFields", "customerPO", "date", "departmentId", "downpaymentApplied", "downpaymentPreviouslyTaxedFlag", "dueDate", "emailTemplateId", "expenseTotal", "id", "internalNotes", "invoiceNumber", "invoiceTemplate", "locationId", "overrideDownPaymentAmountFlag", "payments", "phase", "previousProgressApplied", "productTotal", "project", "reference", "remainingDownpayment", "restrictDownpaymentFlag", "salesOrder", "salesTax", "serviceAdjustmentAmount", "serviceTotal", "shipToAttention", "shipToCompany", "shippingSite", "shippingSiteAddressLine1", "shippingSiteAddressLine2", "shippingSiteCity", "shippingSiteCountry", "shippingSiteState", "shippingSiteZip", "specialInvoiceFlag", "status", "subtotal", "taxCode", "taxableFlag", "templateSetupId", "territoryId", "ticket", "topComment", "total", "type"]

    @field_validator('apply_to_type')
    def apply_to_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('All', 'Agreement', 'Project', 'ProjectPhase', 'SalesOrder', 'Ticket'):
            raise ValueError("must be one of enum values ('All', 'Agreement', 'Project', 'ProjectPhase', 'SalesOrder', 'Ticket')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Agreement', 'CreditMemo', 'DownPayment', 'Miscellaneous', 'Progress', 'Standard'):
            raise ValueError("must be one of enum values ('Agreement', 'CreditMemo', 'DownPayment', 'Miscellaneous', 'Progress', 'Standard')")
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
        """Create an instance of Invoice from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of agreement
        if self.agreement:
            _dict['agreement'] = self.agreement.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bill_to_company
        if self.bill_to_company:
            _dict['billToCompany'] = self.bill_to_company.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billing_setup_reference
        if self.billing_setup_reference:
            _dict['billingSetupReference'] = self.billing_setup_reference.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billing_site
        if self.billing_site:
            _dict['billingSite'] = self.billing_site.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billing_terms
        if self.billing_terms:
            _dict['billingTerms'] = self.billing_terms.to_dict()
        # override the default output from pydantic by calling `to_dict()` of company
        if self.company:
            _dict['company'] = self.company.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency
        if self.currency:
            _dict['currency'] = self.currency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in custom_fields (list)
        _items = []
        if self.custom_fields:
            for _item in self.custom_fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customFields'] = _items
        # override the default output from pydantic by calling `to_dict()` of invoice_template
        if self.invoice_template:
            _dict['invoiceTemplate'] = self.invoice_template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of phase
        if self.phase:
            _dict['phase'] = self.phase.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sales_order
        if self.sales_order:
            _dict['salesOrder'] = self.sales_order.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ship_to_company
        if self.ship_to_company:
            _dict['shipToCompany'] = self.ship_to_company.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_site
        if self.shipping_site:
            _dict['shippingSite'] = self.shipping_site.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tax_code
        if self.tax_code:
            _dict['taxCode'] = self.tax_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ticket
        if self.ticket:
            _dict['ticket'] = self.ticket.to_dict()
        # set to None if add_to_batch_email_list (nullable) is None
        # and model_fields_set contains the field
        if self.add_to_batch_email_list is None and "add_to_batch_email_list" in self.model_fields_set:
            _dict['addToBatchEmailList'] = None

        # set to None if agreement_amount (nullable) is None
        # and model_fields_set contains the field
        if self.agreement_amount is None and "agreement_amount" in self.model_fields_set:
            _dict['agreementAmount'] = None

        # set to None if apply_to_id (nullable) is None
        # and model_fields_set contains the field
        if self.apply_to_id is None and "apply_to_id" in self.model_fields_set:
            _dict['applyToId'] = None

        # set to None if apply_to_type (nullable) is None
        # and model_fields_set contains the field
        if self.apply_to_type is None and "apply_to_type" in self.model_fields_set:
            _dict['applyToType'] = None

        # set to None if balance (nullable) is None
        # and model_fields_set contains the field
        if self.balance is None and "balance" in self.model_fields_set:
            _dict['balance'] = None

        # set to None if credits (nullable) is None
        # and model_fields_set contains the field
        if self.credits is None and "credits" in self.model_fields_set:
            _dict['credits'] = None

        # set to None if department_id (nullable) is None
        # and model_fields_set contains the field
        if self.department_id is None and "department_id" in self.model_fields_set:
            _dict['departmentId'] = None

        # set to None if downpayment_applied (nullable) is None
        # and model_fields_set contains the field
        if self.downpayment_applied is None and "downpayment_applied" in self.model_fields_set:
            _dict['downpaymentApplied'] = None

        # set to None if downpayment_previously_taxed_flag (nullable) is None
        # and model_fields_set contains the field
        if self.downpayment_previously_taxed_flag is None and "downpayment_previously_taxed_flag" in self.model_fields_set:
            _dict['downpaymentPreviouslyTaxedFlag'] = None

        # set to None if email_template_id (nullable) is None
        # and model_fields_set contains the field
        if self.email_template_id is None and "email_template_id" in self.model_fields_set:
            _dict['emailTemplateId'] = None

        # set to None if expense_total (nullable) is None
        # and model_fields_set contains the field
        if self.expense_total is None and "expense_total" in self.model_fields_set:
            _dict['expenseTotal'] = None

        # set to None if location_id (nullable) is None
        # and model_fields_set contains the field
        if self.location_id is None and "location_id" in self.model_fields_set:
            _dict['locationId'] = None

        # set to None if override_down_payment_amount_flag (nullable) is None
        # and model_fields_set contains the field
        if self.override_down_payment_amount_flag is None and "override_down_payment_amount_flag" in self.model_fields_set:
            _dict['overrideDownPaymentAmountFlag'] = None

        # set to None if payments (nullable) is None
        # and model_fields_set contains the field
        if self.payments is None and "payments" in self.model_fields_set:
            _dict['payments'] = None

        # set to None if previous_progress_applied (nullable) is None
        # and model_fields_set contains the field
        if self.previous_progress_applied is None and "previous_progress_applied" in self.model_fields_set:
            _dict['previousProgressApplied'] = None

        # set to None if product_total (nullable) is None
        # and model_fields_set contains the field
        if self.product_total is None and "product_total" in self.model_fields_set:
            _dict['productTotal'] = None

        # set to None if remaining_downpayment (nullable) is None
        # and model_fields_set contains the field
        if self.remaining_downpayment is None and "remaining_downpayment" in self.model_fields_set:
            _dict['remainingDownpayment'] = None

        # set to None if restrict_downpayment_flag (nullable) is None
        # and model_fields_set contains the field
        if self.restrict_downpayment_flag is None and "restrict_downpayment_flag" in self.model_fields_set:
            _dict['restrictDownpaymentFlag'] = None

        # set to None if sales_tax (nullable) is None
        # and model_fields_set contains the field
        if self.sales_tax is None and "sales_tax" in self.model_fields_set:
            _dict['salesTax'] = None

        # set to None if service_adjustment_amount (nullable) is None
        # and model_fields_set contains the field
        if self.service_adjustment_amount is None and "service_adjustment_amount" in self.model_fields_set:
            _dict['serviceAdjustmentAmount'] = None

        # set to None if service_total (nullable) is None
        # and model_fields_set contains the field
        if self.service_total is None and "service_total" in self.model_fields_set:
            _dict['serviceTotal'] = None

        # set to None if special_invoice_flag (nullable) is None
        # and model_fields_set contains the field
        if self.special_invoice_flag is None and "special_invoice_flag" in self.model_fields_set:
            _dict['specialInvoiceFlag'] = None

        # set to None if subtotal (nullable) is None
        # and model_fields_set contains the field
        if self.subtotal is None and "subtotal" in self.model_fields_set:
            _dict['subtotal'] = None

        # set to None if taxable_flag (nullable) is None
        # and model_fields_set contains the field
        if self.taxable_flag is None and "taxable_flag" in self.model_fields_set:
            _dict['taxableFlag'] = None

        # set to None if template_setup_id (nullable) is None
        # and model_fields_set contains the field
        if self.template_setup_id is None and "template_setup_id" in self.model_fields_set:
            _dict['templateSetupId'] = None

        # set to None if territory_id (nullable) is None
        # and model_fields_set contains the field
        if self.territory_id is None and "territory_id" in self.model_fields_set:
            _dict['territoryId'] = None

        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict['total'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Invoice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Invoice) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "accountNumber": obj.get("accountNumber"),
            "addToBatchEmailList": obj.get("addToBatchEmailList"),
            "adjustedBy": obj.get("adjustedBy"),
            "adjustmentReason": obj.get("adjustmentReason"),
            "agreement": AgreementReference.from_dict(obj.get("agreement")) if obj.get("agreement") is not None else None,
            "agreementAmount": obj.get("agreementAmount"),
            "applyToId": obj.get("applyToId"),
            "applyToType": obj.get("applyToType"),
            "attention": obj.get("attention"),
            "balance": obj.get("balance"),
            "billToCompany": CompanyReference.from_dict(obj.get("billToCompany")) if obj.get("billToCompany") is not None else None,
            "billingSetupReference": BillingSetupReference.from_dict(obj.get("billingSetupReference")) if obj.get("billingSetupReference") is not None else None,
            "billingSite": SiteReference.from_dict(obj.get("billingSite")) if obj.get("billingSite") is not None else None,
            "billingSiteAddressLine1": obj.get("billingSiteAddressLine1"),
            "billingSiteAddressLine2": obj.get("billingSiteAddressLine2"),
            "billingSiteCity": obj.get("billingSiteCity"),
            "billingSiteCountry": obj.get("billingSiteCountry"),
            "billingSiteState": obj.get("billingSiteState"),
            "billingSiteZip": obj.get("billingSiteZip"),
            "billingTerms": BillingTermsReference.from_dict(obj.get("billingTerms")) if obj.get("billingTerms") is not None else None,
            "bottomComment": obj.get("bottomComment"),
            "company": CompanyReference.from_dict(obj.get("company")) if obj.get("company") is not None else None,
            "credits": obj.get("credits"),
            "currency": CurrencyReference.from_dict(obj.get("currency")) if obj.get("currency") is not None else None,
            "customFields": [CustomFieldValue.from_dict(_item) for _item in obj.get("customFields")] if obj.get("customFields") is not None else None,
            "customerPO": obj.get("customerPO"),
            "date": obj.get("date"),
            "departmentId": obj.get("departmentId"),
            "downpaymentApplied": obj.get("downpaymentApplied"),
            "downpaymentPreviouslyTaxedFlag": obj.get("downpaymentPreviouslyTaxedFlag"),
            "dueDate": obj.get("dueDate"),
            "emailTemplateId": obj.get("emailTemplateId"),
            "expenseTotal": obj.get("expenseTotal"),
            "id": obj.get("id"),
            "internalNotes": obj.get("internalNotes"),
            "invoiceNumber": obj.get("invoiceNumber"),
            "invoiceTemplate": InvoiceTemplateDetailReference.from_dict(obj.get("invoiceTemplate")) if obj.get("invoiceTemplate") is not None else None,
            "locationId": obj.get("locationId"),
            "overrideDownPaymentAmountFlag": obj.get("overrideDownPaymentAmountFlag"),
            "payments": obj.get("payments"),
            "phase": ProjectPhaseReference.from_dict(obj.get("phase")) if obj.get("phase") is not None else None,
            "previousProgressApplied": obj.get("previousProgressApplied"),
            "productTotal": obj.get("productTotal"),
            "project": ProjectReference.from_dict(obj.get("project")) if obj.get("project") is not None else None,
            "reference": obj.get("reference"),
            "remainingDownpayment": obj.get("remainingDownpayment"),
            "restrictDownpaymentFlag": obj.get("restrictDownpaymentFlag"),
            "salesOrder": SalesOrderReference.from_dict(obj.get("salesOrder")) if obj.get("salesOrder") is not None else None,
            "salesTax": obj.get("salesTax"),
            "serviceAdjustmentAmount": obj.get("serviceAdjustmentAmount"),
            "serviceTotal": obj.get("serviceTotal"),
            "shipToAttention": obj.get("shipToAttention"),
            "shipToCompany": CompanyReference.from_dict(obj.get("shipToCompany")) if obj.get("shipToCompany") is not None else None,
            "shippingSite": SiteReference.from_dict(obj.get("shippingSite")) if obj.get("shippingSite") is not None else None,
            "shippingSiteAddressLine1": obj.get("shippingSiteAddressLine1"),
            "shippingSiteAddressLine2": obj.get("shippingSiteAddressLine2"),
            "shippingSiteCity": obj.get("shippingSiteCity"),
            "shippingSiteCountry": obj.get("shippingSiteCountry"),
            "shippingSiteState": obj.get("shippingSiteState"),
            "shippingSiteZip": obj.get("shippingSiteZip"),
            "specialInvoiceFlag": obj.get("specialInvoiceFlag"),
            "status": BillingStatusReference.from_dict(obj.get("status")) if obj.get("status") is not None else None,
            "subtotal": obj.get("subtotal"),
            "taxCode": TaxCodeReference.from_dict(obj.get("taxCode")) if obj.get("taxCode") is not None else None,
            "taxableFlag": obj.get("taxableFlag"),
            "templateSetupId": obj.get("templateSetupId"),
            "territoryId": obj.get("territoryId"),
            "ticket": TicketReference.from_dict(obj.get("ticket")) if obj.get("ticket") is not None else None,
            "topComment": obj.get("topComment"),
            "total": obj.get("total"),
            "type": obj.get("type")
        })
        return _obj


