# ConfigurationReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**device_identifier** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.configuration_reference import ConfigurationReference

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationReference from a JSON string
configuration_reference_instance = ConfigurationReference.from_json(json)
# print the JSON string representation of the object
print ConfigurationReference.to_json()

# convert the object into a dict
configuration_reference_dict = configuration_reference_instance.to_dict()
# create an instance of ConfigurationReference from a dict
configuration_reference_form_dict = configuration_reference.from_dict(configuration_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


