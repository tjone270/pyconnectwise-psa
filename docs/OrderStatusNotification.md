# OrderStatusNotification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**email** | **str** | Order Status Notification sendEmail must be entered if the notify type is \&quot;Email Address\&quot;. Max length: 50; | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**notify_who** | [**NotificationRecipientReference**](NotificationRecipientReference.md) |  | [optional] 
**status** | [**OrderStatusReference**](OrderStatusReference.md) |  | [optional] 
**workflow_step** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.order_status_notification import OrderStatusNotification

# TODO update the JSON string below
json = "{}"
# create an instance of OrderStatusNotification from a JSON string
order_status_notification_instance = OrderStatusNotification.from_json(json)
# print the JSON string representation of the object
print OrderStatusNotification.to_json()

# convert the object into a dict
order_status_notification_dict = order_status_notification_instance.to_dict()
# create an instance of OrderStatusNotification from a dict
order_status_notification_form_dict = order_status_notification.from_dict(order_status_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


