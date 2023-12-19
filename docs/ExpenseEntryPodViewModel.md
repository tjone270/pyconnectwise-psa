# ExpenseEntryPodViewModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expense_entry_pod_user_defined_field_values** | [**List[UserDefinedFieldValue]**](UserDefinedFieldValue.md) |  | [optional] 
**expense_entry_widget** | [**ExpenseEntryWidgetViewModel**](ExpenseEntryWidgetViewModel.md) |  | [optional] 
**expense_taxes** | [**List[ExpenseEntryTaxViewModel]**](ExpenseEntryTaxViewModel.md) |  | [optional] 
**mileage_calculator_vm** | [**MileageCalculatorViewModel**](MileageCalculatorViewModel.md) |  | [optional] 
**notes** | **str** |  | [optional] 
**show_expense_tax** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.expense_entry_pod_view_model import ExpenseEntryPodViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseEntryPodViewModel from a JSON string
expense_entry_pod_view_model_instance = ExpenseEntryPodViewModel.from_json(json)
# print the JSON string representation of the object
print ExpenseEntryPodViewModel.to_json()

# convert the object into a dict
expense_entry_pod_view_model_dict = expense_entry_pod_view_model_instance.to_dict()
# create an instance of ExpenseEntryPodViewModel from a dict
expense_entry_pod_view_model_form_dict = expense_entry_pod_view_model.from_dict(expense_entry_pod_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


