# Invoice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**account_number** | **str** |  | [optional] 
**add_to_batch_email_list** | **bool** |  | [optional] 
**adjusted_by** | **str** |  | [optional] 
**adjustment_reason** | **str** |  | [optional] 
**agreement** | [**AgreementReference**](AgreementReference.md) |  | [optional] 
**agreement_amount** | **float** |  | [optional] 
**apply_to_id** | **int** |  | [optional] 
**apply_to_type** | **str** |  | [optional] 
**attention** | **str** |  Max length: 60; | [optional] 
**balance** | **float** |  | [optional] 
**bill_to_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**billing_setup_reference** | [**BillingSetupReference**](BillingSetupReference.md) |  | [optional] 
**billing_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**billing_site_address_line1** | **str** |  | [optional] 
**billing_site_address_line2** | **str** |  | [optional] 
**billing_site_city** | **str** |  | [optional] 
**billing_site_country** | **str** |  | [optional] 
**billing_site_state** | **str** |  | [optional] 
**billing_site_zip** | **str** |  | [optional] 
**billing_terms** | [**BillingTermsReference**](BillingTermsReference.md) |  | [optional] 
**bottom_comment** | **str** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**credits** | **float** |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**customer_po** | **str** |  Max length: 50; | [optional] 
**var_date** | **datetime** |  | [optional] 
**department_id** | **int** | departmentId is only required for special invoices. | [optional] 
**downpayment_applied** | **float** |  | [optional] 
**downpayment_previously_taxed_flag** | **bool** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**email_template_id** | **int** | Can be obtained via InvoiceEmailTemplate report. | [optional] 
**expense_total** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**internal_notes** | **str** |  | [optional] 
**invoice_number** | **str** |  Max length: 15; Required On Updates; | [optional] 
**invoice_template** | [**InvoiceTemplateDetailReference**](InvoiceTemplateDetailReference.md) |  | [optional] 
**location_id** | **int** |  Required On Updates; | [optional] 
**override_down_payment_amount_flag** | **bool** |  | [optional] 
**payments** | **float** |  | [optional] 
**phase** | [**ProjectPhaseReference**](ProjectPhaseReference.md) |  | [optional] 
**previous_progress_applied** | **float** |  | [optional] 
**product_total** | **float** |  | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**reference** | **str** |  Max length: 50; | [optional] 
**remaining_downpayment** | **float** |  | [optional] 
**restrict_downpayment_flag** | **bool** |  | [optional] 
**sales_order** | [**SalesOrderReference**](SalesOrderReference.md) |  | [optional] 
**sales_tax** | **float** |  | [optional] 
**service_adjustment_amount** | **float** |  | [optional] 
**service_total** | **float** |  | [optional] 
**ship_to_attention** | **str** |  Max length: 60; | [optional] 
**ship_to_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**shipping_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**shipping_site_address_line1** | **str** |  | [optional] 
**shipping_site_address_line2** | **str** |  | [optional] 
**shipping_site_city** | **str** |  | [optional] 
**shipping_site_country** | **str** |  | [optional] 
**shipping_site_state** | **str** |  | [optional] 
**shipping_site_zip** | **str** |  | [optional] 
**special_invoice_flag** | **bool** |  | [optional] 
**status** | [**BillingStatusReference**](BillingStatusReference.md) |  | [optional] 
**subtotal** | **float** |  | [optional] 
**tax_code** | [**TaxCodeReference**](TaxCodeReference.md) |  | [optional] 
**taxable_flag** | **bool** |  | [optional] 
**template_setup_id** | **int** | Can be obtained via InvoiceTemplate report. | [optional] 
**territory_id** | **int** |  | [optional] 
**ticket** | [**TicketReference**](TicketReference.md) |  | [optional] 
**top_comment** | **str** |  | [optional] 
**total** | **float** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from connectwise_psa.models.invoice import Invoice

# TODO update the JSON string below
json = "{}"
# create an instance of Invoice from a JSON string
invoice_instance = Invoice.from_json(json)
# print the JSON string representation of the object
print Invoice.to_json()

# convert the object into a dict
invoice_dict = invoice_instance.to_dict()
# create an instance of Invoice from a dict
invoice_form_dict = invoice.from_dict(invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


