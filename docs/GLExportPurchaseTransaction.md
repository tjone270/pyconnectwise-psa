# GLExportPurchaseTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ap_account_number** | **str** |  | [optional] 
**billing_terms** | [**BillingTermsReference**](BillingTermsReference.md) |  | [optional] 
**billing_terms_xref** | **str** |  | [optional] 
**city_tax_xref** | **str** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**company_type** | [**CompanyTypeReference**](CompanyTypeReference.md) |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**county_tax_xref** | **str** |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**description** | **str** |  | [optional] 
**document_date** | **str** |  | [optional] 
**document_number** | **str** |  | [optional] 
**dropship_flag** | **bool** |  | [optional] 
**due_days** | **int** |  | [optional] 
**freight_amount** | **float** |  | [optional] 
**freight_packing_slip** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**memo** | **str** |  | [optional] 
**packing_slip** | **str** |  | [optional] 
**purchase_class** | **str** |  | [optional] 
**purchase_date** | **str** |  | [optional] 
**purchase_detail** | [**List[GLExportPurchaseTransactionDetail]**](GLExportPurchaseTransactionDetail.md) |  | [optional] 
**purchase_detail_tax** | [**List[GLExportPurchaseTransactionDetailTax]**](GLExportPurchaseTransactionDetailTax.md) |  | [optional] 
**purchase_header_freight_taxable_flag** | **bool** |  | [optional] 
**purchase_header_tax_group** | **str** |  | [optional] 
**purchase_header_taxable_flag** | **bool** |  | [optional] 
**ship_to_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**ship_to_company_account_number** | **str** |  | [optional] 
**ship_to_company_type** | [**CompanyTypeReference**](CompanyTypeReference.md) |  | [optional] 
**ship_to_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**ship_to_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**ship_to_tax_group** | **str** |  | [optional] 
**site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**state_tax_xref** | **str** |  | [optional] 
**tax_agency_xref** | **str** |  | [optional] 
**tax_code** | [**TaxCodeReference**](TaxCodeReference.md) |  | [optional] 
**tax_group_rate** | **float** |  | [optional] 
**tax_levels** | [**List[GLExportPurchaseTransactionTaxLevel]**](GLExportPurchaseTransactionTaxLevel.md) |  | [optional] 
**total** | **float** |  | [optional] 
**use_avalara_tax_flag** | **bool** |  | [optional] 
**vendor_account_number** | **str** |  | [optional] 
**vendor_invoice_date** | **str** |  | [optional] 
**vendor_invoice_number** | **str** |  | [optional] 
**vendor_number** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.gl_export_purchase_transaction import GLExportPurchaseTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of GLExportPurchaseTransaction from a JSON string
gl_export_purchase_transaction_instance = GLExportPurchaseTransaction.from_json(json)
# print the JSON string representation of the object
print GLExportPurchaseTransaction.to_json()

# convert the object into a dict
gl_export_purchase_transaction_dict = gl_export_purchase_transaction_instance.to_dict()
# create an instance of GLExportPurchaseTransaction from a dict
gl_export_purchase_transaction_form_dict = gl_export_purchase_transaction.from_dict(gl_export_purchase_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


