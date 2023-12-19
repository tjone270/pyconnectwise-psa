# ExpenseReportAudit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**message** | **str** |  | [optional] 
**new_value** | **str** |  | [optional] 
**old_value** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.expense_report_audit import ExpenseReportAudit

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseReportAudit from a JSON string
expense_report_audit_instance = ExpenseReportAudit.from_json(json)
# print the JSON string representation of the object
print ExpenseReportAudit.to_json()

# convert the object into a dict
expense_report_audit_dict = expense_report_audit_instance.to_dict()
# create an instance of ExpenseReportAudit from a dict
expense_report_audit_form_dict = expense_report_audit.from_dict(expense_report_audit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


