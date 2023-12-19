# CalendarInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.calendar_info import CalendarInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarInfo from a JSON string
calendar_info_instance = CalendarInfo.from_json(json)
# print the JSON string representation of the object
print CalendarInfo.to_json()

# convert the object into a dict
calendar_info_dict = calendar_info_instance.to_dict()
# create an instance of CalendarInfo from a dict
calendar_info_form_dict = calendar_info.from_dict(calendar_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


