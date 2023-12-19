# GLExportTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**agreement_pre_payment_flag** | **bool** |  | [optional] 
**attention** | **str** |  | [optional] 
**billing_terms** | [**BillingTermsReference**](BillingTermsReference.md) |  | [optional] 
**billing_terms_xref** | **str** |  | [optional] 
**billing_type** | **str** |  | [optional] 
**city_tax** | **float** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**company_account_number** | **str** |  | [optional] 
**company_type** | [**CompanyTypeReference**](CompanyTypeReference.md) |  | [optional] 
**county_tax** | **float** |  | [optional] 
**county_tax_xref** | **str** |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**description** | **str** |  | [optional] 
**detail** | [**List[GLExportTransactionDetail]**](GLExportTransactionDetail.md) |  | [optional] 
**document_date** | **str** |  | [optional] 
**document_number** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**due_days** | **int** |  | [optional] 
**email_delivery_flag** | **bool** |  | [optional] 
**gl_class** | **str** |  | [optional] 
**gl_entry_ids** | **str** |  | [optional] 
**gl_type_id** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**memo** | **str** |  | [optional] 
**piggy_back_flag** | **bool** |  | [optional] 
**print_delivery_flag** | **bool** |  | [optional] 
**project** | [**ProjectReference**](ProjectReference.md) |  | [optional] 
**purchase_order** | [**PurchaseOrderReference**](PurchaseOrderReference.md) |  | [optional] 
**sales_rep_id** | **str** |  | [optional] 
**sales_rep_name** | **str** |  | [optional] 
**sales_tax** | **float** |  | [optional] 
**sales_territory** | **str** |  | [optional] 
**send_avalara_tax_flag** | **bool** |  | [optional] 
**ship_contact** | **str** |  | [optional] 
**ship_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**ship_to_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**ship_to_company_account_number** | **str** |  | [optional] 
**ship_to_company_type** | [**CompanyTypeReference**](CompanyTypeReference.md) |  | [optional] 
**ship_to_tax_id** | **str** |  | [optional] 
**site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**state_tax** | **float** |  | [optional] 
**state_tax_xref** | **str** |  | [optional] 
**tax_account_number** | **str** |  | [optional] 
**tax_agency_xref** | **str** |  | [optional] 
**tax_code** | [**TaxCodeReference**](TaxCodeReference.md) |  | [optional] 
**tax_dp_applied_flag** | **bool** |  | [optional] 
**tax_group_rate** | **float** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**tax_levels** | [**List[GLExportTransactionTaxLevel]**](GLExportTransactionTaxLevel.md) |  | [optional] 
**taxable** | **bool** |  | [optional] 
**taxable_amount1** | **float** |  | [optional] 
**taxable_amount2** | **float** |  | [optional] 
**taxable_amount3** | **float** |  | [optional] 
**taxable_amount4** | **float** |  | [optional] 
**taxable_amount5** | **float** |  | [optional] 
**taxable_total** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**use_avalara_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.gl_export_transaction import GLExportTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of GLExportTransaction from a JSON string
gl_export_transaction_instance = GLExportTransaction.from_json(json)
# print the JSON string representation of the object
print GLExportTransaction.to_json()

# convert the object into a dict
gl_export_transaction_dict = gl_export_transaction_instance.to_dict()
# create an instance of GLExportTransaction from a dict
gl_export_transaction_form_dict = gl_export_transaction.from_dict(gl_export_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


