# MemberTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.member_type_info import MemberTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MemberTypeInfo from a JSON string
member_type_info_instance = MemberTypeInfo.from_json(json)
# print the JSON string representation of the object
print MemberTypeInfo.to_json()

# convert the object into a dict
member_type_info_dict = member_type_info_instance.to_dict()
# create an instance of MemberTypeInfo from a dict
member_type_info_form_dict = member_type_info.from_dict(member_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


