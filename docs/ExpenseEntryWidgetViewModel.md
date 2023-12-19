# ExpenseEntryWidgetViewModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**billable** | [**GenericNameIdDTO**](GenericNameIdDTO.md) |  | [optional] 
**class_type** | [**GenericNameIdDTO**](GenericNameIdDTO.md) |  | [optional] 
**default_billable** | [**GenericNameIdDTO**](GenericNameIdDTO.md) |  | [optional] 
**default_billable_rec_id** | **int** |  | [optional] 
**default_classification** | [**GenericNameIdDTO**](GenericNameIdDTO.md) |  | [optional] 
**default_payment_method** | [**GenericNameIdDTO**](GenericNameIdDTO.md) |  | [optional] 
**expense_type** | [**GenericNameIdDTO**](GenericNameIdDTO.md) |  | [optional] 
**payment_method** | [**GenericNameIdDTO**](GenericNameIdDTO.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.expense_entry_widget_view_model import ExpenseEntryWidgetViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseEntryWidgetViewModel from a JSON string
expense_entry_widget_view_model_instance = ExpenseEntryWidgetViewModel.from_json(json)
# print the JSON string representation of the object
print ExpenseEntryWidgetViewModel.to_json()

# convert the object into a dict
expense_entry_widget_view_model_dict = expense_entry_widget_view_model_instance.to_dict()
# create an instance of ExpenseEntryWidgetViewModel from a dict
expense_entry_widget_view_model_form_dict = expense_entry_widget_view_model.from_dict(expense_entry_widget_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


