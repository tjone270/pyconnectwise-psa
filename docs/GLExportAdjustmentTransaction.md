# GLExportAdjustmentTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**adjustment_description** | **str** |  | [optional] 
**adjustment_detail** | [**List[GLExportAdjustmentTransactionDetail]**](GLExportAdjustmentTransactionDetail.md) |  | [optional] 
**document_date** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 
**gl_class** | **str** |  | [optional] 
**gl_type_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**memo** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.gl_export_adjustment_transaction import GLExportAdjustmentTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of GLExportAdjustmentTransaction from a JSON string
gl_export_adjustment_transaction_instance = GLExportAdjustmentTransaction.from_json(json)
# print the JSON string representation of the object
print GLExportAdjustmentTransaction.to_json()

# convert the object into a dict
gl_export_adjustment_transaction_dict = gl_export_adjustment_transaction_instance.to_dict()
# create an instance of GLExportAdjustmentTransaction from a dict
gl_export_adjustment_transaction_form_dict = gl_export_adjustment_transaction.from_dict(gl_export_adjustment_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


