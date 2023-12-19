# PurchaseOrderStatusNotification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**email** | **str** | Purchase Order Status Notification email must be entered if the notify type is \&quot;Email Address\&quot;. Max length: 50; | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**notify_who** | [**NotificationRecipientReference**](NotificationRecipientReference.md) |  | [optional] 
**status** | [**PurchaseOrderStatusReference**](PurchaseOrderStatusReference.md) |  | [optional] 
**workflow_step** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.purchase_order_status_notification import PurchaseOrderStatusNotification

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderStatusNotification from a JSON string
purchase_order_status_notification_instance = PurchaseOrderStatusNotification.from_json(json)
# print the JSON string representation of the object
print PurchaseOrderStatusNotification.to_json()

# convert the object into a dict
purchase_order_status_notification_dict = purchase_order_status_notification_instance.to_dict()
# create an instance of PurchaseOrderStatusNotification from a dict
purchase_order_status_notification_form_dict = purchase_order_status_notification.from_dict(purchase_order_status_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


