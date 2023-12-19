# PortalSecuritySetting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**function_description** | **str** |  | [optional] 
**function_identifier** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**level_five** | **bool** |  | [optional] 
**level_four** | **bool** |  | [optional] 
**level_one** | **bool** |  | [optional] 
**level_six** | **bool** |  | [optional] 
**level_three** | **bool** |  | [optional] 
**level_two** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.portal_security_setting import PortalSecuritySetting

# TODO update the JSON string below
json = "{}"
# create an instance of PortalSecuritySetting from a JSON string
portal_security_setting_instance = PortalSecuritySetting.from_json(json)
# print the JSON string representation of the object
print PortalSecuritySetting.to_json()

# convert the object into a dict
portal_security_setting_dict = portal_security_setting_instance.to_dict()
# create an instance of PortalSecuritySetting from a dict
portal_security_setting_form_dict = portal_security_setting.from_dict(portal_security_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


