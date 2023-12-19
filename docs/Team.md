# Team


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**commission_percent** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**opportunity_id** | **int** |  | [optional] 
**referral_flag** | **bool** |  | [optional] 
**responsible_flag** | **bool** |  | [optional] 
**sales_team** | [**SalesTeamReference**](SalesTeamReference.md) |  | [optional] 
**type** | **str** |  | 

## Example

```python
from connectwise_psa.models.team import Team

# TODO update the JSON string below
json = "{}"
# create an instance of Team from a JSON string
team_instance = Team.from_json(json)
# print the JSON string representation of the object
print Team.to_json()

# convert the object into a dict
team_dict = team_instance.to_dict()
# create an instance of Team from a dict
team_form_dict = team.from_dict(team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


