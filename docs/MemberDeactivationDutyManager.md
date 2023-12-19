# MemberDeactivationDutyManager


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**re_assign_to_member** | [**MemberReference**](MemberReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.member_deactivation_duty_manager import MemberDeactivationDutyManager

# TODO update the JSON string below
json = "{}"
# create an instance of MemberDeactivationDutyManager from a JSON string
member_deactivation_duty_manager_instance = MemberDeactivationDutyManager.from_json(json)
# print the JSON string representation of the object
print MemberDeactivationDutyManager.to_json()

# convert the object into a dict
member_deactivation_duty_manager_dict = member_deactivation_duty_manager_instance.to_dict()
# create an instance of MemberDeactivationDutyManager from a dict
member_deactivation_duty_manager_form_dict = member_deactivation_duty_manager.from_dict(member_deactivation_duty_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


