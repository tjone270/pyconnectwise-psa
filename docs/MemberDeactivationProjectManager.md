# MemberDeactivationProjectManager


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**re_assign_to_member** | [**MemberReference**](MemberReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.member_deactivation_project_manager import MemberDeactivationProjectManager

# TODO update the JSON string below
json = "{}"
# create an instance of MemberDeactivationProjectManager from a JSON string
member_deactivation_project_manager_instance = MemberDeactivationProjectManager.from_json(json)
# print the JSON string representation of the object
print MemberDeactivationProjectManager.to_json()

# convert the object into a dict
member_deactivation_project_manager_dict = member_deactivation_project_manager_instance.to_dict()
# create an instance of MemberDeactivationProjectManager from a dict
member_deactivation_project_manager_form_dict = member_deactivation_project_manager.from_dict(member_deactivation_project_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


