# M365ContactSync


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**authorized_flag** | **bool** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**company_contacts_folder** | **str** |  | [optional] 
**credential_file** | **str** |  | [optional] 
**credential_file_name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**password** | **str** |  | [optional] 
**primary_domain** | **str** |  | [optional] 
**server_url** | **str** |  | [optional] 
**service_account_email** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.m365_contact_sync import M365ContactSync

# TODO update the JSON string below
json = "{}"
# create an instance of M365ContactSync from a JSON string
m365_contact_sync_instance = M365ContactSync.from_json(json)
# print the JSON string representation of the object
print M365ContactSync.to_json()

# convert the object into a dict
m365_contact_sync_dict = m365_contact_sync_instance.to_dict()
# create an instance of M365ContactSync from a dict
m365_contact_sync_form_dict = m365_contact_sync.from_dict(m365_contact_sync_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


