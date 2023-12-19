# SurveyResultDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | **object** | If question type is Selection, this should be the option array index. | [optional] 
**question_id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.survey_result_detail import SurveyResultDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SurveyResultDetail from a JSON string
survey_result_detail_instance = SurveyResultDetail.from_json(json)
# print the JSON string representation of the object
print SurveyResultDetail.to_json()

# convert the object into a dict
survey_result_detail_dict = survey_result_detail_instance.to_dict()
# create an instance of SurveyResultDetail from a dict
survey_result_detail_form_dict = survey_result_detail.from_dict(survey_result_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


