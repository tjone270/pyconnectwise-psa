# MemberNotificationSetting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**notification_trigger** | **str** |  | 
**notification_type** | **str** |  | 

## Example

```python
from connectwise_psa.models.member_notification_setting import MemberNotificationSetting

# TODO update the JSON string below
json = "{}"
# create an instance of MemberNotificationSetting from a JSON string
member_notification_setting_instance = MemberNotificationSetting.from_json(json)
# print the JSON string representation of the object
print MemberNotificationSetting.to_json()

# convert the object into a dict
member_notification_setting_dict = member_notification_setting_instance.to_dict()
# create an instance of MemberNotificationSetting from a dict
member_notification_setting_form_dict = member_notification_setting.from_dict(member_notification_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


