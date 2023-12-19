# ProjectType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**integration_xref** | **str** |  Max length: 50; | [optional] 
**name** | **str** |  Max length: 30; | 

## Example

```python
from connectwise_psa.models.project_type import ProjectType

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectType from a JSON string
project_type_instance = ProjectType.from_json(json)
# print the JSON string representation of the object
print ProjectType.to_json()

# convert the object into a dict
project_type_dict = project_type_instance.to_dict()
# create an instance of ProjectType from a dict
project_type_form_dict = project_type.from_dict(project_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


