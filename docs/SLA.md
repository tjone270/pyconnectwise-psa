# SLA


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**application_order** | **int** |  | [optional] 
**based_on** | **str** |  | 
**custom_calendar** | [**CalendarReference**](CalendarReference.md) |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**hi_impact_hi_urgency** | [**PriorityReference**](PriorityReference.md) |  | [optional] 
**hi_impact_low_urgency** | [**PriorityReference**](PriorityReference.md) |  | [optional] 
**hi_impact_med_urgency** | [**PriorityReference**](PriorityReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**low_impact_hi_urgency** | [**PriorityReference**](PriorityReference.md) |  | [optional] 
**low_impact_low_urgency** | [**PriorityReference**](PriorityReference.md) |  | [optional] 
**low_impact_med_urgency** | [**PriorityReference**](PriorityReference.md) |  | [optional] 
**med_impact_hi_urgency** | [**PriorityReference**](PriorityReference.md) |  | [optional] 
**med_impact_low_urgency** | [**PriorityReference**](PriorityReference.md) |  | [optional] 
**med_impact_med_urgency** | [**PriorityReference**](PriorityReference.md) |  | [optional] 
**name** | **str** |  Max length: 25; | 
**plan_within** | **float** |  | [optional] 
**plan_within_percent** | **int** |  | [optional] 
**resolution_hours** | **float** |  | [optional] 
**resolution_percent** | **int** |  | [optional] 
**respond_hours** | **float** |  | [optional] 
**respond_percent** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.sla import SLA

# TODO update the JSON string below
json = "{}"
# create an instance of SLA from a JSON string
sla_instance = SLA.from_json(json)
# print the JSON string representation of the object
print SLA.to_json()

# convert the object into a dict
sla_dict = sla_instance.to_dict()
# create an instance of SLA from a dict
sla_form_dict = sla.from_dict(sla_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


