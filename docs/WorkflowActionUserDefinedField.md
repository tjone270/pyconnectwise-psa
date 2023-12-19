# WorkflowActionUserDefinedField


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**action_id** | **int** |  | [optional] 
**caption** | **str** |  | [optional] 
**entry_type_id** | **str** |  | [optional] 
**event_id** | **int** |  | [optional] 
**field_type_id** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**overwrite_flag** | **bool** |  | [optional] 
**pod_description** | **str** |  | [optional] 
**required_flag** | **bool** |  | [optional] 
**user_defined_field_id** | **int** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.workflow_action_user_defined_field import WorkflowActionUserDefinedField

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowActionUserDefinedField from a JSON string
workflow_action_user_defined_field_instance = WorkflowActionUserDefinedField.from_json(json)
# print the JSON string representation of the object
print WorkflowActionUserDefinedField.to_json()

# convert the object into a dict
workflow_action_user_defined_field_dict = workflow_action_user_defined_field_instance.to_dict()
# create an instance of WorkflowActionUserDefinedField from a dict
workflow_action_user_defined_field_form_dict = workflow_action_user_defined_field.from_dict(workflow_action_user_defined_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


