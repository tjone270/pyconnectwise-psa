# WorkflowTrigger


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**custom_field** | [**UserDefinedFieldReference**](UserDefinedFieldReference.md) |  | [optional] 
**description** | **str** |  | [optional] 
**expected_type** | **str** |  | [optional] 
**has_operator_flag** | **bool** |  | [optional] 
**has_options_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.workflow_trigger import WorkflowTrigger

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTrigger from a JSON string
workflow_trigger_instance = WorkflowTrigger.from_json(json)
# print the JSON string representation of the object
print WorkflowTrigger.to_json()

# convert the object into a dict
workflow_trigger_dict = workflow_trigger_instance.to_dict()
# create an instance of WorkflowTrigger from a dict
workflow_trigger_form_dict = workflow_trigger.from_dict(workflow_trigger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


