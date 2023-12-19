# ScheduleColor


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**color** | **str** | Must be a valid Hexadecimal Color Code. | 
**end_percent** | **int** | A endPercent is required if startPercent has value. | [optional] 
**id** | **int** |  | [optional] 
**start_percent** | **int** | A startPercent (0 or higher) is required if endPercent has value. | [optional] 

## Example

```python
from connectwise_psa.models.schedule_color import ScheduleColor

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleColor from a JSON string
schedule_color_instance = ScheduleColor.from_json(json)
# print the JSON string representation of the object
print ScheduleColor.to_json()

# convert the object into a dict
schedule_color_dict = schedule_color_instance.to_dict()
# create an instance of ScheduleColor from a dict
schedule_color_form_dict = schedule_color.from_dict(schedule_color_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


