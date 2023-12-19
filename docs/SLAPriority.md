# SLAPriority


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**plan_within** | **float** |  | [optional] 
**plan_within_percent** | **int** |  | [optional] 
**priority** | [**PriorityReference**](PriorityReference.md) |  | [optional] 
**resolution_hours** | **float** |  | [optional] 
**resolution_percent** | **int** |  | [optional] 
**respond_hours** | **float** |  | [optional] 
**respond_percent** | **int** |  | [optional] 
**sla** | [**SLAReference**](SLAReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.sla_priority import SLAPriority

# TODO update the JSON string below
json = "{}"
# create an instance of SLAPriority from a JSON string
sla_priority_instance = SLAPriority.from_json(json)
# print the JSON string representation of the object
print SLAPriority.to_json()

# convert the object into a dict
sla_priority_dict = sla_priority_instance.to_dict()
# create an instance of SLAPriority from a dict
sla_priority_form_dict = sla_priority.from_dict(sla_priority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


