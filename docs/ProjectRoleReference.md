# ProjectRoleReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.project_role_reference import ProjectRoleReference

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectRoleReference from a JSON string
project_role_reference_instance = ProjectRoleReference.from_json(json)
# print the JSON string representation of the object
print ProjectRoleReference.to_json()

# convert the object into a dict
project_role_reference_dict = project_role_reference_instance.to_dict()
# create an instance of ProjectRoleReference from a dict
project_role_reference_form_dict = project_role_reference.from_dict(project_role_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


