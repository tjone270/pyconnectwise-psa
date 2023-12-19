# WorkflowTriggerOption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**custom_field** | [**UserDefinedFieldReference**](UserDefinedFieldReference.md) |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.workflow_trigger_option import WorkflowTriggerOption

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTriggerOption from a JSON string
workflow_trigger_option_instance = WorkflowTriggerOption.from_json(json)
# print the JSON string representation of the object
print WorkflowTriggerOption.to_json()

# convert the object into a dict
workflow_trigger_option_dict = workflow_trigger_option_instance.to_dict()
# create an instance of WorkflowTriggerOption from a dict
workflow_trigger_option_form_dict = workflow_trigger_option.from_dict(workflow_trigger_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


