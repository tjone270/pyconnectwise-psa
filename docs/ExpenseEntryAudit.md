# ExpenseEntryAudit


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
from connectwise_psa.models.expense_entry_audit import ExpenseEntryAudit

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseEntryAudit from a JSON string
expense_entry_audit_instance = ExpenseEntryAudit.from_json(json)
# print the JSON string representation of the object
print ExpenseEntryAudit.to_json()

# convert the object into a dict
expense_entry_audit_dict = expense_entry_audit_instance.to_dict()
# create an instance of ExpenseEntryAudit from a dict
expense_entry_audit_form_dict = expense_entry_audit.from_dict(expense_entry_audit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


