# HolidayList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.holiday_list import HolidayList

# TODO update the JSON string below
json = "{}"
# create an instance of HolidayList from a JSON string
holiday_list_instance = HolidayList.from_json(json)
# print the JSON string representation of the object
print HolidayList.to_json()

# convert the object into a dict
holiday_list_dict = holiday_list_instance.to_dict()
# create an instance of HolidayList from a dict
holiday_list_form_dict = holiday_list.from_dict(holiday_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


