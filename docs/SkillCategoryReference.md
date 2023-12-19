# SkillCategoryReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.skill_category_reference import SkillCategoryReference

# TODO update the JSON string below
json = "{}"
# create an instance of SkillCategoryReference from a JSON string
skill_category_reference_instance = SkillCategoryReference.from_json(json)
# print the JSON string representation of the object
print SkillCategoryReference.to_json()

# convert the object into a dict
skill_category_reference_dict = skill_category_reference_instance.to_dict()
# create an instance of SkillCategoryReference from a dict
skill_category_reference_form_dict = skill_category_reference.from_dict(skill_category_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


