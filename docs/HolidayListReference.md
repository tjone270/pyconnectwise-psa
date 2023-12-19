# HolidayListReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.holiday_list_reference import HolidayListReference

# TODO update the JSON string below
json = "{}"
# create an instance of HolidayListReference from a JSON string
holiday_list_reference_instance = HolidayListReference.from_json(json)
# print the JSON string representation of the object
print HolidayListReference.to_json()

# convert the object into a dict
holiday_list_reference_dict = holiday_list_reference_instance.to_dict()
# create an instance of HolidayListReference from a dict
holiday_list_reference_form_dict = holiday_list_reference.from_dict(holiday_list_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


