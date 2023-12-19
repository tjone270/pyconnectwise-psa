# M365ContactSyncInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.m365_contact_sync_info import M365ContactSyncInfo

# TODO update the JSON string below
json = "{}"
# create an instance of M365ContactSyncInfo from a JSON string
m365_contact_sync_info_instance = M365ContactSyncInfo.from_json(json)
# print the JSON string representation of the object
print M365ContactSyncInfo.to_json()

# convert the object into a dict
m365_contact_sync_info_dict = m365_contact_sync_info_instance.to_dict()
# create an instance of M365ContactSyncInfo from a dict
m365_contact_sync_info_form_dict = m365_contact_sync_info.from_dict(m365_contact_sync_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


