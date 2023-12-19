# ScheduleType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**charge_code** | [**ChargeCodeReference**](ChargeCodeReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  Max length: 1; | 
**name** | **str** |  Max length: 50; | 
**system_flag** | **bool** |  | [optional] 
**where** | [**ServiceLocationReference**](ServiceLocationReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.schedule_type import ScheduleType

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleType from a JSON string
schedule_type_instance = ScheduleType.from_json(json)
# print the JSON string representation of the object
print ScheduleType.to_json()

# convert the object into a dict
schedule_type_dict = schedule_type_instance.to_dict()
# create an instance of ScheduleType from a dict
schedule_type_form_dict = schedule_type.from_dict(schedule_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


