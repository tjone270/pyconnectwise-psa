# CrmInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**account_manager_role** | [**TeamRoleReference**](TeamRoleReference.md) |  | [optional] 
**field10_caption** | **str** |  | [optional] 
**field1_caption** | **str** |  | [optional] 
**field2_caption** | **str** |  | [optional] 
**field3_caption** | **str** |  | [optional] 
**field4_caption** | **str** |  | [optional] 
**field5_caption** | **str** |  | [optional] 
**field6_caption** | **str** |  | [optional] 
**field7_caption** | **str** |  | [optional] 
**field8_caption** | **str** |  | [optional] 
**field9_caption** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**primary_rep_caption** | **str** |  | [optional] 
**sales_rep_role** | [**TeamRoleReference**](TeamRoleReference.md) |  | [optional] 
**secondary_rep_caption** | **str** |  | [optional] 
**technical_contact_role** | [**TeamRoleReference**](TeamRoleReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.crm_info import CrmInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CrmInfo from a JSON string
crm_info_instance = CrmInfo.from_json(json)
# print the JSON string representation of the object
print CrmInfo.to_json()

# convert the object into a dict
crm_info_dict = crm_info_instance.to_dict()
# create an instance of CrmInfo from a dict
crm_info_form_dict = crm_info.from_dict(crm_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


