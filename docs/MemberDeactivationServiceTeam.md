# MemberDeactivationServiceTeam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**re_assign_to_member** | [**MemberReference**](MemberReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.member_deactivation_service_team import MemberDeactivationServiceTeam

# TODO update the JSON string below
json = "{}"
# create an instance of MemberDeactivationServiceTeam from a JSON string
member_deactivation_service_team_instance = MemberDeactivationServiceTeam.from_json(json)
# print the JSON string representation of the object
print MemberDeactivationServiceTeam.to_json()

# convert the object into a dict
member_deactivation_service_team_dict = member_deactivation_service_team_instance.to_dict()
# create an instance of MemberDeactivationServiceTeam from a dict
member_deactivation_service_team_form_dict = member_deactivation_service_team.from_dict(member_deactivation_service_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


