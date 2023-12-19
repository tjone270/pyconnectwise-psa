# SurveyQuestion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**entry_type** | **str** |  | 
**field_type** | **str** |  | 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**number_of_decimals** | **int** |  | [optional] 
**question** | **str** |  Max length: 1000; | 
**required_flag** | **bool** |  | [optional] 
**sequence_number** | **float** |  | 
**survey** | [**SurveyReference**](SurveyReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.survey_question import SurveyQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of SurveyQuestion from a JSON string
survey_question_instance = SurveyQuestion.from_json(json)
# print the JSON string representation of the object
print SurveyQuestion.to_json()

# convert the object into a dict
survey_question_dict = survey_question_instance.to_dict()
# create an instance of SurveyQuestion from a dict
survey_question_form_dict = survey_question.from_dict(survey_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


