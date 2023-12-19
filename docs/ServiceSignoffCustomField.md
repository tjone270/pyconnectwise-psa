# ServiceSignoffCustomField


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**display_section** | **str** |  | 
**id** | **int** |  | [optional] 
**sequence_number** | **float** |  | 
**user_defined_field** | [**UserDefinedFieldReference**](UserDefinedFieldReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.service_signoff_custom_field import ServiceSignoffCustomField

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSignoffCustomField from a JSON string
service_signoff_custom_field_instance = ServiceSignoffCustomField.from_json(json)
# print the JSON string representation of the object
print ServiceSignoffCustomField.to_json()

# convert the object into a dict
service_signoff_custom_field_dict = service_signoff_custom_field_instance.to_dict()
# create an instance of ServiceSignoffCustomField from a dict
service_signoff_custom_field_form_dict = service_signoff_custom_field.from_dict(service_signoff_custom_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


