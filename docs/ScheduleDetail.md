# ScheduleDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**date_end** | **str** |  | [optional] 
**date_start** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**schedule_entry** | [**ScheduleEntryReference**](ScheduleEntryReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.schedule_detail import ScheduleDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleDetail from a JSON string
schedule_detail_instance = ScheduleDetail.from_json(json)
# print the JSON string representation of the object
print ScheduleDetail.to_json()

# convert the object into a dict
schedule_detail_dict = schedule_detail_instance.to_dict()
# create an instance of ScheduleDetail from a dict
schedule_detail_form_dict = schedule_detail.from_dict(schedule_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


