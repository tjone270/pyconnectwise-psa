# ScheduleEntryReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.schedule_entry_reference import ScheduleEntryReference

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleEntryReference from a JSON string
schedule_entry_reference_instance = ScheduleEntryReference.from_json(json)
# print the JSON string representation of the object
print ScheduleEntryReference.to_json()

# convert the object into a dict
schedule_entry_reference_dict = schedule_entry_reference_instance.to_dict()
# create an instance of ScheduleEntryReference from a dict
schedule_entry_reference_form_dict = schedule_entry_reference.from_dict(schedule_entry_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


