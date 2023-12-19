# BoardTeamInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.board_team_info import BoardTeamInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BoardTeamInfo from a JSON string
board_team_info_instance = BoardTeamInfo.from_json(json)
# print the JSON string representation of the object
print BoardTeamInfo.to_json()

# convert the object into a dict
board_team_info_dict = board_team_info_instance.to_dict()
# create an instance of BoardTeamInfo from a dict
board_team_info_form_dict = board_team_info.from_dict(board_team_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


