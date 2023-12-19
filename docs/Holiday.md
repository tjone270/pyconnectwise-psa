# Holiday


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**all_day_flag** | **bool** | Can be set to false to set a holiday for specific hours (Defaults to True). | [optional] 
**var_date** | **date** |  | 
**holiday_list** | [**HolidayListReference**](HolidayListReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**time_end** | **str** |  | [optional] 
**time_start** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.holiday import Holiday

# TODO update the JSON string below
json = "{}"
# create an instance of Holiday from a JSON string
holiday_instance = Holiday.from_json(json)
# print the JSON string representation of the object
print Holiday.to_json()

# convert the object into a dict
holiday_dict = holiday_instance.to_dict()
# create an instance of Holiday from a dict
holiday_form_dict = holiday.from_dict(holiday_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


