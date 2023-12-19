# ProjectBoardTeamInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.project_board_team_info import ProjectBoardTeamInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectBoardTeamInfo from a JSON string
project_board_team_info_instance = ProjectBoardTeamInfo.from_json(json)
# print the JSON string representation of the object
print ProjectBoardTeamInfo.to_json()

# convert the object into a dict
project_board_team_info_dict = project_board_team_info_instance.to_dict()
# create an instance of ProjectBoardTeamInfo from a dict
project_board_team_info_form_dict = project_board_team_info.from_dict(project_board_team_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


