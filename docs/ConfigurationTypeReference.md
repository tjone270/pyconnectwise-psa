# ConfigurationTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.configuration_type_reference import ConfigurationTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationTypeReference from a JSON string
configuration_type_reference_instance = ConfigurationTypeReference.from_json(json)
# print the JSON string representation of the object
print ConfigurationTypeReference.to_json()

# convert the object into a dict
configuration_type_reference_dict = configuration_type_reference_instance.to_dict()
# create an instance of ConfigurationTypeReference from a dict
configuration_type_reference_form_dict = configuration_type_reference.from_dict(configuration_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


