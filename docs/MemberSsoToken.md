# MemberSsoToken


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.member_sso_token import MemberSsoToken

# TODO update the JSON string below
json = "{}"
# create an instance of MemberSsoToken from a JSON string
member_sso_token_instance = MemberSsoToken.from_json(json)
# print the JSON string representation of the object
print MemberSsoToken.to_json()

# convert the object into a dict
member_sso_token_dict = member_sso_token_instance.to_dict()
# create an instance of MemberSsoToken from a dict
member_sso_token_form_dict = member_sso_token.from_dict(member_sso_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


