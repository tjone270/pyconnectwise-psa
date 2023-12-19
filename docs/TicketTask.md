# TicketTask


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
from connectwise_psa.models.ticket_task import TicketTask

# TODO update the JSON string below
json = "{}"
# create an instance of TicketTask from a JSON string
ticket_task_instance = TicketTask.from_json(json)
# print the JSON string representation of the object
print TicketTask.to_json()

# convert the object into a dict
ticket_task_dict = ticket_task_instance.to_dict()
# create an instance of TicketTask from a dict
ticket_task_form_dict = ticket_task.from_dict(ticket_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


