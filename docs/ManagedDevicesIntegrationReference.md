# ManagedDevicesIntegrationReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.managed_devices_integration_reference import ManagedDevicesIntegrationReference

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedDevicesIntegrationReference from a JSON string
managed_devices_integration_reference_instance = ManagedDevicesIntegrationReference.from_json(json)
# print the JSON string representation of the object
print ManagedDevicesIntegrationReference.to_json()

# convert the object into a dict
managed_devices_integration_reference_dict = managed_devices_integration_reference_instance.to_dict()
# create an instance of ManagedDevicesIntegrationReference from a dict
managed_devices_integration_reference_form_dict = managed_devices_integration_reference.from_dict(managed_devices_integration_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


