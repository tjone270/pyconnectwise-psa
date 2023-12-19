# WorkflowTableTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.workflow_table_type_info import WorkflowTableTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowTableTypeInfo from a JSON string
workflow_table_type_info_instance = WorkflowTableTypeInfo.from_json(json)
# print the JSON string representation of the object
print WorkflowTableTypeInfo.to_json()

# convert the object into a dict
workflow_table_type_info_dict = workflow_table_type_info_instance.to_dict()
# create an instance of WorkflowTableTypeInfo from a dict
workflow_table_type_info_form_dict = workflow_table_type_info.from_dict(workflow_table_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


