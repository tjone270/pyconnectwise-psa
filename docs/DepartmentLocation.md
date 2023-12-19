# DepartmentLocation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**add_all_locations** | **bool** |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**department_manager** | [**MemberReference**](MemberReference.md) |  | [optional] 
**dispatch** | [**MemberReference**](MemberReference.md) |  | [optional] 
**duty_manager** | [**MemberReference**](MemberReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**ldap_config** | [**LdapConfigurationReference**](LdapConfigurationReference.md) |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**remove_all_locations** | **bool** |  | [optional] 
**service_manager** | [**MemberReference**](MemberReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.department_location import DepartmentLocation

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentLocation from a JSON string
department_location_instance = DepartmentLocation.from_json(json)
# print the JSON string representation of the object
print DepartmentLocation.to_json()

# convert the object into a dict
department_location_dict = department_location_instance.to_dict()
# create an instance of DepartmentLocation from a dict
department_location_form_dict = department_location.from_dict(department_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


