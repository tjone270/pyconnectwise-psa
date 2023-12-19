# ScheduleEntryDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**date_end** | **str** |  | [optional] 
**date_start** | **str** |  | [optional] 
**hours_scheduled** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**schedule_entry** | [**ScheduleEntryReference**](ScheduleEntryReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.schedule_entry_detail import ScheduleEntryDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleEntryDetail from a JSON string
schedule_entry_detail_instance = ScheduleEntryDetail.from_json(json)
# print the JSON string representation of the object
print ScheduleEntryDetail.to_json()

# convert the object into a dict
schedule_entry_detail_dict = schedule_entry_detail_instance.to_dict()
# create an instance of ScheduleEntryDetail from a dict
schedule_entry_detail_form_dict = schedule_entry_detail.from_dict(schedule_entry_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


