# LocationDepartment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.location_department import LocationDepartment

# TODO update the JSON string below
json = "{}"
# create an instance of LocationDepartment from a JSON string
location_department_instance = LocationDepartment.from_json(json)
# print the JSON string representation of the object
print LocationDepartment.to_json()

# convert the object into a dict
location_department_dict = location_department_instance.to_dict()
# create an instance of LocationDepartment from a dict
location_department_form_dict = location_department.from_dict(location_department_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


