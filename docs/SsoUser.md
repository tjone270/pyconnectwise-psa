# SsoUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_entered** | **str** |  | [optional] 
**disabled_flag** | **bool** |  | [optional] 
**email** | **str** |  | [optional] 
**email_confirmed** | **bool** |  | [optional] 
**first_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**last_name** | **str** |  | [optional] 
**last_updated** | **str** |  | [optional] 
**linked_flag** | **bool** |  | [optional] 
**linked_member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**sso_user_id** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.sso_user import SsoUser

# TODO update the JSON string below
json = "{}"
# create an instance of SsoUser from a JSON string
sso_user_instance = SsoUser.from_json(json)
# print the JSON string representation of the object
print SsoUser.to_json()

# convert the object into a dict
sso_user_dict = sso_user_instance.to_dict()
# create an instance of SsoUser from a dict
sso_user_form_dict = sso_user.from_dict(sso_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


