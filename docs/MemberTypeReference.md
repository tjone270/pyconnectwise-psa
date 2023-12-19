# MemberTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.member_type_reference import MemberTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of MemberTypeReference from a JSON string
member_type_reference_instance = MemberTypeReference.from_json(json)
# print the JSON string representation of the object
print MemberTypeReference.to_json()

# convert the object into a dict
member_type_reference_dict = member_type_reference_instance.to_dict()
# create an instance of MemberTypeReference from a dict
member_type_reference_form_dict = member_type_reference.from_dict(member_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


