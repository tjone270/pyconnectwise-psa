# TimeEntryDetailViewModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_expenses** | [**List[ExpenseEntryPodViewModel]**](ExpenseEntryPodViewModel.md) |  | [optional] 
**audit_reason** | **str** |  | [optional] 
**billing_log_rec_id** | **int** |  | [optional] 
**billing_model** | [**TimeEntryBillingOptionsViewModel**](TimeEntryBillingOptionsViewModel.md) |  | [optional] 
**charge_to** | [**TimeEntryChargeToSelection**](TimeEntryChargeToSelection.md) |  | [optional] 
**client_time** | **str** |  | [optional] 
**current_user_is_manager** | **bool** |  | [optional] 
**email_model** | [**TimeEntryEmailViewModel**](TimeEntryEmailViewModel.md) |  | [optional] 
**exp_billable_defaulting_source** | **str** |  | [optional] 
**expense** | [**ExpenseEntryPodViewModel**](ExpenseEntryPodViewModel.md) |  | [optional] 
**history** | [**List[HistoryEntry]**](HistoryEntry.md) |  | [optional] 
**invoice_closed** | **bool** |  | [optional] 
**is_billing_context** | **bool** |  | [optional] 
**is_pop_out** | **bool** |  | [optional] 
**is_service_or_activity_context** | **bool** |  | [optional] 
**iso_currency_code** | **str** |  | [optional] 
**last_load_time** | **str** |  | [optional] 
**member_current_date** | **str** |  | [optional] 
**no_future_records_flag** | **bool** |  | [optional] 
**pop_out_height** | **int** |  | [optional] 
**pop_out_width** | **int** |  | [optional] 
**require_reason_flag** | **bool** |  | [optional] 
**te_status_id** | **int** |  | [optional] 
**time_entry_additional_details** | [**List[TimeEntryDetailsViewModel]**](TimeEntryDetailsViewModel.md) |  | [optional] 
**time_entry_detail_model** | [**TimeEntryDetailsForApiViewModel**](TimeEntryDetailsForApiViewModel.md) |  | [optional] 
**time_entry_note_size** | **int** |  | [optional] 
**time_rec_id** | **int** |  | [optional] 
**time_sheet_rec_id** | **int** |  | [optional] 
**time_sheet_reversed_flag** | **bool** |  | [optional] 
**time_sheet_status_id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.time_entry_detail_view_model import TimeEntryDetailViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of TimeEntryDetailViewModel from a JSON string
time_entry_detail_view_model_instance = TimeEntryDetailViewModel.from_json(json)
# print the JSON string representation of the object
print TimeEntryDetailViewModel.to_json()

# convert the object into a dict
time_entry_detail_view_model_dict = time_entry_detail_view_model_instance.to_dict()
# create an instance of TimeEntryDetailViewModel from a dict
time_entry_detail_view_model_form_dict = time_entry_detail_view_model.from_dict(time_entry_detail_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


