# ProjectTeamMember


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**hours** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**project_id** | **int** |  | [optional] 
**project_role** | [**ProjectRoleReference**](ProjectRoleReference.md) |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.project_team_member import ProjectTeamMember

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTeamMember from a JSON string
project_team_member_instance = ProjectTeamMember.from_json(json)
# print the JSON string representation of the object
print ProjectTeamMember.to_json()

# convert the object into a dict
project_team_member_dict = project_team_member_instance.to_dict()
# create an instance of ProjectTeamMember from a dict
project_team_member_form_dict = project_team_member.from_dict(project_team_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


