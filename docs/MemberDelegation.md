# MemberDelegation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**date_end** | **datetime** |  | 
**date_start** | **datetime** |  | 
**delegated_to** | [**MemberReference**](MemberReference.md) |  | [optional] 
**delegation_type** | **str** |  | 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.member_delegation import MemberDelegation

# TODO update the JSON string below
json = "{}"
# create an instance of MemberDelegation from a JSON string
member_delegation_instance = MemberDelegation.from_json(json)
# print the JSON string representation of the object
print MemberDelegation.to_json()

# convert the object into a dict
member_delegation_dict = member_delegation_instance.to_dict()
# create an instance of MemberDelegation from a dict
member_delegation_form_dict = member_delegation.from_dict(member_delegation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


