# ConfigurationTypeQuestionReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**question** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.configuration_type_question_reference import ConfigurationTypeQuestionReference

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationTypeQuestionReference from a JSON string
configuration_type_question_reference_instance = ConfigurationTypeQuestionReference.from_json(json)
# print the JSON string representation of the object
print ConfigurationTypeQuestionReference.to_json()

# convert the object into a dict
configuration_type_question_reference_dict = configuration_type_question_reference_instance.to_dict()
# create an instance of ConfigurationTypeQuestionReference from a dict
configuration_type_question_reference_form_dict = configuration_type_question_reference.from_dict(configuration_type_question_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


