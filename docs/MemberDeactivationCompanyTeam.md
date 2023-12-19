# MemberDeactivationCompanyTeam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**re_assign_to_contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**re_assign_to_member** | [**MemberReference**](MemberReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.member_deactivation_company_team import MemberDeactivationCompanyTeam

# TODO update the JSON string below
json = "{}"
# create an instance of MemberDeactivationCompanyTeam from a JSON string
member_deactivation_company_team_instance = MemberDeactivationCompanyTeam.from_json(json)
# print the JSON string representation of the object
print MemberDeactivationCompanyTeam.to_json()

# convert the object into a dict
member_deactivation_company_team_dict = member_deactivation_company_team_instance.to_dict()
# create an instance of MemberDeactivationCompanyTeam from a dict
member_deactivation_company_team_form_dict = member_deactivation_company_team.from_dict(member_deactivation_company_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


