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
from connectwise_psa.models.country_reference import CountryReference
from connectwise_psa.models.currency_reference import CurrencyReference
from connectwise_psa.models.email_template_reference import EmailTemplateReference
from connectwise_psa.models.invoice_template_reference import InvoiceTemplateReference
from connectwise_psa.models.state_reference import StateReference
from connectwise_psa.models.system_location_reference import SystemLocationReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class BillingSetup(BaseModel):
    """
    BillingSetup
    """ # noqa: E501
    info: Optional[Dict[str, StrictStr]] = Field(default=None, alias="_info")
    address_one: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="addressOne")
    address_two: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="addressTwo")
    agreement_invoice: Optional[InvoiceTemplateReference] = Field(default=None, alias="agreementInvoice")
    allow_restricted_dept_on_routing_flag: Optional[StrictBool] = Field(default=None, alias="allowRestrictedDeptOnRoutingFlag")
    attach_xml_invoice_flag: Optional[StrictBool] = Field(default=None, alias="attachXmlInvoiceFlag")
    bill_product_after_ship_flag: Optional[StrictBool] = Field(default=None, alias="billProductAfterShipFlag")
    bill_project_complete_flag: Optional[StrictBool] = Field(default=None, alias="billProjectCompleteFlag")
    bill_project_unapproved_flag: Optional[StrictBool] = Field(default=None, alias="billProjectUnapprovedFlag")
    bill_sales_order_complete_flag: Optional[StrictBool] = Field(default=None, alias="billSalesOrderCompleteFlag")
    bill_ticket_complete_flag: Optional[StrictBool] = Field(default=None, alias="billTicketCompleteFlag")
    bill_ticket_separately_flag: Optional[StrictBool] = Field(default=None, alias="billTicketSeparatelyFlag")
    bill_ticket_unapproved_flag: Optional[StrictBool] = Field(default=None, alias="billTicketUnapprovedFlag")
    business_number: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="businessNumber")
    charge_adj_to_firm_flag: Optional[StrictBool] = Field(default=None, alias="chargeAdjToFirmFlag")
    city: Optional[StrictStr] = Field(default=None, description=" Max length: 50;")
    company_code: Optional[StrictStr] = Field(default=None, description=" Max length: 250;", alias="companyCode")
    copy_agreement_products_flag: Optional[StrictBool] = Field(default=None, alias="copyAgreementProductsFlag")
    copy_non_service_products_flag: Optional[StrictBool] = Field(default=None, alias="copyNonServiceProductsFlag")
    copy_service_products_flag: Optional[StrictBool] = Field(default=None, alias="copyServiceProductsFlag")
    country: Optional[CountryReference] = None
    credit_memo_invoice: Optional[InvoiceTemplateReference] = Field(default=None, alias="creditMemoInvoice")
    currency: Optional[CurrencyReference] = None
    custom_label: Optional[StrictStr] = Field(default=None, description=" Max length: 50;", alias="customLabel")
    custom_text: Optional[StrictStr] = Field(default=None, description=" Max length: 500;", alias="customText")
    delivery_receipt_flag: Optional[StrictBool] = Field(default=None, alias="deliveryReceiptFlag")
    disable_routing_email_flag: Optional[StrictBool] = Field(default=None, alias="disableRoutingEmailFlag")
    display_tax_flag: Optional[StrictBool] = Field(default=None, alias="displayTaxFlag")
    down_payment_invoice: Optional[InvoiceTemplateReference] = Field(default=None, alias="downPaymentInvoice")
    email_template: EmailTemplateReference = Field(alias="emailTemplate")
    exclude_avalara_flag: Optional[StrictBool] = Field(default=None, alias="excludeAvalaraFlag")
    exclude_do_not_bill_expense_flag: Optional[StrictBool] = Field(default=None, alias="excludeDoNotBillExpenseFlag")
    exclude_do_not_bill_product_flag: Optional[StrictBool] = Field(default=None, alias="excludeDoNotBillProductFlag")
    exclude_do_not_bill_time_flag: Optional[StrictBool] = Field(default=None, alias="excludeDoNotBillTimeFlag")
    id: Optional[StrictInt] = None
    invoice_footer: Optional[StrictStr] = Field(default=None, description=" Max length: 500;", alias="invoiceFooter")
    invoice_title: StrictStr = Field(description=" Max length: 50;", alias="invoiceTitle")
    localized_country: Optional[CountryReference] = Field(default=None, alias="localizedCountry")
    location: SystemLocationReference
    misc_invoice: Optional[InvoiceTemplateReference] = Field(default=None, alias="miscInvoice")
    no_watermark_flag: Optional[StrictBool] = Field(default=None, alias="noWatermarkFlag")
    overall_invoice_default: Optional[InvoiceTemplateReference] = Field(default=None, alias="overallInvoiceDefault")
    payable_name: StrictStr = Field(description=" Max length: 50;", alias="payableName")
    phone: Optional[StrictStr] = Field(default=None, description=" Max length: 15;")
    prefix_suffix_flag: Optional[StrictStr] = Field(default=None, alias="prefixSuffixFlag")
    prefix_suffix_text: Optional[StrictStr] = Field(default=None, description=" Max length: 5;", alias="prefixSuffixText")
    print_logo_flag: Optional[StrictBool] = Field(default=None, alias="printLogoFlag")
    progress_invoice: Optional[InvoiceTemplateReference] = Field(default=None, alias="progressInvoice")
    progress_time_flag: Optional[StrictBool] = Field(default=None, alias="progressTimeFlag")
    quote_footer: Optional[StrictStr] = Field(default=None, description=" Max length: 1000;", alias="quoteFooter")
    read_receipt_flag: Optional[StrictBool] = Field(default=None, alias="readReceiptFlag")
    remit_name: StrictStr = Field(description=" Max length: 50;", alias="remitName")
    restrict_downpayment_flag: Optional[StrictBool] = Field(default=None, alias="restrictDownpaymentFlag")
    restrict_project_downpayment_flag: Optional[StrictBool] = Field(default=None, alias="restrictProjectDownpaymentFlag")
    sales_order_invoice: Optional[InvoiceTemplateReference] = Field(default=None, alias="salesOrderInvoice")
    standard_invoice_actual: Optional[InvoiceTemplateReference] = Field(default=None, alias="standardInvoiceActual")
    standard_invoice_fixed: Optional[InvoiceTemplateReference] = Field(default=None, alias="standardInvoiceFixed")
    state: Optional[StateReference] = None
    topcomment: Optional[StrictStr] = Field(default=None, description=" Max length: 4000;")
    zip: Optional[StrictStr] = Field(default=None, description=" Max length: 12;")
    __properties: ClassVar[List[str]] = ["_info", "addressOne", "addressTwo", "agreementInvoice", "allowRestrictedDeptOnRoutingFlag", "attachXmlInvoiceFlag", "billProductAfterShipFlag", "billProjectCompleteFlag", "billProjectUnapprovedFlag", "billSalesOrderCompleteFlag", "billTicketCompleteFlag", "billTicketSeparatelyFlag", "billTicketUnapprovedFlag", "businessNumber", "chargeAdjToFirmFlag", "city", "companyCode", "copyAgreementProductsFlag", "copyNonServiceProductsFlag", "copyServiceProductsFlag", "country", "creditMemoInvoice", "currency", "customLabel", "customText", "deliveryReceiptFlag", "disableRoutingEmailFlag", "displayTaxFlag", "downPaymentInvoice", "emailTemplate", "excludeAvalaraFlag", "excludeDoNotBillExpenseFlag", "excludeDoNotBillProductFlag", "excludeDoNotBillTimeFlag", "id", "invoiceFooter", "invoiceTitle", "localizedCountry", "location", "miscInvoice", "noWatermarkFlag", "overallInvoiceDefault", "payableName", "phone", "prefixSuffixFlag", "prefixSuffixText", "printLogoFlag", "progressInvoice", "progressTimeFlag", "quoteFooter", "readReceiptFlag", "remitName", "restrictDownpaymentFlag", "restrictProjectDownpaymentFlag", "salesOrderInvoice", "standardInvoiceActual", "standardInvoiceFixed", "state", "topcomment", "zip"]

    @field_validator('prefix_suffix_flag')
    def prefix_suffix_flag_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Prefix', 'Suffix'):
            raise ValueError("must be one of enum values ('Prefix', 'Suffix')")
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
        """Create an instance of BillingSetup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of agreement_invoice
        if self.agreement_invoice:
            _dict['agreementInvoice'] = self.agreement_invoice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of country
        if self.country:
            _dict['country'] = self.country.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credit_memo_invoice
        if self.credit_memo_invoice:
            _dict['creditMemoInvoice'] = self.credit_memo_invoice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency
        if self.currency:
            _dict['currency'] = self.currency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of down_payment_invoice
        if self.down_payment_invoice:
            _dict['downPaymentInvoice'] = self.down_payment_invoice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of email_template
        if self.email_template:
            _dict['emailTemplate'] = self.email_template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of localized_country
        if self.localized_country:
            _dict['localizedCountry'] = self.localized_country.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of misc_invoice
        if self.misc_invoice:
            _dict['miscInvoice'] = self.misc_invoice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of overall_invoice_default
        if self.overall_invoice_default:
            _dict['overallInvoiceDefault'] = self.overall_invoice_default.to_dict()
        # override the default output from pydantic by calling `to_dict()` of progress_invoice
        if self.progress_invoice:
            _dict['progressInvoice'] = self.progress_invoice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sales_order_invoice
        if self.sales_order_invoice:
            _dict['salesOrderInvoice'] = self.sales_order_invoice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of standard_invoice_actual
        if self.standard_invoice_actual:
            _dict['standardInvoiceActual'] = self.standard_invoice_actual.to_dict()
        # override the default output from pydantic by calling `to_dict()` of standard_invoice_fixed
        if self.standard_invoice_fixed:
            _dict['standardInvoiceFixed'] = self.standard_invoice_fixed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # set to None if allow_restricted_dept_on_routing_flag (nullable) is None
        # and model_fields_set contains the field
        if self.allow_restricted_dept_on_routing_flag is None and "allow_restricted_dept_on_routing_flag" in self.model_fields_set:
            _dict['allowRestrictedDeptOnRoutingFlag'] = None

        # set to None if attach_xml_invoice_flag (nullable) is None
        # and model_fields_set contains the field
        if self.attach_xml_invoice_flag is None and "attach_xml_invoice_flag" in self.model_fields_set:
            _dict['attachXmlInvoiceFlag'] = None

        # set to None if bill_product_after_ship_flag (nullable) is None
        # and model_fields_set contains the field
        if self.bill_product_after_ship_flag is None and "bill_product_after_ship_flag" in self.model_fields_set:
            _dict['billProductAfterShipFlag'] = None

        # set to None if bill_project_complete_flag (nullable) is None
        # and model_fields_set contains the field
        if self.bill_project_complete_flag is None and "bill_project_complete_flag" in self.model_fields_set:
            _dict['billProjectCompleteFlag'] = None

        # set to None if bill_project_unapproved_flag (nullable) is None
        # and model_fields_set contains the field
        if self.bill_project_unapproved_flag is None and "bill_project_unapproved_flag" in self.model_fields_set:
            _dict['billProjectUnapprovedFlag'] = None

        # set to None if bill_sales_order_complete_flag (nullable) is None
        # and model_fields_set contains the field
        if self.bill_sales_order_complete_flag is None and "bill_sales_order_complete_flag" in self.model_fields_set:
            _dict['billSalesOrderCompleteFlag'] = None

        # set to None if bill_ticket_complete_flag (nullable) is None
        # and model_fields_set contains the field
        if self.bill_ticket_complete_flag is None and "bill_ticket_complete_flag" in self.model_fields_set:
            _dict['billTicketCompleteFlag'] = None

        # set to None if bill_ticket_separately_flag (nullable) is None
        # and model_fields_set contains the field
        if self.bill_ticket_separately_flag is None and "bill_ticket_separately_flag" in self.model_fields_set:
            _dict['billTicketSeparatelyFlag'] = None

        # set to None if bill_ticket_unapproved_flag (nullable) is None
        # and model_fields_set contains the field
        if self.bill_ticket_unapproved_flag is None and "bill_ticket_unapproved_flag" in self.model_fields_set:
            _dict['billTicketUnapprovedFlag'] = None

        # set to None if charge_adj_to_firm_flag (nullable) is None
        # and model_fields_set contains the field
        if self.charge_adj_to_firm_flag is None and "charge_adj_to_firm_flag" in self.model_fields_set:
            _dict['chargeAdjToFirmFlag'] = None

        # set to None if copy_agreement_products_flag (nullable) is None
        # and model_fields_set contains the field
        if self.copy_agreement_products_flag is None and "copy_agreement_products_flag" in self.model_fields_set:
            _dict['copyAgreementProductsFlag'] = None

        # set to None if copy_non_service_products_flag (nullable) is None
        # and model_fields_set contains the field
        if self.copy_non_service_products_flag is None and "copy_non_service_products_flag" in self.model_fields_set:
            _dict['copyNonServiceProductsFlag'] = None

        # set to None if copy_service_products_flag (nullable) is None
        # and model_fields_set contains the field
        if self.copy_service_products_flag is None and "copy_service_products_flag" in self.model_fields_set:
            _dict['copyServiceProductsFlag'] = None

        # set to None if delivery_receipt_flag (nullable) is None
        # and model_fields_set contains the field
        if self.delivery_receipt_flag is None and "delivery_receipt_flag" in self.model_fields_set:
            _dict['deliveryReceiptFlag'] = None

        # set to None if disable_routing_email_flag (nullable) is None
        # and model_fields_set contains the field
        if self.disable_routing_email_flag is None and "disable_routing_email_flag" in self.model_fields_set:
            _dict['disableRoutingEmailFlag'] = None

        # set to None if display_tax_flag (nullable) is None
        # and model_fields_set contains the field
        if self.display_tax_flag is None and "display_tax_flag" in self.model_fields_set:
            _dict['displayTaxFlag'] = None

        # set to None if exclude_avalara_flag (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_avalara_flag is None and "exclude_avalara_flag" in self.model_fields_set:
            _dict['excludeAvalaraFlag'] = None

        # set to None if exclude_do_not_bill_expense_flag (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_do_not_bill_expense_flag is None and "exclude_do_not_bill_expense_flag" in self.model_fields_set:
            _dict['excludeDoNotBillExpenseFlag'] = None

        # set to None if exclude_do_not_bill_product_flag (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_do_not_bill_product_flag is None and "exclude_do_not_bill_product_flag" in self.model_fields_set:
            _dict['excludeDoNotBillProductFlag'] = None

        # set to None if exclude_do_not_bill_time_flag (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_do_not_bill_time_flag is None and "exclude_do_not_bill_time_flag" in self.model_fields_set:
            _dict['excludeDoNotBillTimeFlag'] = None

        # set to None if no_watermark_flag (nullable) is None
        # and model_fields_set contains the field
        if self.no_watermark_flag is None and "no_watermark_flag" in self.model_fields_set:
            _dict['noWatermarkFlag'] = None

        # set to None if prefix_suffix_flag (nullable) is None
        # and model_fields_set contains the field
        if self.prefix_suffix_flag is None and "prefix_suffix_flag" in self.model_fields_set:
            _dict['prefixSuffixFlag'] = None

        # set to None if print_logo_flag (nullable) is None
        # and model_fields_set contains the field
        if self.print_logo_flag is None and "print_logo_flag" in self.model_fields_set:
            _dict['printLogoFlag'] = None

        # set to None if progress_time_flag (nullable) is None
        # and model_fields_set contains the field
        if self.progress_time_flag is None and "progress_time_flag" in self.model_fields_set:
            _dict['progressTimeFlag'] = None

        # set to None if read_receipt_flag (nullable) is None
        # and model_fields_set contains the field
        if self.read_receipt_flag is None and "read_receipt_flag" in self.model_fields_set:
            _dict['readReceiptFlag'] = None

        # set to None if restrict_downpayment_flag (nullable) is None
        # and model_fields_set contains the field
        if self.restrict_downpayment_flag is None and "restrict_downpayment_flag" in self.model_fields_set:
            _dict['restrictDownpaymentFlag'] = None

        # set to None if restrict_project_downpayment_flag (nullable) is None
        # and model_fields_set contains the field
        if self.restrict_project_downpayment_flag is None and "restrict_project_downpayment_flag" in self.model_fields_set:
            _dict['restrictProjectDownpaymentFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of BillingSetup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in BillingSetup) in the input: " + _key)

        _obj = cls.model_validate({
            "_info": obj.get("_info"),
            "addressOne": obj.get("addressOne"),
            "addressTwo": obj.get("addressTwo"),
            "agreementInvoice": InvoiceTemplateReference.from_dict(obj.get("agreementInvoice")) if obj.get("agreementInvoice") is not None else None,
            "allowRestrictedDeptOnRoutingFlag": obj.get("allowRestrictedDeptOnRoutingFlag"),
            "attachXmlInvoiceFlag": obj.get("attachXmlInvoiceFlag"),
            "billProductAfterShipFlag": obj.get("billProductAfterShipFlag"),
            "billProjectCompleteFlag": obj.get("billProjectCompleteFlag"),
            "billProjectUnapprovedFlag": obj.get("billProjectUnapprovedFlag"),
            "billSalesOrderCompleteFlag": obj.get("billSalesOrderCompleteFlag"),
            "billTicketCompleteFlag": obj.get("billTicketCompleteFlag"),
            "billTicketSeparatelyFlag": obj.get("billTicketSeparatelyFlag"),
            "billTicketUnapprovedFlag": obj.get("billTicketUnapprovedFlag"),
            "businessNumber": obj.get("businessNumber"),
            "chargeAdjToFirmFlag": obj.get("chargeAdjToFirmFlag"),
            "city": obj.get("city"),
            "companyCode": obj.get("companyCode"),
            "copyAgreementProductsFlag": obj.get("copyAgreementProductsFlag"),
            "copyNonServiceProductsFlag": obj.get("copyNonServiceProductsFlag"),
            "copyServiceProductsFlag": obj.get("copyServiceProductsFlag"),
            "country": CountryReference.from_dict(obj.get("country")) if obj.get("country") is not None else None,
            "creditMemoInvoice": InvoiceTemplateReference.from_dict(obj.get("creditMemoInvoice")) if obj.get("creditMemoInvoice") is not None else None,
            "currency": CurrencyReference.from_dict(obj.get("currency")) if obj.get("currency") is not None else None,
            "customLabel": obj.get("customLabel"),
            "customText": obj.get("customText"),
            "deliveryReceiptFlag": obj.get("deliveryReceiptFlag"),
            "disableRoutingEmailFlag": obj.get("disableRoutingEmailFlag"),
            "displayTaxFlag": obj.get("displayTaxFlag"),
            "downPaymentInvoice": InvoiceTemplateReference.from_dict(obj.get("downPaymentInvoice")) if obj.get("downPaymentInvoice") is not None else None,
            "emailTemplate": EmailTemplateReference.from_dict(obj.get("emailTemplate")) if obj.get("emailTemplate") is not None else None,
            "excludeAvalaraFlag": obj.get("excludeAvalaraFlag"),
            "excludeDoNotBillExpenseFlag": obj.get("excludeDoNotBillExpenseFlag"),
            "excludeDoNotBillProductFlag": obj.get("excludeDoNotBillProductFlag"),
            "excludeDoNotBillTimeFlag": obj.get("excludeDoNotBillTimeFlag"),
            "id": obj.get("id"),
            "invoiceFooter": obj.get("invoiceFooter"),
            "invoiceTitle": obj.get("invoiceTitle"),
            "localizedCountry": CountryReference.from_dict(obj.get("localizedCountry")) if obj.get("localizedCountry") is not None else None,
            "location": SystemLocationReference.from_dict(obj.get("location")) if obj.get("location") is not None else None,
            "miscInvoice": InvoiceTemplateReference.from_dict(obj.get("miscInvoice")) if obj.get("miscInvoice") is not None else None,
            "noWatermarkFlag": obj.get("noWatermarkFlag"),
            "overallInvoiceDefault": InvoiceTemplateReference.from_dict(obj.get("overallInvoiceDefault")) if obj.get("overallInvoiceDefault") is not None else None,
            "payableName": obj.get("payableName"),
            "phone": obj.get("phone"),
            "prefixSuffixFlag": obj.get("prefixSuffixFlag"),
            "prefixSuffixText": obj.get("prefixSuffixText"),
            "printLogoFlag": obj.get("printLogoFlag"),
            "progressInvoice": InvoiceTemplateReference.from_dict(obj.get("progressInvoice")) if obj.get("progressInvoice") is not None else None,
            "progressTimeFlag": obj.get("progressTimeFlag"),
            "quoteFooter": obj.get("quoteFooter"),
            "readReceiptFlag": obj.get("readReceiptFlag"),
            "remitName": obj.get("remitName"),
            "restrictDownpaymentFlag": obj.get("restrictDownpaymentFlag"),
            "restrictProjectDownpaymentFlag": obj.get("restrictProjectDownpaymentFlag"),
            "salesOrderInvoice": InvoiceTemplateReference.from_dict(obj.get("salesOrderInvoice")) if obj.get("salesOrderInvoice") is not None else None,
            "standardInvoiceActual": InvoiceTemplateReference.from_dict(obj.get("standardInvoiceActual")) if obj.get("standardInvoiceActual") is not None else None,
            "standardInvoiceFixed": InvoiceTemplateReference.from_dict(obj.get("standardInvoiceFixed")) if obj.get("standardInvoiceFixed") is not None else None,
            "state": StateReference.from_dict(obj.get("state")) if obj.get("state") is not None else None,
            "topcomment": obj.get("topcomment"),
            "zip": obj.get("zip")
        })
        return _obj


