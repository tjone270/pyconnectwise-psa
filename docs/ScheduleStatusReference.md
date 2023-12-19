# ScheduleStatusReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.schedule_status_reference import ScheduleStatusReference

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleStatusReference from a JSON string
schedule_status_reference_instance = ScheduleStatusReference.from_json(json)
# print the JSON string representation of the object
print ScheduleStatusReference.to_json()

# convert the object into a dict
schedule_status_reference_dict = schedule_status_reference_instance.to_dict()
# create an instance of ScheduleStatusReference from a dict
schedule_status_reference_form_dict = schedule_status_reference.from_dict(schedule_status_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


