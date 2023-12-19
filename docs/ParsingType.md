# ParsingType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**parse_rule** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.parsing_type import ParsingType

# TODO update the JSON string below
json = "{}"
# create an instance of ParsingType from a JSON string
parsing_type_instance = ParsingType.from_json(json)
# print the JSON string representation of the object
print ParsingType.to_json()

# convert the object into a dict
parsing_type_dict = parsing_type_instance.to_dict()
# create an instance of ParsingType from a dict
parsing_type_form_dict = parsing_type.from_dict(parsing_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


