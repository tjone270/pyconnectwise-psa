# M365ContactSyncMonitoringNotificationInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_rec_id** | **int** |  | [optional] 
**company_name** | **str** |  | [optional] 
**company_rec_id** | **int** |  | [optional] 
**primary_contact_full_name** | **str** |  | [optional] 
**primary_contact_rec_id** | **int** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**tenant_name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.m365_contact_sync_monitoring_notification_info import M365ContactSyncMonitoringNotificationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of M365ContactSyncMonitoringNotificationInfo from a JSON string
m365_contact_sync_monitoring_notification_info_instance = M365ContactSyncMonitoringNotificationInfo.from_json(json)
# print the JSON string representation of the object
print M365ContactSyncMonitoringNotificationInfo.to_json()

# convert the object into a dict
m365_contact_sync_monitoring_notification_info_dict = m365_contact_sync_monitoring_notification_info_instance.to_dict()
# create an instance of M365ContactSyncMonitoringNotificationInfo from a dict
m365_contact_sync_monitoring_notification_info_form_dict = m365_contact_sync_monitoring_notification_info.from_dict(m365_contact_sync_monitoring_notification_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


