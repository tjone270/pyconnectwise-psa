# ProjectStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**closed_flag** | **bool** |  | [optional] 
**custom_status_indicator_name** | **str** | Required when statusIndicator is Custom. Max length: 30; | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 30; | 
**no_time_flag** | **bool** |  | [optional] 
**status_indicator** | [**StatusIndicatorReference**](StatusIndicatorReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.project_status import ProjectStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStatus from a JSON string
project_status_instance = ProjectStatus.from_json(json)
# print the JSON string representation of the object
print ProjectStatus.to_json()

# convert the object into a dict
project_status_dict = project_status_instance.to_dict()
# create an instance of ProjectStatus from a dict
project_status_form_dict = project_status.from_dict(project_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


