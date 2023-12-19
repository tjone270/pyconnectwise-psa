# TimeEntryEmailViewModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**append_discussion** | **bool** |  | [optional] 
**append_internal** | **bool** |  | [optional] 
**append_resolution** | **bool** |  | [optional] 
**cc_email_address_list** | **str** |  | [optional] 
**contact** | **str** |  | [optional] 
**contact_email_address** | **str** |  | [optional] 
**document_rec_id_list** | **List[int]** |  | [optional] 
**var_from** | **str** |  | [optional] 
**from_email_address** | **str** |  | [optional] 
**from_email_address_for_resources** | **str** |  | [optional] 
**from_for_resources** | **str** |  | [optional] 
**is_to_ccs** | **bool** |  | [optional] 
**is_to_contact** | **bool** |  | [optional] 
**is_to_resources** | **bool** |  | [optional] 
**member_rec_id** | **int** |  | [optional] 
**no_time_entry** | **bool** |  | [optional] 
**note** | **str** |  | [optional] 
**resource_email_address_list** | **str** |  | [optional] 
**resources** | **str** |  | [optional] 
**save_cc_list** | **bool** |  | [optional] 
**schedule_date** | **datetime** |  | [optional] 
**schedule_done** | **bool** |  | [optional] 
**sr_detail_rec_id** | **int** |  | [optional] 
**sr_service_rec_id** | **int** |  | [optional] 
**sr_service_status_rec_id** | **int** |  | [optional] 
**time_rec_id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.time_entry_email_view_model import TimeEntryEmailViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of TimeEntryEmailViewModel from a JSON string
time_entry_email_view_model_instance = TimeEntryEmailViewModel.from_json(json)
# print the JSON string representation of the object
print TimeEntryEmailViewModel.to_json()

# convert the object into a dict
time_entry_email_view_model_dict = time_entry_email_view_model_instance.to_dict()
# create an instance of TimeEntryEmailViewModel from a dict
time_entry_email_view_model_form_dict = time_entry_email_view_model.from_dict(time_entry_email_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


