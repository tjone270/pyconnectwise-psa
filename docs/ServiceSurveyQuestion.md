# ServiceSurveyQuestion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**include_flag** | **bool** |  | [optional] 
**no_answer_points** | **int** |  | [optional] 
**options** | [**List[ServiceSurveyQuestionOption]**](ServiceSurveyQuestionOption.md) |  | [optional] 
**question** | **str** |  Max length: 1000; | 
**required_flag** | **bool** |  | [optional] 
**sequence_number** | **int** |  | [optional] 
**survey_id** | **int** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from connectwise_psa.models.service_survey_question import ServiceSurveyQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSurveyQuestion from a JSON string
service_survey_question_instance = ServiceSurveyQuestion.from_json(json)
# print the JSON string representation of the object
print ServiceSurveyQuestion.to_json()

# convert the object into a dict
service_survey_question_dict = service_survey_question_instance.to_dict()
# create an instance of ServiceSurveyQuestion from a dict
service_survey_question_form_dict = service_survey_question.from_dict(service_survey_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


