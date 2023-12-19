# SystemDepartmentReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.system_department_reference import SystemDepartmentReference

# TODO update the JSON string below
json = "{}"
# create an instance of SystemDepartmentReference from a JSON string
system_department_reference_instance = SystemDepartmentReference.from_json(json)
# print the JSON string representation of the object
print SystemDepartmentReference.to_json()

# convert the object into a dict
system_department_reference_dict = system_department_reference_instance.to_dict()
# create an instance of SystemDepartmentReference from a dict
system_department_reference_form_dict = system_department_reference.from_dict(system_department_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


