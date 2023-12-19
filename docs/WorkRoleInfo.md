# WorkRoleInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.work_role_info import WorkRoleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WorkRoleInfo from a JSON string
work_role_info_instance = WorkRoleInfo.from_json(json)
# print the JSON string representation of the object
print WorkRoleInfo.to_json()

# convert the object into a dict
work_role_info_dict = work_role_info_instance.to_dict()
# create an instance of WorkRoleInfo from a dict
work_role_info_form_dict = work_role_info.from_dict(work_role_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


