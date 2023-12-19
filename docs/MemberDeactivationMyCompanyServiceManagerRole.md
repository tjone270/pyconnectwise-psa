# MemberDeactivationMyCompanyServiceManagerRole


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**re_assign_to_member** | [**MemberReference**](MemberReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.member_deactivation_my_company_service_manager_role import MemberDeactivationMyCompanyServiceManagerRole

# TODO update the JSON string below
json = "{}"
# create an instance of MemberDeactivationMyCompanyServiceManagerRole from a JSON string
member_deactivation_my_company_service_manager_role_instance = MemberDeactivationMyCompanyServiceManagerRole.from_json(json)
# print the JSON string representation of the object
print MemberDeactivationMyCompanyServiceManagerRole.to_json()

# convert the object into a dict
member_deactivation_my_company_service_manager_role_dict = member_deactivation_my_company_service_manager_role_instance.to_dict()
# create an instance of MemberDeactivationMyCompanyServiceManagerRole from a dict
member_deactivation_my_company_service_manager_role_form_dict = member_deactivation_my_company_service_manager_role.from_dict(member_deactivation_my_company_service_manager_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


