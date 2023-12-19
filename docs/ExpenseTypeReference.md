# ExpenseTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.expense_type_reference import ExpenseTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseTypeReference from a JSON string
expense_type_reference_instance = ExpenseTypeReference.from_json(json)
# print the JSON string representation of the object
print ExpenseTypeReference.to_json()

# convert the object into a dict
expense_type_reference_dict = expense_type_reference_instance.to_dict()
# create an instance of ExpenseTypeReference from a dict
expense_type_reference_form_dict = expense_type_reference.from_dict(expense_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


