# WorkflowNotifyTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**is_setup_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.workflow_notify_type_info import WorkflowNotifyTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowNotifyTypeInfo from a JSON string
workflow_notify_type_info_instance = WorkflowNotifyTypeInfo.from_json(json)
# print the JSON string representation of the object
print WorkflowNotifyTypeInfo.to_json()

# convert the object into a dict
workflow_notify_type_info_dict = workflow_notify_type_info_instance.to_dict()
# create an instance of WorkflowNotifyTypeInfo from a dict
workflow_notify_type_info_form_dict = workflow_notify_type_info.from_dict(workflow_notify_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


