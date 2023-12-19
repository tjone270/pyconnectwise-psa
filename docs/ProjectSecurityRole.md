# ProjectSecurityRole


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_contact_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**manager_role_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 30; | 

## Example

```python
from connectwise_psa.models.project_security_role import ProjectSecurityRole

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSecurityRole from a JSON string
project_security_role_instance = ProjectSecurityRole.from_json(json)
# print the JSON string representation of the object
print ProjectSecurityRole.to_json()

# convert the object into a dict
project_security_role_dict = project_security_role_instance.to_dict()
# create an instance of ProjectSecurityRole from a dict
project_security_role_form_dict = project_security_role.from_dict(project_security_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


