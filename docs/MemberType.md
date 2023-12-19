# MemberType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 30; | 

## Example

```python
from connectwise_psa.models.member_type import MemberType

# TODO update the JSON string below
json = "{}"
# create an instance of MemberType from a JSON string
member_type_instance = MemberType.from_json(json)
# print the JSON string representation of the object
print MemberType.to_json()

# convert the object into a dict
member_type_dict = member_type_instance.to_dict()
# create an instance of MemberType from a dict
member_type_form_dict = member_type.from_dict(member_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


