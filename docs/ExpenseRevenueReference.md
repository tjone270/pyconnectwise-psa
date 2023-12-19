# ExpenseRevenueReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**cost** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**margin** | **float** |  | [optional] 
**percentage** | **float** |  | [optional] 
**revenue** | **float** |  | [optional] 

## Example

```python
from connectwise_psa.models.expense_revenue_reference import ExpenseRevenueReference

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseRevenueReference from a JSON string
expense_revenue_reference_instance = ExpenseRevenueReference.from_json(json)
# print the JSON string representation of the object
print ExpenseRevenueReference.to_json()

# convert the object into a dict
expense_revenue_reference_dict = expense_revenue_reference_instance.to_dict()
# create an instance of ExpenseRevenueReference from a dict
expense_revenue_reference_form_dict = expense_revenue_reference.from_dict(expense_revenue_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


