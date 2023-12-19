# SalesTeamMember


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**allow_access_flag** | **bool** |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.sales_team_member import SalesTeamMember

# TODO update the JSON string below
json = "{}"
# create an instance of SalesTeamMember from a JSON string
sales_team_member_instance = SalesTeamMember.from_json(json)
# print the JSON string representation of the object
print SalesTeamMember.to_json()

# convert the object into a dict
sales_team_member_dict = sales_team_member_instance.to_dict()
# create an instance of SalesTeamMember from a dict
sales_team_member_form_dict = sales_team_member.from_dict(sales_team_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


