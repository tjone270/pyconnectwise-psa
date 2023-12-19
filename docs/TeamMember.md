# TeamMember


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**team** | [**ServiceTeamReference**](ServiceTeamReference.md) |  | [optional] 
**team_leader_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.team_member import TeamMember

# TODO update the JSON string below
json = "{}"
# create an instance of TeamMember from a JSON string
team_member_instance = TeamMember.from_json(json)
# print the JSON string representation of the object
print TeamMember.to_json()

# convert the object into a dict
team_member_dict = team_member_instance.to_dict()
# create an instance of TeamMember from a dict
team_member_form_dict = team_member.from_dict(team_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


