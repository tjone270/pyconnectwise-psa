# ServiceSurveyQuestionOption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** |  | [optional] 
**include_flag** | **bool** |  | [optional] 
**points** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.service_survey_question_option import ServiceSurveyQuestionOption

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSurveyQuestionOption from a JSON string
service_survey_question_option_instance = ServiceSurveyQuestionOption.from_json(json)
# print the JSON string representation of the object
print ServiceSurveyQuestionOption.to_json()

# convert the object into a dict
service_survey_question_option_dict = service_survey_question_option_instance.to_dict()
# create an instance of ServiceSurveyQuestionOption from a dict
service_survey_question_option_form_dict = service_survey_question_option.from_dict(service_survey_question_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


