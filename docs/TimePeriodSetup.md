# TimePeriodSetup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**days_past_end_date** | **int** |  | 
**description** | **str** |  Max length: 100; | [optional] 
**first_period_end_date** | **date** |  | 
**id** | **int** |  | [optional] 
**last_day_flag** | **bool** | Only needed when type is monthly | [optional] 
**monthly_period_ends** | **int** | Only needed when type is monthly | [optional] 
**number_future_periods** | **int** |  | 
**period_apply_to** | **str** |  | 
**semi_monthly_first_period** | **int** | Only needed when type is semi-monthly | [optional] 
**semi_monthly_last_day_flag** | **bool** |  | [optional] 
**semi_monthly_second_period** | **int** | Only needed when type is semi-monthly | [optional] 
**type** | **str** |  | 
**year** | **int** |  | 

## Example

```python
from connectwise_psa.models.time_period_setup import TimePeriodSetup

# TODO update the JSON string below
json = "{}"
# create an instance of TimePeriodSetup from a JSON string
time_period_setup_instance = TimePeriodSetup.from_json(json)
# print the JSON string representation of the object
print TimePeriodSetup.to_json()

# convert the object into a dict
time_period_setup_dict = time_period_setup_instance.to_dict()
# create an instance of TimePeriodSetup from a dict
time_period_setup_form_dict = time_period_setup.from_dict(time_period_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


