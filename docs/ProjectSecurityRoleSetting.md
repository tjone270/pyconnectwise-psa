# ProjectSecurityRoleSetting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**add_level** | **str** |  | [optional] 
**delete_level** | **str** |  | [optional] 
**edit_level** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**inquire_level** | **str** |  | [optional] 
**module_identifier** | **str** |  Max length: 50; | [optional] 
**my_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.project_security_role_setting import ProjectSecurityRoleSetting

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSecurityRoleSetting from a JSON string
project_security_role_setting_instance = ProjectSecurityRoleSetting.from_json(json)
# print the JSON string representation of the object
print ProjectSecurityRoleSetting.to_json()

# convert the object into a dict
project_security_role_setting_dict = project_security_role_setting_instance.to_dict()
# create an instance of ProjectSecurityRoleSetting from a dict
project_security_role_setting_form_dict = project_security_role_setting.from_dict(project_security_role_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


