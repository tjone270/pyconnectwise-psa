# ProjectTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.project_type_info import ProjectTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTypeInfo from a JSON string
project_type_info_instance = ProjectTypeInfo.from_json(json)
# print the JSON string representation of the object
print ProjectTypeInfo.to_json()

# convert the object into a dict
project_type_info_dict = project_type_info_instance.to_dict()
# create an instance of ProjectTypeInfo from a dict
project_type_info_form_dict = project_type_info.from_dict(project_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


