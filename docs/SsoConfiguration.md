# SsoConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**all_members_submitted** | **bool** |  | [optional] 
**client_id** | **str** | Client identity for this configuration of ConnectWise SSO Max length: 1000; | [optional] 
**id** | **int** | Unique identifier of the SSO Configuration | [optional] 
**inactive_flag** | **bool** | Whether the SSO configuration is not active | [optional] 
**is_sso_on_by_default** | **bool** |  | [optional] 
**location_ids** | **List[int]** | The locations where the SAML Idp Configuration is used | 
**name** | **str** | Descriptor of the SSO Configuration Max length: 100; | 
**saml_certificate_issued_to** | **str** | Who the SAML certificate was issued to. Metadata on SAML_Idp_Certificate | [optional] 
**saml_certificate_name** | **str** | Name of the SAML certificate. Metadata on SAML_Idp_Certificate | [optional] 
**saml_certificate_thumbprint** | **str** | Thumbprint of the SAML certificate. Metadata on SAML_Idp_Certificate | [optional] 
**saml_certificate_valid_from** | **datetime** | Date when the SAML certificate becomes valid. Metadata on SAML_Idp_Certificate | [optional] 
**saml_certificate_valid_to** | **datetime** | Date when the SAML certificate is no longer valid. Metadata on SAML_Idp_Certificate | [optional] 
**saml_entity_id** | **str** | SAML Identity Provider Id Max length: 1000; | [optional] 
**saml_idp_certificate** | **str** | Public certificate for Identity Provider signatures | [optional] 
**saml_sign_in_url** | **str** | Sign in url for the SAML Identity Provider Max length: 1000; | [optional] 
**sso_type** | **str** | Type of SSO Configuration | 
**sts_base_url** | **str** | Sign in URL for ConnectWise SSO | [optional] 
**sts_user_admin_url** | **str** | User Admin Url for ConnectWise SSO | [optional] 
**submitted_member_count** | **int** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.sso_configuration import SsoConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of SsoConfiguration from a JSON string
sso_configuration_instance = SsoConfiguration.from_json(json)
# print the JSON string representation of the object
print SsoConfiguration.to_json()

# convert the object into a dict
sso_configuration_dict = sso_configuration_instance.to_dict()
# create an instance of SsoConfiguration from a dict
sso_configuration_form_dict = sso_configuration.from_dict(sso_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


