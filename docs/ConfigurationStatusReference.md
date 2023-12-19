# ConfigurationStatusReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.configuration_status_reference import ConfigurationStatusReference

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationStatusReference from a JSON string
configuration_status_reference_instance = ConfigurationStatusReference.from_json(json)
# print the JSON string representation of the object
print ConfigurationStatusReference.to_json()

# convert the object into a dict
configuration_status_reference_dict = configuration_status_reference_instance.to_dict()
# create an instance of ConfigurationStatusReference from a dict
configuration_status_reference_form_dict = configuration_status_reference.from_dict(configuration_status_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


