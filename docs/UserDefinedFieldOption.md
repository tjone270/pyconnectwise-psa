# UserDefinedFieldOption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**option_value** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.user_defined_field_option import UserDefinedFieldOption

# TODO update the JSON string below
json = "{}"
# create an instance of UserDefinedFieldOption from a JSON string
user_defined_field_option_instance = UserDefinedFieldOption.from_json(json)
# print the JSON string representation of the object
print UserDefinedFieldOption.to_json()

# convert the object into a dict
user_defined_field_option_dict = user_defined_field_option_instance.to_dict()
# create an instance of UserDefinedFieldOption from a dict
user_defined_field_option_form_dict = user_defined_field_option.from_dict(user_defined_field_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


