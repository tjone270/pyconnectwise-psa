# ManagedDeviceAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**managed_devices_integration** | [**ManagedDevicesIntegrationReference**](ManagedDevicesIntegrationReference.md) |  | [optional] 
**password** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.managed_device_account import ManagedDeviceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedDeviceAccount from a JSON string
managed_device_account_instance = ManagedDeviceAccount.from_json(json)
# print the JSON string representation of the object
print ManagedDeviceAccount.to_json()

# convert the object into a dict
managed_device_account_dict = managed_device_account_instance.to_dict()
# create an instance of ManagedDeviceAccount from a dict
managed_device_account_form_dict = managed_device_account.from_dict(managed_device_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


