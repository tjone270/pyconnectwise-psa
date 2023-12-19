# TeamRoleInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.team_role_info import TeamRoleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TeamRoleInfo from a JSON string
team_role_info_instance = TeamRoleInfo.from_json(json)
# print the JSON string representation of the object
print TeamRoleInfo.to_json()

# convert the object into a dict
team_role_info_dict = team_role_info_instance.to_dict()
# create an instance of TeamRoleInfo from a dict
team_role_info_form_dict = team_role_info.from_dict(team_role_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


