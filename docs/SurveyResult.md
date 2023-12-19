# SurveyResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**contact_me_flag** | **bool** |  | [optional] 
**email_address** | **str** |  | [optional] 
**footer_response** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**results** | [**List[SurveyResultDetail]**](SurveyResultDetail.md) |  | [optional] 
**survey_id** | **int** |  | [optional] 
**ticket_id** | **int** |  | 
**total_points** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.survey_result import SurveyResult

# TODO update the JSON string below
json = "{}"
# create an instance of SurveyResult from a JSON string
survey_result_instance = SurveyResult.from_json(json)
# print the JSON string representation of the object
print SurveyResult.to_json()

# convert the object into a dict
survey_result_dict = survey_result_instance.to_dict()
# create an instance of SurveyResult from a dict
survey_result_form_dict = survey_result.from_dict(survey_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


