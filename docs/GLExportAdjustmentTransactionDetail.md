# GLExportAdjustmentTransactionDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**cost** | **float** |  | [optional] 
**cost_account_number** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**gl_class** | **str** |  | [optional] 
**inventory_account_number** | **str** |  | [optional] 
**item** | [**IvItemReference**](IvItemReference.md) |  | [optional] 
**memo** | **str** |  | [optional] 
**product_account_number** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from connectwise_psa.models.gl_export_adjustment_transaction_detail import GLExportAdjustmentTransactionDetail

# TODO update the JSON string below
json = "{}"
# create an instance of GLExportAdjustmentTransactionDetail from a JSON string
gl_export_adjustment_transaction_detail_instance = GLExportAdjustmentTransactionDetail.from_json(json)
# print the JSON string representation of the object
print GLExportAdjustmentTransactionDetail.to_json()

# convert the object into a dict
gl_export_adjustment_transaction_detail_dict = gl_export_adjustment_transaction_detail_instance.to_dict()
# create an instance of GLExportAdjustmentTransactionDetail from a dict
gl_export_adjustment_transaction_detail_form_dict = gl_export_adjustment_transaction_detail.from_dict(gl_export_adjustment_transaction_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


