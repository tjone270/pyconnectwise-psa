# TimeEntryChargeToSelection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_rec_id** | **int** |  | [optional] 
**add_notes_to_desc** | **bool** |  | [optional] 
**add_notes_to_internal** | **bool** |  | [optional] 
**add_notes_to_resolution** | **bool** |  | [optional] 
**agr_expense_billing_options_no_default_flag** | **bool** |  | [optional] 
**agr_name** | **str** |  | [optional] 
**agr_rec_id** | **int** |  | [optional] 
**billing_option_rec_id** | **int** |  | [optional] 
**billing_unit_name** | **str** |  | [optional] 
**billing_unit_rec_id** | **int** |  | [optional] 
**charge_code_rec_id** | **int** |  | [optional] 
**charge_company_id** | **int** |  | [optional] 
**charge_company_name** | **str** |  | [optional] 
**charge_company_no_service_flag** | **bool** |  | [optional] 
**charge_description** | **str** |  | [optional] 
**charge_rec_id** | **int** |  | [optional] 
**company_address_rec_id** | **int** |  | [optional] 
**contact_email_address** | **str** |  | [optional] 
**contact_name** | **str** |  | [optional] 
**contact_rec_id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**disable_successor_time** | **bool** |  | [optional] 
**expense_billing_option_rec_id** | **int** |  | [optional] 
**expense_billing_option_text** | **str** |  | [optional] 
**expense_billing_options_no_default_flag** | **bool** |  | [optional] 
**owner_level_name** | **str** |  | [optional] 
**owner_level_rec_id** | **int** |  | [optional] 
**phase_name** | **str** |  | [optional] 
**phase_rec_id** | **int** |  | [optional] 
**project_name** | **str** |  | [optional] 
**project_rec_id** | **int** |  | [optional] 
**rec_type** | **str** |  | [optional] 
**service_rec_id** | **int** |  | [optional] 
**sr_member_is_resource_flag** | **bool** |  | [optional] 
**sr_status_closed_flag** | **bool** |  | [optional] 
**sr_status_desc** | **str** |  | [optional] 
**sr_status_no_time_flag** | **bool** |  | [optional] 
**sr_status_rec_id** | **int** |  | [optional] 
**work_role_name** | **str** |  | [optional] 
**work_role_rec_id** | **int** |  | [optional] 
**work_type_name** | **str** |  | [optional] 
**work_type_rec_id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.time_entry_charge_to_selection import TimeEntryChargeToSelection

# TODO update the JSON string below
json = "{}"
# create an instance of TimeEntryChargeToSelection from a JSON string
time_entry_charge_to_selection_instance = TimeEntryChargeToSelection.from_json(json)
# print the JSON string representation of the object
print TimeEntryChargeToSelection.to_json()

# convert the object into a dict
time_entry_charge_to_selection_dict = time_entry_charge_to_selection_instance.to_dict()
# create an instance of TimeEntryChargeToSelection from a dict
time_entry_charge_to_selection_form_dict = time_entry_charge_to_selection.from_dict(time_entry_charge_to_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


