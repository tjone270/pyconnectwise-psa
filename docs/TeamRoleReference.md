# TeamRoleReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.team_role_reference import TeamRoleReference

# TODO update the JSON string below
json = "{}"
# create an instance of TeamRoleReference from a JSON string
team_role_reference_instance = TeamRoleReference.from_json(json)
# print the JSON string representation of the object
print TeamRoleReference.to_json()

# convert the object into a dict
team_role_reference_dict = team_role_reference_instance.to_dict()
# create an instance of TeamRoleReference from a dict
team_role_reference_form_dict = team_role_reference.from_dict(team_role_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


