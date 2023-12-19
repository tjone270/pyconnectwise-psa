# ProjectTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 200; | 
**type** | [**ProjectTypeReference**](ProjectTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.project_template import ProjectTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplate from a JSON string
project_template_instance = ProjectTemplate.from_json(json)
# print the JSON string representation of the object
print ProjectTemplate.to_json()

# convert the object into a dict
project_template_dict = project_template_instance.to_dict()
# create an instance of ProjectTemplate from a dict
project_template_form_dict = project_template.from_dict(project_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


