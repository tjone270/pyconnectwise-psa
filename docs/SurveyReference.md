# SurveyReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.survey_reference import SurveyReference

# TODO update the JSON string below
json = "{}"
# create an instance of SurveyReference from a JSON string
survey_reference_instance = SurveyReference.from_json(json)
# print the JSON string representation of the object
print SurveyReference.to_json()

# convert the object into a dict
survey_reference_dict = survey_reference_instance.to_dict()
# create an instance of SurveyReference from a dict
survey_reference_form_dict = survey_reference.from_dict(survey_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


