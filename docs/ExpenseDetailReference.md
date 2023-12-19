# ExpenseDetailReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**amount** | **float** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.expense_detail_reference import ExpenseDetailReference

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseDetailReference from a JSON string
expense_detail_reference_instance = ExpenseDetailReference.from_json(json)
# print the JSON string representation of the object
print ExpenseDetailReference.to_json()

# convert the object into a dict
expense_detail_reference_dict = expense_detail_reference_instance.to_dict()
# create an instance of ExpenseDetailReference from a dict
expense_detail_reference_form_dict = expense_detail_reference.from_dict(expense_detail_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


