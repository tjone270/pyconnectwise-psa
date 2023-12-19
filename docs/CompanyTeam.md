# CompanyTeam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**account_manager_flag** | **bool** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**sales_flag** | **bool** |  | [optional] 
**team_role** | [**TeamRoleReference**](TeamRoleReference.md) |  | [optional] 
**tech_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.company_team import CompanyTeam

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyTeam from a JSON string
company_team_instance = CompanyTeam.from_json(json)
# print the JSON string representation of the object
print CompanyTeam.to_json()

# convert the object into a dict
company_team_dict = company_team_instance.to_dict()
# create an instance of CompanyTeam from a dict
company_team_form_dict = company_team.from_dict(company_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


