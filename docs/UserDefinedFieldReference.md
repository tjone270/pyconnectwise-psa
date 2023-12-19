# UserDefinedFieldReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.user_defined_field_reference import UserDefinedFieldReference

# TODO update the JSON string below
json = "{}"
# create an instance of UserDefinedFieldReference from a JSON string
user_defined_field_reference_instance = UserDefinedFieldReference.from_json(json)
# print the JSON string representation of the object
print UserDefinedFieldReference.to_json()

# convert the object into a dict
user_defined_field_reference_dict = user_defined_field_reference_instance.to_dict()
# create an instance of UserDefinedFieldReference from a dict
user_defined_field_reference_form_dict = user_defined_field_reference.from_dict(user_defined_field_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


