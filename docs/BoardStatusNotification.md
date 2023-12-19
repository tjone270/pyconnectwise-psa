# BoardStatusNotification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**email** | **str** | Service Status Notification email must be entered if the notify type is \&quot;Email Address\&quot;. Max length: 255; | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**notify_who** | [**NotificationRecipientReference**](NotificationRecipientReference.md) |  | [optional] 
**status** | [**ServiceStatusReference**](ServiceStatusReference.md) |  | [optional] 
**workflow_step** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.board_status_notification import BoardStatusNotification

# TODO update the JSON string below
json = "{}"
# create an instance of BoardStatusNotification from a JSON string
board_status_notification_instance = BoardStatusNotification.from_json(json)
# print the JSON string representation of the object
print BoardStatusNotification.to_json()

# convert the object into a dict
board_status_notification_dict = board_status_notification_instance.to_dict()
# create an instance of BoardStatusNotification from a dict
board_status_notification_form_dict = board_status_notification.from_dict(board_status_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


