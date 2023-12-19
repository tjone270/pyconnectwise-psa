# DepartmentInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.department_info import DepartmentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentInfo from a JSON string
department_info_instance = DepartmentInfo.from_json(json)
# print the JSON string representation of the object
print DepartmentInfo.to_json()

# convert the object into a dict
department_info_dict = department_info_instance.to_dict()
# create an instance of DepartmentInfo from a dict
department_info_form_dict = department_info.from_dict(department_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


