# ExpenseTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**amount_caption** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**mileage_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.expense_type_info import ExpenseTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseTypeInfo from a JSON string
expense_type_info_instance = ExpenseTypeInfo.from_json(json)
# print the JSON string representation of the object
print ExpenseTypeInfo.to_json()

# convert the object into a dict
expense_type_info_dict = expense_type_info_instance.to_dict()
# create an instance of ExpenseTypeInfo from a dict
expense_type_info_form_dict = expense_type_info.from_dict(expense_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


