# ParsingVariable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**code** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.parsing_variable import ParsingVariable

# TODO update the JSON string below
json = "{}"
# create an instance of ParsingVariable from a JSON string
parsing_variable_instance = ParsingVariable.from_json(json)
# print the JSON string representation of the object
print ParsingVariable.to_json()

# convert the object into a dict
parsing_variable_dict = parsing_variable_instance.to_dict()
# create an instance of ParsingVariable from a dict
parsing_variable_form_dict = parsing_variable.from_dict(parsing_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


