# ConfigurationStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**closed_flag** | **bool** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**description** | **str** |  Max length: 50; | 
**id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.configuration_status import ConfigurationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationStatus from a JSON string
configuration_status_instance = ConfigurationStatus.from_json(json)
# print the JSON string representation of the object
print ConfigurationStatus.to_json()

# convert the object into a dict
configuration_status_dict = configuration_status_instance.to_dict()
# create an instance of ConfigurationStatus from a dict
configuration_status_form_dict = configuration_status.from_dict(configuration_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


