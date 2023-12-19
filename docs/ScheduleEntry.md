# ScheduleEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**acknowledged_date** | **datetime** |  | [optional] 
**acknowledged_flag** | **bool** |  | [optional] 
**add_member_to_project_flag** | **bool** |  | [optional] 
**allow_schedule_conflicts_flag** | **bool** |  | [optional] 
**close_date** | **datetime** |  | [optional] 
**date_end** | **datetime** |  | [optional] 
**date_start** | **datetime** |  | [optional] 
**done_flag** | **bool** |  | [optional] 
**hours** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**meeting_flag** | **bool** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**mobile_guid** | **str** |  | [optional] 
**name** | **str** |  Max length: 250; | [optional] 
**object_id** | **int** |  | [optional] 
**owner_flag** | **bool** |  | [optional] 
**project_role_id** | **int** |  | [optional] 
**reminder** | [**ReminderReference**](ReminderReference.md) |  | [optional] 
**span** | [**ScheduleSpanReference**](ScheduleSpanReference.md) |  | [optional] 
**status** | [**ScheduleStatusReference**](ScheduleStatusReference.md) |  | [optional] 
**type** | [**ScheduleTypeReference**](ScheduleTypeReference.md) |  | [optional] 
**where** | [**ServiceLocationReference**](ServiceLocationReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.schedule_entry import ScheduleEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleEntry from a JSON string
schedule_entry_instance = ScheduleEntry.from_json(json)
# print the JSON string representation of the object
print ScheduleEntry.to_json()

# convert the object into a dict
schedule_entry_dict = schedule_entry_instance.to_dict()
# create an instance of ScheduleEntry from a dict
schedule_entry_form_dict = schedule_entry.from_dict(schedule_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


