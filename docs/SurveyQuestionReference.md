# SurveyQuestionReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**question** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.survey_question_reference import SurveyQuestionReference

# TODO update the JSON string below
json = "{}"
# create an instance of SurveyQuestionReference from a JSON string
survey_question_reference_instance = SurveyQuestionReference.from_json(json)
# print the JSON string representation of the object
print SurveyQuestionReference.to_json()

# convert the object into a dict
survey_question_reference_dict = survey_question_reference_instance.to_dict()
# create an instance of SurveyQuestionReference from a dict
survey_question_reference_form_dict = survey_question_reference.from_dict(survey_question_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


