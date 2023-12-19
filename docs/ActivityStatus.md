# ActivityStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**closed_flag** | **bool** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 30; | 
**spawn_followup_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.activity_status import ActivityStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityStatus from a JSON string
activity_status_instance = ActivityStatus.from_json(json)
# print the JSON string representation of the object
print ActivityStatus.to_json()

# convert the object into a dict
activity_status_dict = activity_status_instance.to_dict()
# create an instance of ActivityStatus from a dict
activity_status_form_dict = activity_status.from_dict(activity_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


