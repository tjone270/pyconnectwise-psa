# ConfigurationStatusInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**closed_flag** | **bool** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.configuration_status_info import ConfigurationStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationStatusInfo from a JSON string
configuration_status_info_instance = ConfigurationStatusInfo.from_json(json)
# print the JSON string representation of the object
print ConfigurationStatusInfo.to_json()

# convert the object into a dict
configuration_status_info_dict = configuration_status_info_instance.to_dict()
# create an instance of ConfigurationStatusInfo from a dict
configuration_status_info_form_dict = configuration_status_info.from_dict(configuration_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


