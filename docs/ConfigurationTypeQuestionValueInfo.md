# ConfigurationTypeQuestionValueInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**configuration_type** | [**ConfigurationTypeReference**](ConfigurationTypeReference.md) |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**question** | [**ConfigurationTypeQuestionReference**](ConfigurationTypeQuestionReference.md) |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.configuration_type_question_value_info import ConfigurationTypeQuestionValueInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationTypeQuestionValueInfo from a JSON string
configuration_type_question_value_info_instance = ConfigurationTypeQuestionValueInfo.from_json(json)
# print the JSON string representation of the object
print ConfigurationTypeQuestionValueInfo.to_json()

# convert the object into a dict
configuration_type_question_value_info_dict = configuration_type_question_value_info_instance.to_dict()
# create an instance of ConfigurationTypeQuestionValueInfo from a dict
configuration_type_question_value_info_form_dict = configuration_type_question_value_info.from_dict(configuration_type_question_value_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


