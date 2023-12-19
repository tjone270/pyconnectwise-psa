# BillingSetup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**address_one** | **str** |  Max length: 50; | [optional] 
**address_two** | **str** |  Max length: 50; | [optional] 
**agreement_invoice** | [**InvoiceTemplateReference**](InvoiceTemplateReference.md) |  | [optional] 
**allow_restricted_dept_on_routing_flag** | **bool** |  | [optional] 
**attach_xml_invoice_flag** | **bool** |  | [optional] 
**bill_product_after_ship_flag** | **bool** |  | [optional] 
**bill_project_complete_flag** | **bool** |  | [optional] 
**bill_project_unapproved_flag** | **bool** |  | [optional] 
**bill_sales_order_complete_flag** | **bool** |  | [optional] 
**bill_ticket_complete_flag** | **bool** |  | [optional] 
**bill_ticket_separately_flag** | **bool** |  | [optional] 
**bill_ticket_unapproved_flag** | **bool** |  | [optional] 
**business_number** | **str** |  Max length: 50; | [optional] 
**charge_adj_to_firm_flag** | **bool** |  | [optional] 
**city** | **str** |  Max length: 50; | [optional] 
**company_code** | **str** |  Max length: 250; | [optional] 
**copy_agreement_products_flag** | **bool** |  | [optional] 
**copy_non_service_products_flag** | **bool** |  | [optional] 
**copy_service_products_flag** | **bool** |  | [optional] 
**country** | [**CountryReference**](CountryReference.md) |  | [optional] 
**credit_memo_invoice** | [**InvoiceTemplateReference**](InvoiceTemplateReference.md) |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**custom_label** | **str** |  Max length: 50; | [optional] 
**custom_text** | **str** |  Max length: 500; | [optional] 
**delivery_receipt_flag** | **bool** |  | [optional] 
**disable_routing_email_flag** | **bool** |  | [optional] 
**display_tax_flag** | **bool** |  | [optional] 
**down_payment_invoice** | [**InvoiceTemplateReference**](InvoiceTemplateReference.md) |  | [optional] 
**email_template** | [**EmailTemplateReference**](EmailTemplateReference.md) |  | 
**exclude_avalara_flag** | **bool** |  | [optional] 
**exclude_do_not_bill_expense_flag** | **bool** |  | [optional] 
**exclude_do_not_bill_product_flag** | **bool** |  | [optional] 
**exclude_do_not_bill_time_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**invoice_footer** | **str** |  Max length: 500; | [optional] 
**invoice_title** | **str** |  Max length: 50; | 
**localized_country** | [**CountryReference**](CountryReference.md) |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | 
**misc_invoice** | [**InvoiceTemplateReference**](InvoiceTemplateReference.md) |  | [optional] 
**no_watermark_flag** | **bool** |  | [optional] 
**overall_invoice_default** | [**InvoiceTemplateReference**](InvoiceTemplateReference.md) |  | [optional] 
**payable_name** | **str** |  Max length: 50; | 
**phone** | **str** |  Max length: 15; | [optional] 
**prefix_suffix_flag** | **str** |  | [optional] 
**prefix_suffix_text** | **str** |  Max length: 5; | [optional] 
**print_logo_flag** | **bool** |  | [optional] 
**progress_invoice** | [**InvoiceTemplateReference**](InvoiceTemplateReference.md) |  | [optional] 
**progress_time_flag** | **bool** |  | [optional] 
**quote_footer** | **str** |  Max length: 1000; | [optional] 
**read_receipt_flag** | **bool** |  | [optional] 
**remit_name** | **str** |  Max length: 50; | 
**restrict_downpayment_flag** | **bool** |  | [optional] 
**restrict_project_downpayment_flag** | **bool** |  | [optional] 
**sales_order_invoice** | [**InvoiceTemplateReference**](InvoiceTemplateReference.md) |  | [optional] 
**standard_invoice_actual** | [**InvoiceTemplateReference**](InvoiceTemplateReference.md) |  | [optional] 
**standard_invoice_fixed** | [**InvoiceTemplateReference**](InvoiceTemplateReference.md) |  | [optional] 
**state** | [**StateReference**](StateReference.md) |  | [optional] 
**topcomment** | **str** |  Max length: 4000; | [optional] 
**zip** | **str** |  Max length: 12; | [optional] 

## Example

```python
from connectwise_psa.models.billing_setup import BillingSetup

# TODO update the JSON string below
json = "{}"
# create an instance of BillingSetup from a JSON string
billing_setup_instance = BillingSetup.from_json(json)
# print the JSON string representation of the object
print BillingSetup.to_json()

# convert the object into a dict
billing_setup_dict = billing_setup_instance.to_dict()
# create an instance of BillingSetup from a dict
billing_setup_form_dict = billing_setup.from_dict(billing_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


