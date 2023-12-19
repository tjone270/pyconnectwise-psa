# Other


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**contact_sync** | **str** |  | [optional] 
**default_address_format** | [**AddressFormatReference**](AddressFormatReference.md) |  | [optional] 
**default_calendar** | [**CalendarReference**](CalendarReference.md) |  | [optional] 
**default_from_address** | **str** |  Max length: 50; | 
**default_ldap** | [**LdapConfigurationReference**](LdapConfigurationReference.md) |  | [optional] 
**disable_z_admin_login_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**include_portal_link_flag** | **bool** |  | [optional] 
**locale** | [**LocaleReference**](LocaleReference.md) |  | [optional] 
**logo_path** | **str** |  Max length: 200; | [optional] 
**portal_url_override** | **str** |  Max length: 100; | 
**server_time_zone** | [**TimeZoneSetupReference**](TimeZoneSetupReference.md) |  | [optional] 
**site_url** | **str** |  Max length: 100; | 
**sync_leads_flag** | **bool** |  | [optional] 
**update_member_time_zones_flag** | **bool** | If true, all Members time zone will also be set to serverTimeZone. Otherwise, only My Company time zone will be updated. | [optional] 
**use_expanded_format_activity_flag** | **bool** |  | [optional] 
**use_expanded_format_time_flag** | **bool** |  | [optional] 
**use_ssl_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.other import Other

# TODO update the JSON string below
json = "{}"
# create an instance of Other from a JSON string
other_instance = Other.from_json(json)
# print the JSON string representation of the object
print Other.to_json()

# convert the object into a dict
other_dict = other_instance.to_dict()
# create an instance of Other from a dict
other_form_dict = other.from_dict(other_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


