# WorkflowNotifyType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**external_flag** | **bool** | If the current action effects external objects e.g. integrations or sending an email | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**is_setup_flag** | **bool** | If the current action is available because it is already set up. Pertains to integrations such as Automate | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.workflow_notify_type import WorkflowNotifyType

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowNotifyType from a JSON string
workflow_notify_type_instance = WorkflowNotifyType.from_json(json)
# print the JSON string representation of the object
print WorkflowNotifyType.to_json()

# convert the object into a dict
workflow_notify_type_dict = workflow_notify_type_instance.to_dict()
# create an instance of WorkflowNotifyType from a dict
workflow_notify_type_form_dict = workflow_notify_type.from_dict(workflow_notify_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


