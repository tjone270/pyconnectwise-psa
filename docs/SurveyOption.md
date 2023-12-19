# SurveyOption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**caption** | **str** |  Max length: 100; | 
**id** | **int** |  | [optional] 
**points** | **int** |  | 
**visibleflag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.survey_option import SurveyOption

# TODO update the JSON string below
json = "{}"
# create an instance of SurveyOption from a JSON string
survey_option_instance = SurveyOption.from_json(json)
# print the JSON string representation of the object
print SurveyOption.to_json()

# convert the object into a dict
survey_option_dict = survey_option_instance.to_dict()
# create an instance of SurveyOption from a dict
survey_option_form_dict = survey_option.from_dict(survey_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


