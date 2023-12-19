# ManagedDevicesIntegrationNotification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**log_type** | **str** |  | 
**managed_devices_integration** | [**ManagedDevicesIntegrationReference**](ManagedDevicesIntegrationReference.md) |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**notify_who** | [**NotificationRecipientReference**](NotificationRecipientReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.managed_devices_integration_notification import ManagedDevicesIntegrationNotification

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedDevicesIntegrationNotification from a JSON string
managed_devices_integration_notification_instance = ManagedDevicesIntegrationNotification.from_json(json)
# print the JSON string representation of the object
print ManagedDevicesIntegrationNotification.to_json()

# convert the object into a dict
managed_devices_integration_notification_dict = managed_devices_integration_notification_instance.to_dict()
# create an instance of ManagedDevicesIntegrationNotification from a dict
managed_devices_integration_notification_form_dict = managed_devices_integration_notification.from_dict(managed_devices_integration_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


