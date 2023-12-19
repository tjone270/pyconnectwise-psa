# SecurityRoleReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.security_role_reference import SecurityRoleReference

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityRoleReference from a JSON string
security_role_reference_instance = SecurityRoleReference.from_json(json)
# print the JSON string representation of the object
print SecurityRoleReference.to_json()

# convert the object into a dict
security_role_reference_dict = security_role_reference_instance.to_dict()
# create an instance of SecurityRoleReference from a dict
security_role_reference_form_dict = security_role_reference.from_dict(security_role_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


