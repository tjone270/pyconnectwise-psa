# ScheduleSpanReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.schedule_span_reference import ScheduleSpanReference

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleSpanReference from a JSON string
schedule_span_reference_instance = ScheduleSpanReference.from_json(json)
# print the JSON string representation of the object
print ScheduleSpanReference.to_json()

# convert the object into a dict
schedule_span_reference_dict = schedule_span_reference_instance.to_dict()
# create an instance of ScheduleSpanReference from a dict
schedule_span_reference_form_dict = schedule_span_reference.from_dict(schedule_span_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


