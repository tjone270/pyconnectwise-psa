# ConfigurationTypeQuestionInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**configuration_type** | [**ConfigurationTypeReference**](ConfigurationTypeReference.md) |  | [optional] 
**entry_type** | **str** |  | [optional] 
**field_type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**number_of_decimals** | **int** |  | [optional] 
**question** | **str** |  | [optional] 
**required_flag** | **bool** |  | [optional] 
**sequence_number** | **float** |  | [optional] 

## Example

```python
from connectwise_psa.models.configuration_type_question_info import ConfigurationTypeQuestionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationTypeQuestionInfo from a JSON string
configuration_type_question_info_instance = ConfigurationTypeQuestionInfo.from_json(json)
# print the JSON string representation of the object
print ConfigurationTypeQuestionInfo.to_json()

# convert the object into a dict
configuration_type_question_info_dict = configuration_type_question_info_instance.to_dict()
# create an instance of ConfigurationTypeQuestionInfo from a dict
configuration_type_question_info_form_dict = configuration_type_question_info.from_dict(configuration_type_question_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


