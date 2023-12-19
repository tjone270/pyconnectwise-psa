# TimeAccrual


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**holiday_available_type** | **str** |  | [optional] 
**holiday_carryover_allowed_flag** | **bool** |  | [optional] 
**holiday_carryover_limit** | **float** |  | [optional] 
**holiday_flag** | **bool** | if holidayFlag is set to false, system will clear out or ignore the values of holidayAvailableType, holidayCarryoverAllowedFlag, holidayCarryoverLimit | [optional] 
**id** | **int** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**pto_available_type** | **str** |  | [optional] 
**pto_carryover_allowed_flag** | **bool** |  | [optional] 
**pto_carryover_limit** | **float** |  | [optional] 
**pto_flag** | **bool** | if ptoFlag is set to false, system will clear out or ignore the values of ptoAvailableType, ptoCarryoverAllowedFlag, ptoCarryoverLimit | [optional] 
**sick_available_type** | **str** |  | [optional] 
**sick_carryover_allowed_flag** | **bool** |  | [optional] 
**sick_carryover_limit** | **float** |  | [optional] 
**sick_flag** | **bool** | if sickFlag is set to false, system will clear out or ignore the values of sickAvailableType, sickCarryoverAllowedFlag, sickCarryoverLimit | [optional] 
**vacation_available_type** | **str** |  | [optional] 
**vacation_carryover_allowed_flag** | **bool** |  | [optional] 
**vacation_carryover_limit** | **float** |  | [optional] 
**vacation_flag** | **bool** | if vacationFlag is set to false, system will clear out or ingore the values of vacationAvailableType, vacationCarryoverAllowedFlag, vacationCarryoverLimit | [optional] 

## Example

```python
from connectwise_psa.models.time_accrual import TimeAccrual

# TODO update the JSON string below
json = "{}"
# create an instance of TimeAccrual from a JSON string
time_accrual_instance = TimeAccrual.from_json(json)
# print the JSON string representation of the object
print TimeAccrual.to_json()

# convert the object into a dict
time_accrual_dict = time_accrual_instance.to_dict()
# create an instance of TimeAccrual from a dict
time_accrual_form_dict = time_accrual.from_dict(time_accrual_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


