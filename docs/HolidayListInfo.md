# HolidayListInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.holiday_list_info import HolidayListInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HolidayListInfo from a JSON string
holiday_list_info_instance = HolidayListInfo.from_json(json)
# print the JSON string representation of the object
print HolidayListInfo.to_json()

# convert the object into a dict
holiday_list_info_dict = holiday_list_info_instance.to_dict()
# create an instance of HolidayListInfo from a dict
holiday_list_info_form_dict = holiday_list_info.from_dict(holiday_list_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


