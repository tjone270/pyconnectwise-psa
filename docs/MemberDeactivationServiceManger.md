# MemberDeactivationServiceManger


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**re_assign_to_member** | [**MemberReference**](MemberReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.member_deactivation_service_manger import MemberDeactivationServiceManger

# TODO update the JSON string below
json = "{}"
# create an instance of MemberDeactivationServiceManger from a JSON string
member_deactivation_service_manger_instance = MemberDeactivationServiceManger.from_json(json)
# print the JSON string representation of the object
print MemberDeactivationServiceManger.to_json()

# convert the object into a dict
member_deactivation_service_manger_dict = member_deactivation_service_manger_instance.to_dict()
# create an instance of MemberDeactivationServiceManger from a dict
member_deactivation_service_manger_form_dict = member_deactivation_service_manger.from_dict(member_deactivation_service_manger_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


