# BoardTeam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**board_id** | **int** |  | [optional] 
**business_unit_id** | **int** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**default_round_robin_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**location_id** | **int** |  | [optional] 
**members** | **List[int]** |  | [optional] 
**name** | **str** |  Max length: 30; | 
**notify_on_ticket_delete** | **bool** |  | [optional] 
**round_robin_flag** | **bool** |  | [optional] 
**team_leader** | [**MemberReference**](MemberReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.board_team import BoardTeam

# TODO update the JSON string below
json = "{}"
# create an instance of BoardTeam from a JSON string
board_team_instance = BoardTeam.from_json(json)
# print the JSON string representation of the object
print BoardTeam.to_json()

# convert the object into a dict
board_team_dict = board_team_instance.to_dict()
# create an instance of BoardTeam from a dict
board_team_form_dict = board_team.from_dict(board_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


