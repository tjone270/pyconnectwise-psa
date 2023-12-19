# MemberLinkSsoUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sso_user_id** | **str** |  Max length: 100; | [optional] 

## Example

```python
from connectwise_psa.models.member_link_sso_user import MemberLinkSsoUser

# TODO update the JSON string below
json = "{}"
# create an instance of MemberLinkSsoUser from a JSON string
member_link_sso_user_instance = MemberLinkSsoUser.from_json(json)
# print the JSON string representation of the object
print MemberLinkSsoUser.to_json()

# convert the object into a dict
member_link_sso_user_dict = member_link_sso_user_instance.to_dict()
# create an instance of MemberLinkSsoUser from a dict
member_link_sso_user_form_dict = member_link_sso_user.from_dict(member_link_sso_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


