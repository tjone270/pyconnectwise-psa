# UserDefinedFieldValueModel


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
from connectwise_psa.models.user_defined_field_value_model import UserDefinedFieldValueModel

# TODO update the JSON string below
json = "{}"
# create an instance of UserDefinedFieldValueModel from a JSON string
user_defined_field_value_model_instance = UserDefinedFieldValueModel.from_json(json)
# print the JSON string representation of the object
print UserDefinedFieldValueModel.to_json()

# convert the object into a dict
user_defined_field_value_model_dict = user_defined_field_value_model_instance.to_dict()
# create an instance of UserDefinedFieldValueModel from a dict
user_defined_field_value_model_form_dict = user_defined_field_value_model.from_dict(user_defined_field_value_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


