# SecurityRole


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**admin_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 30; | 
**role_type** | **str** |  Max length: 30; | [optional] 

## Example

```python
from connectwise_psa.models.security_role import SecurityRole

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityRole from a JSON string
security_role_instance = SecurityRole.from_json(json)
# print the JSON string representation of the object
print SecurityRole.to_json()

# convert the object into a dict
security_role_dict = security_role_instance.to_dict()
# create an instance of SecurityRole from a dict
security_role_form_dict = security_role.from_dict(security_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


