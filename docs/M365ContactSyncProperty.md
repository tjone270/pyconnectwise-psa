# M365ContactSyncProperty


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**company_rec_id** | **int** |  | [optional] 
**exclude_include_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**include_exclude_type** | **str** |  | [optional] 
**property_type** | **str** |  | [optional] 
**wild_card** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.m365_contact_sync_property import M365ContactSyncProperty

# TODO update the JSON string below
json = "{}"
# create an instance of M365ContactSyncProperty from a JSON string
m365_contact_sync_property_instance = M365ContactSyncProperty.from_json(json)
# print the JSON string representation of the object
print M365ContactSyncProperty.to_json()

# convert the object into a dict
m365_contact_sync_property_dict = m365_contact_sync_property_instance.to_dict()
# create an instance of M365ContactSyncProperty from a dict
m365_contact_sync_property_form_dict = m365_contact_sync_property.from_dict(m365_contact_sync_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


