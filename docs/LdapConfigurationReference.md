# LdapConfigurationReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**server** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.ldap_configuration_reference import LdapConfigurationReference

# TODO update the JSON string below
json = "{}"
# create an instance of LdapConfigurationReference from a JSON string
ldap_configuration_reference_instance = LdapConfigurationReference.from_json(json)
# print the JSON string representation of the object
print LdapConfigurationReference.to_json()

# convert the object into a dict
ldap_configuration_reference_dict = ldap_configuration_reference_instance.to_dict()
# create an instance of LdapConfigurationReference from a dict
ldap_configuration_reference_form_dict = ldap_configuration_reference.from_dict(ldap_configuration_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


