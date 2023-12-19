# MemberDeactivationDepartmentMananager


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**re_assign_to_member** | [**MemberReference**](MemberReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.member_deactivation_department_mananager import MemberDeactivationDepartmentMananager

# TODO update the JSON string below
json = "{}"
# create an instance of MemberDeactivationDepartmentMananager from a JSON string
member_deactivation_department_mananager_instance = MemberDeactivationDepartmentMananager.from_json(json)
# print the JSON string representation of the object
print MemberDeactivationDepartmentMananager.to_json()

# convert the object into a dict
member_deactivation_department_mananager_dict = member_deactivation_department_mananager_instance.to_dict()
# create an instance of MemberDeactivationDepartmentMananager from a dict
member_deactivation_department_mananager_form_dict = member_deactivation_department_mananager.from_dict(member_deactivation_department_mananager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


