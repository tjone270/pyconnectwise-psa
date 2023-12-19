# ConfigurationType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**system_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.configuration_type import ConfigurationType

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationType from a JSON string
configuration_type_instance = ConfigurationType.from_json(json)
# print the JSON string representation of the object
print ConfigurationType.to_json()

# convert the object into a dict
configuration_type_dict = configuration_type_instance.to_dict()
# create an instance of ConfigurationType from a dict
configuration_type_form_dict = configuration_type.from_dict(configuration_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


