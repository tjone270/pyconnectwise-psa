# ExpenseReportTierUpdate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.expense_report_tier_update import ExpenseReportTierUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseReportTierUpdate from a JSON string
expense_report_tier_update_instance = ExpenseReportTierUpdate.from_json(json)
# print the JSON string representation of the object
print ExpenseReportTierUpdate.to_json()

# convert the object into a dict
expense_report_tier_update_dict = expense_report_tier_update_instance.to_dict()
# create an instance of ExpenseReportTierUpdate from a dict
expense_report_tier_update_form_dict = expense_report_tier_update.from_dict(expense_report_tier_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


