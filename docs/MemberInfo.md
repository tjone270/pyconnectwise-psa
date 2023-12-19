# MemberInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**last_name** | **str** |  | [optional] 
**license_class** | **str** | F &#x3D; Full Member, A &#x3D; API Member, C &#x3D; StreamlineIT Member, X &#x3D; Subcontractor Member | [optional] 
**middle_initial** | **str** |  | [optional] 
**photo** | [**DocumentReference**](DocumentReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.member_info import MemberInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MemberInfo from a JSON string
member_info_instance = MemberInfo.from_json(json)
# print the JSON string representation of the object
print MemberInfo.to_json()

# convert the object into a dict
member_info_dict = member_info_instance.to_dict()
# create an instance of MemberInfo from a dict
member_info_form_dict = member_info.from_dict(member_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


