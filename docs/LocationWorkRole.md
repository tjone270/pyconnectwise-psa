# LocationWorkRole


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 
**work_role_inactive_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.location_work_role import LocationWorkRole

# TODO update the JSON string below
json = "{}"
# create an instance of LocationWorkRole from a JSON string
location_work_role_instance = LocationWorkRole.from_json(json)
# print the JSON string representation of the object
print LocationWorkRole.to_json()

# convert the object into a dict
location_work_role_dict = location_work_role_instance.to_dict()
# create an instance of LocationWorkRole from a dict
location_work_role_form_dict = location_work_role.from_dict(location_work_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


