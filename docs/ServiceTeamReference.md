# ServiceTeamReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.service_team_reference import ServiceTeamReference

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTeamReference from a JSON string
service_team_reference_instance = ServiceTeamReference.from_json(json)
# print the JSON string representation of the object
print ServiceTeamReference.to_json()

# convert the object into a dict
service_team_reference_dict = service_team_reference_instance.to_dict()
# create an instance of ServiceTeamReference from a dict
service_team_reference_form_dict = service_team_reference.from_dict(service_team_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


