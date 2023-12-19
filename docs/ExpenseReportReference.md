# ExpenseReportReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.expense_report_reference import ExpenseReportReference

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseReportReference from a JSON string
expense_report_reference_instance = ExpenseReportReference.from_json(json)
# print the JSON string representation of the object
print ExpenseReportReference.to_json()

# convert the object into a dict
expense_report_reference_dict = expense_report_reference_instance.to_dict()
# create an instance of ExpenseReportReference from a dict
expense_report_reference_form_dict = expense_report_reference.from_dict(expense_report_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


