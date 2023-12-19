# ConfigurationTypeQuestion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**configuration_type** | [**ConfigurationTypeReference**](ConfigurationTypeReference.md) |  | [optional] 
**entry_type** | **str** |  | 
**field_type** | **str** |  | 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**number_of_decimals** | **int** |  | [optional] 
**question** | **str** |  Max length: 1000; | 
**required_flag** | **bool** |  | [optional] 
**sequence_number** | **float** |  | 

## Example

```python
from connectwise_psa.models.configuration_type_question import ConfigurationTypeQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationTypeQuestion from a JSON string
configuration_type_question_instance = ConfigurationTypeQuestion.from_json(json)
# print the JSON string representation of the object
print ConfigurationTypeQuestion.to_json()

# convert the object into a dict
configuration_type_question_dict = configuration_type_question_instance.to_dict()
# create an instance of ConfigurationTypeQuestion from a dict
configuration_type_question_form_dict = configuration_type_question.from_dict(configuration_type_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


