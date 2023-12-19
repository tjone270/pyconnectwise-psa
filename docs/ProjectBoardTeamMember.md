# ProjectBoardTeamMember


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**project_role** | [**ProjectRoleReference**](ProjectRoleReference.md) |  | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.project_board_team_member import ProjectBoardTeamMember

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBoardTeamMember from a JSON string
project_board_team_member_instance = ProjectBoardTeamMember.from_json(json)
# print the JSON string representation of the object
print ProjectBoardTeamMember.to_json()

# convert the object into a dict
project_board_team_member_dict = project_board_team_member_instance.to_dict()
# create an instance of ProjectBoardTeamMember from a dict
project_board_team_member_form_dict = project_board_team_member.from_dict(project_board_team_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


