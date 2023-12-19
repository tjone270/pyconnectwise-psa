# GLExportCustomerTaxLevel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agency_xref** | **str** |  | [optional] 
**tax_code_xref** | **str** |  | [optional] 
**tax_level** | **int** |  | [optional] 
**tax_rate** | **float** |  | [optional] 

## Example

```python
from connectwise_psa.models.gl_export_customer_tax_level import GLExportCustomerTaxLevel

# TODO update the JSON string below
json = "{}"
# create an instance of GLExportCustomerTaxLevel from a JSON string
gl_export_customer_tax_level_instance = GLExportCustomerTaxLevel.from_json(json)
# print the JSON string representation of the object
print GLExportCustomerTaxLevel.to_json()

# convert the object into a dict
gl_export_customer_tax_level_dict = gl_export_customer_tax_level_instance.to_dict()
# create an instance of GLExportCustomerTaxLevel from a dict
gl_export_customer_tax_level_form_dict = gl_export_customer_tax_level.from_dict(gl_export_customer_tax_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


