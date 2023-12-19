# SkillReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.skill_reference import SkillReference

# TODO update the JSON string below
json = "{}"
# create an instance of SkillReference from a JSON string
skill_reference_instance = SkillReference.from_json(json)
# print the JSON string representation of the object
print SkillReference.to_json()

# convert the object into a dict
skill_reference_dict = skill_reference_instance.to_dict()
# create an instance of SkillReference from a dict
skill_reference_form_dict = skill_reference.from_dict(skill_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


