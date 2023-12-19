# ServiceSurvey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**footer_text** | **str** |  Max length: 500; | [optional] 
**footer_text_visible_flag** | **bool** |  | [optional] 
**header_include_logo_flag** | **bool** |  | [optional] 
**header_text** | **str** |  Max length: 4000; | [optional] 
**header_text_visible_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**notify_member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**notify_who** | [**GenericIdIdentifierReference**](GenericIdIdentifierReference.md) |  | [optional] 
**notify_who_visible_flag** | **bool** |  | [optional] 
**thank_you_text** | **str** |  Max length: 4000; | [optional] 

## Example

```python
from connectwise_psa.models.service_survey import ServiceSurvey

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSurvey from a JSON string
service_survey_instance = ServiceSurvey.from_json(json)
# print the JSON string representation of the object
print ServiceSurvey.to_json()

# convert the object into a dict
service_survey_dict = service_survey_instance.to_dict()
# create an instance of ServiceSurvey from a dict
service_survey_form_dict = service_survey.from_dict(service_survey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


