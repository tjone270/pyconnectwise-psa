# SurveyQuestionValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**point_value** | **int** |  | [optional] 
**question** | [**SurveyQuestionReference**](SurveyQuestionReference.md) |  | [optional] 
**survey** | [**SurveyReference**](SurveyReference.md) |  | [optional] 
**value** | **str** |  Max length: 1000; | 

## Example

```python
from connectwise_psa.models.survey_question_value import SurveyQuestionValue

# TODO update the JSON string below
json = "{}"
# create an instance of SurveyQuestionValue from a JSON string
survey_question_value_instance = SurveyQuestionValue.from_json(json)
# print the JSON string representation of the object
print SurveyQuestionValue.to_json()

# convert the object into a dict
survey_question_value_dict = survey_question_value_instance.to_dict()
# create an instance of SurveyQuestionValue from a dict
survey_question_value_form_dict = survey_question_value.from_dict(survey_question_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


