# HistoryEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | [optional] 
**history_type** | **str** |  | [optional] 
**member_id** | **str** |  | [optional] 
**member_name** | **str** |  | [optional] 
**time_zone_offset_display** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.history_entry import HistoryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryEntry from a JSON string
history_entry_instance = HistoryEntry.from_json(json)
# print the JSON string representation of the object
print HistoryEntry.to_json()

# convert the object into a dict
history_entry_dict = history_entry_instance.to_dict()
# create an instance of HistoryEntry from a dict
history_entry_form_dict = history_entry.from_dict(history_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


