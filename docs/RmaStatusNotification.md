# RmaStatusNotification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**email** | **str** | RMA Status Notification sendEmail must be entered if the notify type is \&quot;Email Address\&quot;. Max length: 50; | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**notify_who** | [**NotificationRecipientReference**](NotificationRecipientReference.md) |  | [optional] 
**status** | [**RmaStatusReference**](RmaStatusReference.md) |  | [optional] 
**workflow_step** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.rma_status_notification import RmaStatusNotification

# TODO update the JSON string below
json = "{}"
# create an instance of RmaStatusNotification from a JSON string
rma_status_notification_instance = RmaStatusNotification.from_json(json)
# print the JSON string representation of the object
print RmaStatusNotification.to_json()

# convert the object into a dict
rma_status_notification_dict = rma_status_notification_instance.to_dict()
# create an instance of RmaStatusNotification from a dict
rma_status_notification_form_dict = rma_status_notification.from_dict(rma_status_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


