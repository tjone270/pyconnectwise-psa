# ManagedDevicesIntegrationLogin


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**managed_devices_integration** | [**ManagedDevicesIntegrationReference**](ManagedDevicesIntegrationReference.md) |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**password** | **str** |  Max length: 50; | [optional] 
**username** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.managed_devices_integration_login import ManagedDevicesIntegrationLogin

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedDevicesIntegrationLogin from a JSON string
managed_devices_integration_login_instance = ManagedDevicesIntegrationLogin.from_json(json)
# print the JSON string representation of the object
print ManagedDevicesIntegrationLogin.to_json()

# convert the object into a dict
managed_devices_integration_login_dict = managed_devices_integration_login_instance.to_dict()
# create an instance of ManagedDevicesIntegrationLogin from a dict
managed_devices_integration_login_form_dict = managed_devices_integration_login.from_dict(managed_devices_integration_login_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


