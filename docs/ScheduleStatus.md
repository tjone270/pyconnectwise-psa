# ScheduleStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 30; | 
**show_as_tentative_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.schedule_status import ScheduleStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleStatus from a JSON string
schedule_status_instance = ScheduleStatus.from_json(json)
# print the JSON string representation of the object
print ScheduleStatus.to_json()

# convert the object into a dict
schedule_status_dict = schedule_status_instance.to_dict()
# create an instance of ScheduleStatus from a dict
schedule_status_form_dict = schedule_status.from_dict(schedule_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


