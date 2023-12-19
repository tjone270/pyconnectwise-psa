# LdapConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**domain** | **str** | Domain Name of the server. Max length: 50; | 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 100; | 
**server** | **str** | FQDN of the Server. Max length: 200; | 

## Example

```python
from connectwise_psa.models.ldap_configuration import LdapConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of LdapConfiguration from a JSON string
ldap_configuration_instance = LdapConfiguration.from_json(json)
# print the JSON string representation of the object
print LdapConfiguration.to_json()

# convert the object into a dict
ldap_configuration_dict = ldap_configuration_instance.to_dict()
# create an instance of LdapConfiguration from a dict
ldap_configuration_form_dict = ldap_configuration.from_dict(ldap_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


