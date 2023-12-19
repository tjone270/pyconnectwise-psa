# ProjectBoardTeam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.project_board_team import ProjectBoardTeam

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBoardTeam from a JSON string
project_board_team_instance = ProjectBoardTeam.from_json(json)
# print the JSON string representation of the object
print ProjectBoardTeam.to_json()

# convert the object into a dict
project_board_team_dict = project_board_team_instance.to_dict()
# create an instance of ProjectBoardTeam from a dict
project_board_team_form_dict = project_board_team.from_dict(project_board_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


