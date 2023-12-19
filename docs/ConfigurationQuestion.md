# ConfigurationQuestion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | **object** |  | [optional] 
**answer_id** | **int** |  | [optional] 
**field_type** | **str** |  | [optional] 
**number_of_decimals** | **int** |  | [optional] 
**question** | **str** |  | [optional] 
**question_id** | **int** |  | [optional] 
**required_flag** | **bool** |  | [optional] 
**sequence_number** | **float** |  | [optional] 

## Example

```python
from connectwise_psa.models.configuration_question import ConfigurationQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationQuestion from a JSON string
configuration_question_instance = ConfigurationQuestion.from_json(json)
# print the JSON string representation of the object
print ConfigurationQuestion.to_json()

# convert the object into a dict
configuration_question_dict = configuration_question_instance.to_dict()
# create an instance of ConfigurationQuestion from a dict
configuration_question_form_dict = configuration_question.from_dict(configuration_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


