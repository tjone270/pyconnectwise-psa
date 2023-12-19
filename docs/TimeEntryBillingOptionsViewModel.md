# TimeEntryBillingOptionsViewModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied_hours** | **float** |  | [optional] 
**hourly_rate** | **float** |  | [optional] 
**invoice_hours** | **float** |  | [optional] 
**overage_rate** | **float** |  | [optional] 
**override_flag** | **bool** |  | [optional] 
**total_hours** | **float** |  | [optional] 

## Example

```python
from connectwise_psa.models.time_entry_billing_options_view_model import TimeEntryBillingOptionsViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of TimeEntryBillingOptionsViewModel from a JSON string
time_entry_billing_options_view_model_instance = TimeEntryBillingOptionsViewModel.from_json(json)
# print the JSON string representation of the object
print TimeEntryBillingOptionsViewModel.to_json()

# convert the object into a dict
time_entry_billing_options_view_model_dict = time_entry_billing_options_view_model_instance.to_dict()
# create an instance of TimeEntryBillingOptionsViewModel from a dict
time_entry_billing_options_view_model_form_dict = time_entry_billing_options_view_model.from_dict(time_entry_billing_options_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


