# ConfigurationTypeCopy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.configuration_type_copy import ConfigurationTypeCopy

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationTypeCopy from a JSON string
configuration_type_copy_instance = ConfigurationTypeCopy.from_json(json)
# print the JSON string representation of the object
print ConfigurationTypeCopy.to_json()

# convert the object into a dict
configuration_type_copy_dict = configuration_type_copy_instance.to_dict()
# create an instance of ConfigurationTypeCopy from a dict
configuration_type_copy_form_dict = configuration_type_copy.from_dict(configuration_type_copy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


