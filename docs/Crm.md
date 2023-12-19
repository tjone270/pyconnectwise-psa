# Crm


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**account_manager_role** | [**TeamRoleReference**](TeamRoleReference.md) |  | [optional] 
**company_id_generation_flag** | **bool** |  | [optional] 
**company_list_count** | **int** |  | [optional] 
**default_year** | **bool** |  | [optional] 
**exclude_spaces_flag** | **bool** |  | [optional] 
**field10_caption** | **str** |  Max length: 25; | [optional] 
**field1_caption** | **str** |  Max length: 25; | [optional] 
**field2_caption** | **str** |  Max length: 25; | [optional] 
**field3_caption** | **str** |  Max length: 25; | [optional] 
**field4_caption** | **str** |  Max length: 25; | [optional] 
**field5_caption** | **str** |  Max length: 25; | [optional] 
**field6_caption** | **str** |  Max length: 25; | [optional] 
**field7_caption** | **str** |  Max length: 25; | [optional] 
**field8_caption** | **str** |  Max length: 25; | [optional] 
**field9_caption** | **str** |  Max length: 25; | [optional] 
**id** | **int** |  | [optional] 
**lock_probability_flag** | **bool** |  | [optional] 
**other1_caption** | **str** |  Max length: 50; | [optional] 
**other2_caption** | **str** |  Max length: 50; | [optional] 
**primary_rep_caption** | **str** |  Max length: 50; | [optional] 
**sales_rep_role** | [**TeamRoleReference**](TeamRoleReference.md) |  | [optional] 
**secondary_rep_caption** | **str** |  Max length: 50; | [optional] 
**technical_contact_role** | [**TeamRoleReference**](TeamRoleReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.crm import Crm

# TODO update the JSON string below
json = "{}"
# create an instance of Crm from a JSON string
crm_instance = Crm.from_json(json)
# print the JSON string representation of the object
print Crm.to_json()

# convert the object into a dict
crm_dict = crm_instance.to_dict()
# create an instance of Crm from a dict
crm_form_dict = crm.from_dict(crm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


