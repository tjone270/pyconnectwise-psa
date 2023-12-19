# UnpostedInvoice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**account_number** | **str** |  | [optional] 
**avalara_tax_flag** | **bool** | Used to determine if Avalara tax is enabled. | [optional] 
**bill_to_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**bill_to_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**billing_log_id** | **int** |  | [optional] 
**billing_terms** | [**BillingTermsReference**](BillingTermsReference.md) |  | [optional] 
**city_tax_amount** | **float** |  | [optional] 
**city_tax_flag** | **bool** | Set to true if transaction is taxable at the city level. | [optional] 
**city_tax_xref** | **str** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**composite_tax_amount** | **float** |  | [optional] 
**composite_tax_flag** | **bool** | Set to true if transaction is taxable at the composite level. | [optional] 
**composite_tax_xref** | **str** |  | [optional] 
**country_tax_amount** | **float** |  | [optional] 
**country_tax_flag** | **bool** | Set to true if transaction is taxable at the country level. | [optional] 
**country_tax_xref** | **str** |  | [optional] 
**county_tax_amount** | **float** |  | [optional] 
**county_tax_flag** | **bool** | Set to true if transaction is taxable at the county level. | [optional] 
**county_tax_xref** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**date_closed** | **str** |  | [optional] 
**department_id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**due_days** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**invoice_date** | **str** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**invoice_taxable_flag** | **bool** |  | [optional] 
**invoice_type** | **str** |  | [optional] 
**item_taxable_flag** | **bool** |  | [optional] 
**level_six_tax_amount** | **float** |  | [optional] 
**level_six_tax_flag** | **bool** | Set to true if transaction is taxable at level six. | [optional] 
**level_six_tax_xref** | **str** |  | [optional] 
**location_id** | **int** |  | [optional] 
**sales_tax_amount** | **float** |  | [optional] 
**ship_to_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**ship_to_site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**state_tax_amount** | **float** |  | [optional] 
**state_tax_flag** | **bool** | Set to true if transaction is taxable at the state level. | [optional] 
**state_tax_xref** | **str** |  | [optional] 
**sub_total** | **float** |  | [optional] 
**tax_code** | [**TaxCodeReference**](TaxCodeReference.md) |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from connectwise_psa.models.unposted_invoice import UnpostedInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of UnpostedInvoice from a JSON string
unposted_invoice_instance = UnpostedInvoice.from_json(json)
# print the JSON string representation of the object
print UnpostedInvoice.to_json()

# convert the object into a dict
unposted_invoice_dict = unposted_invoice_instance.to_dict()
# create an instance of UnpostedInvoice from a dict
unposted_invoice_form_dict = unposted_invoice.from_dict(unposted_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


