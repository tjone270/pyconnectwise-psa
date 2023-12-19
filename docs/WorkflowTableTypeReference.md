# WorkflowTableTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.workflow_table_type_reference import WorkflowTableTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTableTypeReference from a JSON string
workflow_table_type_reference_instance = WorkflowTableTypeReference.from_json(json)
# print the JSON string representation of the object
print WorkflowTableTypeReference.to_json()

# convert the object into a dict
workflow_table_type_reference_dict = workflow_table_type_reference_instance.to_dict()
# create an instance of WorkflowTableTypeReference from a dict
workflow_table_type_reference_form_dict = workflow_table_type_reference.from_dict(workflow_table_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


