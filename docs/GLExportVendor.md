# GLExportVendor


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**billing_terms** | [**BillingTermsReference**](BillingTermsReference.md) |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**due_days** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**tax_code** | [**TaxCodeReference**](TaxCodeReference.md) |  | [optional] 
**vendor** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**vendor_number** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.gl_export_vendor import GLExportVendor

# TODO update the JSON string below
json = "{}"
# create an instance of GLExportVendor from a JSON string
gl_export_vendor_instance = GLExportVendor.from_json(json)
# print the JSON string representation of the object
print GLExportVendor.to_json()

# convert the object into a dict
gl_export_vendor_dict = gl_export_vendor_instance.to_dict()
# create an instance of GLExportVendor from a dict
gl_export_vendor_form_dict = gl_export_vendor.from_dict(gl_export_vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


