# ActivityStatusInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**closed_flag** | **bool** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.activity_status_info import ActivityStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityStatusInfo from a JSON string
activity_status_info_instance = ActivityStatusInfo.from_json(json)
# print the JSON string representation of the object
print ActivityStatusInfo.to_json()

# convert the object into a dict
activity_status_info_dict = activity_status_info_instance.to_dict()
# create an instance of ActivityStatusInfo from a dict
activity_status_info_form_dict = activity_status_info.from_dict(activity_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


