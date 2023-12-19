# TimeExpense


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_special_invoice_type** | **str** |  | [optional] 
**disable_time_entry_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**internal_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**invoice_start** | **int** |  | [optional] 
**require_expense_note_flag** | **bool** |  | [optional] 
**require_time_note_flag** | **bool** |  | [optional] 
**rounding_factor** | **float** |  | [optional] 
**tier1_approval_flag** | **bool** |  | [optional] 
**tier2_approval_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.time_expense import TimeExpense

# TODO update the JSON string below
json = "{}"
# create an instance of TimeExpense from a JSON string
time_expense_instance = TimeExpense.from_json(json)
# print the JSON string representation of the object
print TimeExpense.to_json()

# convert the object into a dict
time_expense_dict = time_expense_instance.to_dict()
# create an instance of TimeExpense from a dict
time_expense_form_dict = time_expense.from_dict(time_expense_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


