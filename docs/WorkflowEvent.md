# WorkflowEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**event_condition** | **str** |  | 
**execution_time** | **str** | Defaults to Once when not specified | [optional] 
**frequency_of_execution** | **int** | Required when exectionTimes is set to MultipleTimes or Continuously | [optional] 
**frequency_unit** | **str** | Required when exectionTimes is set to MultipleTimes or Continuously | [optional] 
**id** | **int** |  | [optional] 
**max_number_of_execution** | **int** | Required when exectionTimes is set to MultipleTimes | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.workflow_event import WorkflowEvent

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowEvent from a JSON string
workflow_event_instance = WorkflowEvent.from_json(json)
# print the JSON string representation of the object
print WorkflowEvent.to_json()

# convert the object into a dict
workflow_event_dict = workflow_event_instance.to_dict()
# create an instance of WorkflowEvent from a dict
workflow_event_form_dict = workflow_event.from_dict(workflow_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


