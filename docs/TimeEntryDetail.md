# TimeEntryDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**activity_rec_id** | **int** |  | [optional] 
**board_rec_id** | **int** |  | [optional] 
**charge_code_rec_id** | **int** |  | [optional] 
**company_rec_id** | **int** |  | [optional] 
**default_date** | **str** |  | [optional] 
**end_time** | **str** |  | [optional] 
**flag_type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**lab_start_time** | **str** |  | [optional] 
**lab_start_time_active** | **bool** |  | [optional] 
**schedule_rec_id** | **int** |  | [optional] 
**selected_member_id** | **str** |  | [optional] 
**service_rec_id** | **int** |  | [optional] 
**start_time** | **str** |  | [optional] 
**stop_watch_rec_id** | **int** |  | [optional] 
**task_rec_id** | **int** |  | [optional] 
**time_entry_view_model** | [**TimeEntryDetailViewModel**](TimeEntryDetailViewModel.md) |  | [optional] 
**time_sheet_rec_id** | **int** |  | [optional] 
**time_zone_display** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.time_entry_detail import TimeEntryDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TimeEntryDetail from a JSON string
time_entry_detail_instance = TimeEntryDetail.from_json(json)
# print the JSON string representation of the object
print TimeEntryDetail.to_json()

# convert the object into a dict
time_entry_detail_dict = time_entry_detail_instance.to_dict()
# create an instance of TimeEntryDetail from a dict
time_entry_detail_form_dict = time_entry_detail.from_dict(time_entry_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


