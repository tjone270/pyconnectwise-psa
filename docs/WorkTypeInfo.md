# WorkTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**activity_default_flag** | **bool** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.work_type_info import WorkTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WorkTypeInfo from a JSON string
work_type_info_instance = WorkTypeInfo.from_json(json)
# print the JSON string representation of the object
print WorkTypeInfo.to_json()

# convert the object into a dict
work_type_info_dict = work_type_info_instance.to_dict()
# create an instance of WorkTypeInfo from a dict
work_type_info_form_dict = work_type_info.from_dict(work_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


