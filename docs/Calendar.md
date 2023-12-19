# Calendar


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**friday_end_time** | **str** |  | [optional] 
**friday_start_time** | **str** |  | [optional] 
**holiday_list** | [**HolidayListReference**](HolidayListReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**monday_end_time** | **str** |  | [optional] 
**monday_start_time** | **str** |  | [optional] 
**name** | **str** |  | 
**saturday_end_time** | **str** |  | [optional] 
**saturday_start_time** | **str** |  | [optional] 
**sunday_end_time** | **str** |  | [optional] 
**sunday_start_time** | **str** |  | [optional] 
**thursday_end_time** | **str** |  | [optional] 
**thursday_start_time** | **str** |  | [optional] 
**tuesday_end_time** | **str** |  | [optional] 
**tuesday_start_time** | **str** |  | [optional] 
**wednesday_end_time** | **str** |  | [optional] 
**wednesday_start_time** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.calendar import Calendar

# TODO update the JSON string below
json = "{}"
# create an instance of Calendar from a JSON string
calendar_instance = Calendar.from_json(json)
# print the JSON string representation of the object
print Calendar.to_json()

# convert the object into a dict
calendar_dict = calendar_instance.to_dict()
# create an instance of Calendar from a dict
calendar_form_dict = calendar.from_dict(calendar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


