# ProjectTemplateTask


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**code** | [**ServiceCodeReference**](ServiceCodeReference.md) |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**sequence** | **int** |  | [optional] 
**summary** | **str** |  | [optional] 
**ticket_id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.project_template_task import ProjectTemplateTask

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateTask from a JSON string
project_template_task_instance = ProjectTemplateTask.from_json(json)
# print the JSON string representation of the object
print ProjectTemplateTask.to_json()

# convert the object into a dict
project_template_task_dict = project_template_task_instance.to_dict()
# create an instance of ProjectTemplateTask from a dict
project_template_task_form_dict = project_template_task.from_dict(project_template_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


