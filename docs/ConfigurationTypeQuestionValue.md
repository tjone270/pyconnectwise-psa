# ConfigurationTypeQuestionValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**configuration_type** | [**ConfigurationTypeReference**](ConfigurationTypeReference.md) |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**question** | [**ConfigurationTypeQuestionReference**](ConfigurationTypeQuestionReference.md) |  | [optional] 
**value** | **str** |  Max length: 1000; | 

## Example

```python
from connectwise_psa.models.configuration_type_question_value import ConfigurationTypeQuestionValue

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationTypeQuestionValue from a JSON string
configuration_type_question_value_instance = ConfigurationTypeQuestionValue.from_json(json)
# print the JSON string representation of the object
print ConfigurationTypeQuestionValue.to_json()

# convert the object into a dict
configuration_type_question_value_dict = configuration_type_question_value_instance.to_dict()
# create an instance of ConfigurationTypeQuestionValue from a dict
configuration_type_question_value_form_dict = configuration_type_question_value.from_dict(configuration_type_question_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


