# MemberSsoSettingsReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**email** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**sso_user_id** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.member_sso_settings_reference import MemberSsoSettingsReference

# TODO update the JSON string below
json = "{}"
# create an instance of MemberSsoSettingsReference from a JSON string
member_sso_settings_reference_instance = MemberSsoSettingsReference.from_json(json)
# print the JSON string representation of the object
print MemberSsoSettingsReference.to_json()

# convert the object into a dict
member_sso_settings_reference_dict = member_sso_settings_reference_instance.to_dict()
# create an instance of MemberSsoSettingsReference from a dict
member_sso_settings_reference_form_dict = member_sso_settings_reference.from_dict(member_sso_settings_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


