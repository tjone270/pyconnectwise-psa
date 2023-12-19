# GenericBoardTeamReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**is_project_team_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.generic_board_team_reference import GenericBoardTeamReference

# TODO update the JSON string below
json = "{}"
# create an instance of GenericBoardTeamReference from a JSON string
generic_board_team_reference_instance = GenericBoardTeamReference.from_json(json)
# print the JSON string representation of the object
print GenericBoardTeamReference.to_json()

# convert the object into a dict
generic_board_team_reference_dict = generic_board_team_reference_instance.to_dict()
# create an instance of GenericBoardTeamReference from a dict
generic_board_team_reference_form_dict = generic_board_team_reference.from_dict(generic_board_team_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


