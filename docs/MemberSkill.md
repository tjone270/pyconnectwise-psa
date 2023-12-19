# MemberSkill


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**certified_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**notes** | **str** |  | [optional] 
**skill** | [**SkillReference**](SkillReference.md) |  | 
**skill_level** | **str** |  | 
**years_experience** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.member_skill import MemberSkill

# TODO update the JSON string below
json = "{}"
# create an instance of MemberSkill from a JSON string
member_skill_instance = MemberSkill.from_json(json)
# print the JSON string representation of the object
print MemberSkill.to_json()

# convert the object into a dict
member_skill_dict = member_skill_instance.to_dict()
# create an instance of MemberSkill from a dict
member_skill_form_dict = member_skill.from_dict(member_skill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


