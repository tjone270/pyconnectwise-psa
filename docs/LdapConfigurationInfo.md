# LdapConfigurationInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.ldap_configuration_info import LdapConfigurationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LdapConfigurationInfo from a JSON string
ldap_configuration_info_instance = LdapConfigurationInfo.from_json(json)
# print the JSON string representation of the object
print LdapConfigurationInfo.to_json()

# convert the object into a dict
ldap_configuration_info_dict = ldap_configuration_info_instance.to_dict()
# create an instance of LdapConfigurationInfo from a dict
ldap_configuration_info_form_dict = ldap_configuration_info.from_dict(ldap_configuration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


