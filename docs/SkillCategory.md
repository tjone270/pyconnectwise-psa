# SkillCategory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 30; | 

## Example

```python
from connectwise_psa.models.skill_category import SkillCategory

# TODO update the JSON string below
json = "{}"
# create an instance of SkillCategory from a JSON string
skill_category_instance = SkillCategory.from_json(json)
# print the JSON string representation of the object
print SkillCategory.to_json()

# convert the object into a dict
skill_category_dict = skill_category_instance.to_dict()
# create an instance of SkillCategory from a dict
skill_category_form_dict = skill_category.from_dict(skill_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


