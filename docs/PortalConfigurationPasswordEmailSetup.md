# PortalConfigurationPasswordEmailSetup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**invalid_password_email_body** | **str** |  | [optional] 
**invalid_password_email_from_email** | **str** | Gets or sets             required when invalidPasswordEmailUseCustomEmailFlag is true. | [optional] 
**invalid_password_email_from_first_name** | **str** |  | [optional] 
**invalid_password_email_from_last_name** | **str** |  | [optional] 
**invalid_password_email_subject** | **str** |  | [optional] 
**invalid_password_email_use_custom_email_flag** | **bool** |  | [optional] 
**valid_password_email_body** | **str** |  | [optional] 
**valid_password_email_from_email** | **str** | Gets or sets             required when validPasswordEmailUseCustomEmailFlag is true. | [optional] 
**valid_password_email_from_first_name** | **str** |  | [optional] 
**valid_password_email_from_last_name** | **str** |  | [optional] 
**valid_password_email_subject** | **str** |  | [optional] 
**valid_password_email_use_custom_email_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.portal_configuration_password_email_setup import PortalConfigurationPasswordEmailSetup

# TODO update the JSON string below
json = "{}"
# create an instance of PortalConfigurationPasswordEmailSetup from a JSON string
portal_configuration_password_email_setup_instance = PortalConfigurationPasswordEmailSetup.from_json(json)
# print the JSON string representation of the object
print PortalConfigurationPasswordEmailSetup.to_json()

# convert the object into a dict
portal_configuration_password_email_setup_dict = portal_configuration_password_email_setup_instance.to_dict()
# create an instance of PortalConfigurationPasswordEmailSetup from a dict
portal_configuration_password_email_setup_form_dict = portal_configuration_password_email_setup.from_dict(portal_configuration_password_email_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


