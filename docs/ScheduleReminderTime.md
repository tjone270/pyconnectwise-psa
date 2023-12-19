# ScheduleReminderTime


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 10; | [optional] 
**time** | **int** | Time is calculated in minutes. | [optional] 

## Example

```python
from connectwise_psa.models.schedule_reminder_time import ScheduleReminderTime

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleReminderTime from a JSON string
schedule_reminder_time_instance = ScheduleReminderTime.from_json(json)
# print the JSON string representation of the object
print ScheduleReminderTime.to_json()

# convert the object into a dict
schedule_reminder_time_dict = schedule_reminder_time_instance.to_dict()
# create an instance of ScheduleReminderTime from a dict
schedule_reminder_time_form_dict = schedule_reminder_time.from_dict(schedule_reminder_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


