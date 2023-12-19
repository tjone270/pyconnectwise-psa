# ExpenseTypeExemption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**expense_type** | [**ExpenseTypeReference**](ExpenseTypeReference.md) |  | 
**id** | **int** |  | [optional] 
**taxable_levels** | **List[int]** |  | [optional] 

## Example

```python
from connectwise_psa.models.expense_type_exemption import ExpenseTypeExemption

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseTypeExemption from a JSON string
expense_type_exemption_instance = ExpenseTypeExemption.from_json(json)
# print the JSON string representation of the object
print ExpenseTypeExemption.to_json()

# convert the object into a dict
expense_type_exemption_dict = expense_type_exemption_instance.to_dict()
# create an instance of ExpenseTypeExemption from a dict
expense_type_exemption_form_dict = expense_type_exemption.from_dict(expense_type_exemption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


