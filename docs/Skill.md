# Skill


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**category** | [**SkillCategoryReference**](SkillCategoryReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.skill import Skill

# TODO update the JSON string below
json = "{}"
# create an instance of Skill from a JSON string
skill_instance = Skill.from_json(json)
# print the JSON string representation of the object
print Skill.to_json()

# convert the object into a dict
skill_dict = skill_instance.to_dict()
# create an instance of Skill from a dict
skill_form_dict = skill.from_dict(skill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


