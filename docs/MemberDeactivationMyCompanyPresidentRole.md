# MemberDeactivationMyCompanyPresidentRole


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**re_assign_to_member** | [**MemberReference**](MemberReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.member_deactivation_my_company_president_role import MemberDeactivationMyCompanyPresidentRole

# TODO update the JSON string below
json = "{}"
# create an instance of MemberDeactivationMyCompanyPresidentRole from a JSON string
member_deactivation_my_company_president_role_instance = MemberDeactivationMyCompanyPresidentRole.from_json(json)
# print the JSON string representation of the object
print MemberDeactivationMyCompanyPresidentRole.to_json()

# convert the object into a dict
member_deactivation_my_company_president_role_dict = member_deactivation_my_company_president_role_instance.to_dict()
# create an instance of MemberDeactivationMyCompanyPresidentRole from a dict
member_deactivation_my_company_president_role_form_dict = member_deactivation_my_company_president_role.from_dict(member_deactivation_my_company_president_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


