# Survey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**instructions** | **str** |  Max length: 1000; | [optional] 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.survey import Survey

# TODO update the JSON string below
json = "{}"
# create an instance of Survey from a JSON string
survey_instance = Survey.from_json(json)
# print the JSON string representation of the object
print Survey.to_json()

# convert the object into a dict
survey_dict = survey_instance.to_dict()
# create an instance of Survey from a dict
survey_form_dict = survey.from_dict(survey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


