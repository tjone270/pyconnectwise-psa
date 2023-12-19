# ServiceTeam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**delete_notify_flag** | **bool** |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**leader** | [**MemberReference**](MemberReference.md) |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.service_team import ServiceTeam

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTeam from a JSON string
service_team_instance = ServiceTeam.from_json(json)
# print the JSON string representation of the object
print ServiceTeam.to_json()

# convert the object into a dict
service_team_dict = service_team_instance.to_dict()
# create an instance of ServiceTeam from a dict
service_team_form_dict = service_team.from_dict(service_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


