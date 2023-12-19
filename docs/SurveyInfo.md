# SurveyInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.survey_info import SurveyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SurveyInfo from a JSON string
survey_info_instance = SurveyInfo.from_json(json)
# print the JSON string representation of the object
print SurveyInfo.to_json()

# convert the object into a dict
survey_info_dict = survey_info_instance.to_dict()
# create an instance of SurveyInfo from a dict
survey_info_form_dict = survey_info.from_dict(survey_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


