# WorkRoleLocation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**hourly_rate** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.work_role_location import WorkRoleLocation

# TODO update the JSON string below
json = "{}"
# create an instance of WorkRoleLocation from a JSON string
work_role_location_instance = WorkRoleLocation.from_json(json)
# print the JSON string representation of the object
print WorkRoleLocation.to_json()

# convert the object into a dict
work_role_location_dict = work_role_location_instance.to_dict()
# create an instance of WorkRoleLocation from a dict
work_role_location_form_dict = work_role_location.from_dict(work_role_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


