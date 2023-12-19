# ProjectStatusInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.project_status_info import ProjectStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStatusInfo from a JSON string
project_status_info_instance = ProjectStatusInfo.from_json(json)
# print the JSON string representation of the object
print ProjectStatusInfo.to_json()

# convert the object into a dict
project_status_info_dict = project_status_info_instance.to_dict()
# create an instance of ProjectStatusInfo from a dict
project_status_info_form_dict = project_status_info.from_dict(project_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


