# ManagedDevicesIntegrationInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**management_it_setup_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**solution** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.managed_devices_integration_info import ManagedDevicesIntegrationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedDevicesIntegrationInfo from a JSON string
managed_devices_integration_info_instance = ManagedDevicesIntegrationInfo.from_json(json)
# print the JSON string representation of the object
print ManagedDevicesIntegrationInfo.to_json()

# convert the object into a dict
managed_devices_integration_info_dict = managed_devices_integration_info_instance.to_dict()
# create an instance of ManagedDevicesIntegrationInfo from a dict
managed_devices_integration_info_form_dict = managed_devices_integration_info.from_dict(managed_devices_integration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


