# CompanySite


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**address_format** | **str** |  | [optional] 
**address_line1** | **str** |  Max length: 50; | [optional] 
**address_line2** | **str** |  Max length: 50; | [optional] 
**bill_separate_flag** | **bool** |  | [optional] 
**calendar** | [**CalendarReference**](CalendarReference.md) |  | [optional] 
**city** | **str** |  Max length: 50; | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**country** | [**CountryReference**](CountryReference.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**default_billing_flag** | **bool** |  | [optional] 
**default_mailing_flag** | **bool** |  | [optional] 
**default_shipping_flag** | **bool** |  | [optional] 
**entity_type** | [**EntityTypeReference**](EntityTypeReference.md) |  | [optional] 
**expense_reimbursement** | **float** |  | [optional] 
**fax_number** | **str** |  Max length: 30; | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**mobile_guid** | **str** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**phone_number** | **str** |  Max length: 30; | [optional] 
**phone_number_ext** | **str** |  Max length: 30; | [optional] 
**primary_address_flag** | **bool** |  | [optional] 
**state_reference** | [**StateReference**](StateReference.md) |  | [optional] 
**tax_code** | [**TaxCodeReference**](TaxCodeReference.md) |  | [optional] 
**time_zone** | [**TimeZoneSetupReference**](TimeZoneSetupReference.md) |  | [optional] 
**zip** | **str** |  Max length: 12; | [optional] 

## Example

```python
from connectwise_psa.models.company_site import CompanySite

# TODO update the JSON string below
json = "{}"
# create an instance of CompanySite from a JSON string
company_site_instance = CompanySite.from_json(json)
# print the JSON string representation of the object
print CompanySite.to_json()

# convert the object into a dict
company_site_dict = company_site_instance.to_dict()
# create an instance of CompanySite from a dict
company_site_form_dict = company_site.from_dict(company_site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


