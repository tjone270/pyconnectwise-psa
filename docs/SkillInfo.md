# SkillInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.skill_info import SkillInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SkillInfo from a JSON string
skill_info_instance = SkillInfo.from_json(json)
# print the JSON string representation of the object
print SkillInfo.to_json()

# convert the object into a dict
skill_info_dict = skill_info_instance.to_dict()
# create an instance of SkillInfo from a dict
skill_info_form_dict = skill_info.from_dict(skill_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


