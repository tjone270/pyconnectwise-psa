# UserDefinedFieldValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filtered** | **bool** |  | [optional] 
**row_num** | **int** |  | [optional] 
**skip_location_and_billing_unit** | **bool** |  | [optional] 
**user_defined_field_rec_id** | **int** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.user_defined_field_value import UserDefinedFieldValue

# TODO update the JSON string below
json = "{}"
# create an instance of UserDefinedFieldValue from a JSON string
user_defined_field_value_instance = UserDefinedFieldValue.from_json(json)
# print the JSON string representation of the object
print UserDefinedFieldValue.to_json()

# convert the object into a dict
user_defined_field_value_dict = user_defined_field_value_instance.to_dict()
# create an instance of UserDefinedFieldValue from a dict
user_defined_field_value_form_dict = user_defined_field_value.from_dict(user_defined_field_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


