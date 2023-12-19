# MemberDeactivationSalesTeam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**re_assign_to_member** | [**MemberReference**](MemberReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.member_deactivation_sales_team import MemberDeactivationSalesTeam

# TODO update the JSON string below
json = "{}"
# create an instance of MemberDeactivationSalesTeam from a JSON string
member_deactivation_sales_team_instance = MemberDeactivationSalesTeam.from_json(json)
# print the JSON string representation of the object
print MemberDeactivationSalesTeam.to_json()

# convert the object into a dict
member_deactivation_sales_team_dict = member_deactivation_sales_team_instance.to_dict()
# create an instance of MemberDeactivationSalesTeam from a dict
member_deactivation_sales_team_form_dict = member_deactivation_sales_team.from_dict(member_deactivation_sales_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


