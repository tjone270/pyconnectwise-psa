# GLExportTransactionDetailTaxLevel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_level** | **int** |  | [optional] 
**taxable_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.gl_export_transaction_detail_tax_level import GLExportTransactionDetailTaxLevel

# TODO update the JSON string below
json = "{}"
# create an instance of GLExportTransactionDetailTaxLevel from a JSON string
gl_export_transaction_detail_tax_level_instance = GLExportTransactionDetailTaxLevel.from_json(json)
# print the JSON string representation of the object
print GLExportTransactionDetailTaxLevel.to_json()

# convert the object into a dict
gl_export_transaction_detail_tax_level_dict = gl_export_transaction_detail_tax_level_instance.to_dict()
# create an instance of GLExportTransactionDetailTaxLevel from a dict
gl_export_transaction_detail_tax_level_form_dict = gl_export_transaction_detail_tax_level.from_dict(gl_export_transaction_detail_tax_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


