# GLExportExpenseOffset


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**document_date** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 
**gl_class** | **str** |  | [optional] 
**gl_type_id** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**memo** | **str** |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from connectwise_psa.models.gl_export_expense_offset import GLExportExpenseOffset

# TODO update the JSON string below
json = "{}"
# create an instance of GLExportExpenseOffset from a JSON string
gl_export_expense_offset_instance = GLExportExpenseOffset.from_json(json)
# print the JSON string representation of the object
print GLExportExpenseOffset.to_json()

# convert the object into a dict
gl_export_expense_offset_dict = gl_export_expense_offset_instance.to_dict()
# create an instance of GLExportExpenseOffset from a dict
gl_export_expense_offset_form_dict = gl_export_expense_offset.from_dict(gl_export_expense_offset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


