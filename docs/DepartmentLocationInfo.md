# DepartmentLocationInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.department_location_info import DepartmentLocationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DepartmentLocationInfo from a JSON string
department_location_info_instance = DepartmentLocationInfo.from_json(json)
# print the JSON string representation of the object
print DepartmentLocationInfo.to_json()

# convert the object into a dict
department_location_info_dict = department_location_info_instance.to_dict()
# create an instance of DepartmentLocationInfo from a dict
department_location_info_form_dict = department_location_info.from_dict(department_location_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


