# M365ContactSyncCompany


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**are_all_microsoft365_contact_sync_inactive** | **bool** |  | [optional] 
**company_id** | **str** |  | [optional] 
**company_rec_id** | **int** |  | [optional] 
**contacts** | [**List[GraphUserCsv]**](GraphUserCsv.md) |  | [optional] 
**display_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag_tenant** | **bool** |  | [optional] 
**m365_tenant** | [**M365Tenant**](M365Tenant.md) |  | [optional] 
**parent_tenant_id** | **str** |  | [optional] 
**sync_flag** | **bool** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.m365_contact_sync_company import M365ContactSyncCompany

# TODO update the JSON string below
json = "{}"
# create an instance of M365ContactSyncCompany from a JSON string
m365_contact_sync_company_instance = M365ContactSyncCompany.from_json(json)
# print the JSON string representation of the object
print M365ContactSyncCompany.to_json()

# convert the object into a dict
m365_contact_sync_company_dict = m365_contact_sync_company_instance.to_dict()
# create an instance of M365ContactSyncCompany from a dict
m365_contact_sync_company_form_dict = m365_contact_sync_company.from_dict(m365_contact_sync_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


