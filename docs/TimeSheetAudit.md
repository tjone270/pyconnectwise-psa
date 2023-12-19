# TimeSheetAudit


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
from connectwise_psa.models.time_sheet_audit import TimeSheetAudit

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSheetAudit from a JSON string
time_sheet_audit_instance = TimeSheetAudit.from_json(json)
# print the JSON string representation of the object
print TimeSheetAudit.to_json()

# convert the object into a dict
time_sheet_audit_dict = time_sheet_audit_instance.to_dict()
# create an instance of TimeSheetAudit from a dict
time_sheet_audit_form_dict = time_sheet_audit.from_dict(time_sheet_audit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


