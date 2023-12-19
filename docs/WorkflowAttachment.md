# WorkflowAttachment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.workflow_attachment import WorkflowAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowAttachment from a JSON string
workflow_attachment_instance = WorkflowAttachment.from_json(json)
# print the JSON string representation of the object
print WorkflowAttachment.to_json()

# convert the object into a dict
workflow_attachment_dict = workflow_attachment_instance.to_dict()
# create an instance of WorkflowAttachment from a dict
workflow_attachment_form_dict = workflow_attachment.from_dict(workflow_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


