# WorkflowActionAutomateParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**value** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.workflow_action_automate_parameter import WorkflowActionAutomateParameter

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowActionAutomateParameter from a JSON string
workflow_action_automate_parameter_instance = WorkflowActionAutomateParameter.from_json(json)
# print the JSON string representation of the object
print WorkflowActionAutomateParameter.to_json()

# convert the object into a dict
workflow_action_automate_parameter_dict = workflow_action_automate_parameter_instance.to_dict()
# create an instance of WorkflowActionAutomateParameter from a dict
workflow_action_automate_parameter_form_dict = workflow_action_automate_parameter.from_dict(workflow_action_automate_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


