# TimeEntryDetailsViewModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_end_time** | **datetime** |  | [optional] 
**activity_start_time** | **datetime** |  | [optional] 
**billable** | [**GenericNameIdDTO**](GenericNameIdDTO.md) |  | [optional] 
**deduct** | **float** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**hours** | **float** |  | [optional] 
**internal_notes** | **str** |  | [optional] 
**member_time_zone_offset** | **int** |  | [optional] 
**notes** | **str** |  | [optional] 
**notes_markdown** | **str** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**time_details_pod_user_defined_fields** | [**List[UserDefinedFieldValue]**](UserDefinedFieldValue.md) |  | [optional] 
**work_type** | [**GenericNameIdDTO**](GenericNameIdDTO.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.time_entry_details_view_model import TimeEntryDetailsViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of TimeEntryDetailsViewModel from a JSON string
time_entry_details_view_model_instance = TimeEntryDetailsViewModel.from_json(json)
# print the JSON string representation of the object
print TimeEntryDetailsViewModel.to_json()

# convert the object into a dict
time_entry_details_view_model_dict = time_entry_details_view_model_instance.to_dict()
# create an instance of TimeEntryDetailsViewModel from a dict
time_entry_details_view_model_form_dict = time_entry_details_view_model.from_dict(time_entry_details_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


