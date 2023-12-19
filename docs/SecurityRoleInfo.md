# SecurityRoleInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**role_type** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.security_role_info import SecurityRoleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityRoleInfo from a JSON string
security_role_info_instance = SecurityRoleInfo.from_json(json)
# print the JSON string representation of the object
print SecurityRoleInfo.to_json()

# convert the object into a dict
security_role_info_dict = security_role_info_instance.to_dict()
# create an instance of SecurityRoleInfo from a dict
security_role_info_form_dict = security_role_info.from_dict(security_role_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


