# GLExportCustomer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**billing_terms** | [**BillingTermsReference**](BillingTermsReference.md) |  | [optional] 
**billing_terms_xref** | **str** |  | [optional] 
**city_tax_agency_xref** | **str** |  | [optional] 
**city_tax_rate** | **float** |  | [optional] 
**city_tax_xref** | **str** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**company_type** | [**CompanyTypeReference**](CompanyTypeReference.md) |  | [optional] 
**composite_tax_agency_xref** | **str** |  | [optional] 
**composite_tax_rate** | **float** |  | [optional] 
**composite_tax_xref** | **str** |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**country_tax_agency_xref** | **str** |  | [optional] 
**country_tax_rate** | **float** |  | [optional] 
**country_tax_xref** | **str** |  | [optional] 
**county_tax_agency_xref** | **str** |  | [optional] 
**county_tax_rate** | **float** |  | [optional] 
**county_tax_xref** | **str** |  | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**due_days** | **int** |  | [optional] 
**site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**state_tax_agency_xref** | **str** |  | [optional] 
**state_tax_rate** | **float** |  | [optional] 
**state_tax_xref** | **str** |  | [optional] 
**tax_agency_xref** | **str** |  | [optional] 
**tax_code** | [**TaxCodeReference**](TaxCodeReference.md) |  | [optional] 
**tax_group_rate** | **float** |  | [optional] 
**tax_levels** | [**List[GLExportCustomerTaxLevel]**](GLExportCustomerTaxLevel.md) |  | [optional] 
**taxable** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.gl_export_customer import GLExportCustomer

# TODO update the JSON string below
json = "{}"
# create an instance of GLExportCustomer from a JSON string
gl_export_customer_instance = GLExportCustomer.from_json(json)
# print the JSON string representation of the object
print GLExportCustomer.to_json()

# convert the object into a dict
gl_export_customer_dict = gl_export_customer_instance.to_dict()
# create an instance of GLExportCustomer from a dict
gl_export_customer_form_dict = gl_export_customer.from_dict(gl_export_customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


