# AuditTrailEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audit_source** | **str** |  | [optional] 
**audit_sub_type** | **str** |  | [optional] 
**audit_type** | **str** |  | [optional] 
**entered_by** | **str** |  | [optional] 
**entered_date** | **str** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.audit_trail_entry import AuditTrailEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AuditTrailEntry from a JSON string
audit_trail_entry_instance = AuditTrailEntry.from_json(json)
# print the JSON string representation of the object
print AuditTrailEntry.to_json()

# convert the object into a dict
audit_trail_entry_dict = audit_trail_entry_instance.to_dict()
# create an instance of AuditTrailEntry from a dict
audit_trail_entry_form_dict = audit_trail_entry.from_dict(audit_trail_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


