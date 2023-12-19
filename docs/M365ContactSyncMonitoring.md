# M365ContactSyncMonitoring


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**email_address** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**monitoring_type_id** | **int** |  | [optional] 
**service_board_id** | **int** |  | [optional] 
**service_board_status_id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.m365_contact_sync_monitoring import M365ContactSyncMonitoring

# TODO update the JSON string below
json = "{}"
# create an instance of M365ContactSyncMonitoring from a JSON string
m365_contact_sync_monitoring_instance = M365ContactSyncMonitoring.from_json(json)
# print the JSON string representation of the object
print M365ContactSyncMonitoring.to_json()

# convert the object into a dict
m365_contact_sync_monitoring_dict = m365_contact_sync_monitoring_instance.to_dict()
# create an instance of M365ContactSyncMonitoring from a dict
m365_contact_sync_monitoring_form_dict = m365_contact_sync_monitoring.from_dict(m365_contact_sync_monitoring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


