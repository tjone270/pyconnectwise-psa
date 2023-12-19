# Task


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**child_schedule_action** | **str** |  | [optional] 
**child_ticket_id** | **int** |  | [optional] 
**closed_flag** | **bool** |  | [optional] 
**code** | [**ServiceCodeReference**](ServiceCodeReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**notes** | **str** |  | [optional] 
**priority** | **int** |  | [optional] 
**resolution** | **str** |  | [optional] 
**schedule** | [**ScheduleEntryReference**](ScheduleEntryReference.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**ticket_id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print Task.to_json()

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_form_dict = task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


