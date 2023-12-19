# BoardNotification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**email** | **str** |  Max length: 50; | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**notify_who** | [**NotificationRecipientReference**](NotificationRecipientReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.board_notification import BoardNotification

# TODO update the JSON string below
json = "{}"
# create an instance of BoardNotification from a JSON string
board_notification_instance = BoardNotification.from_json(json)
# print the JSON string representation of the object
print BoardNotification.to_json()

# convert the object into a dict
board_notification_dict = board_notification_instance.to_dict()
# create an instance of BoardNotification from a dict
board_notification_form_dict = board_notification.from_dict(board_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


