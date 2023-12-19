# MemberDeactivationSendFromEmailNotify


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**re_assign_to_member** | [**MemberReference**](MemberReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.member_deactivation_send_from_email_notify import MemberDeactivationSendFromEmailNotify

# TODO update the JSON string below
json = "{}"
# create an instance of MemberDeactivationSendFromEmailNotify from a JSON string
member_deactivation_send_from_email_notify_instance = MemberDeactivationSendFromEmailNotify.from_json(json)
# print the JSON string representation of the object
print MemberDeactivationSendFromEmailNotify.to_json()

# convert the object into a dict
member_deactivation_send_from_email_notify_dict = member_deactivation_send_from_email_notify_instance.to_dict()
# create an instance of MemberDeactivationSendFromEmailNotify from a dict
member_deactivation_send_from_email_notify_form_dict = member_deactivation_send_from_email_notify.from_dict(member_deactivation_send_from_email_notify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


