# ExpenseReport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**date_end** | **str** |  | [optional] 
**date_start** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**period** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**total** | **float** |  | [optional] 
**year** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.expense_report import ExpenseReport

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseReport from a JSON string
expense_report_instance = ExpenseReport.from_json(json)
# print the JSON string representation of the object
print ExpenseReport.to_json()

# convert the object into a dict
expense_report_dict = expense_report_instance.to_dict()
# create an instance of ExpenseReport from a dict
expense_report_form_dict = expense_report.from_dict(expense_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


