# ManagedDevicesIntegration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**config_bill_customer_flag** | **bool** |  | [optional] 
**default_billing_level** | **str** |  | 
**default_department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**default_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**disable_new_cross_references_flag** | **bool** |  | [optional] 
**global_login_password** | **str** | Gets or sets             this is only required when globalLoginFlag &#x3D; true. Max length: 50; | [optional] 
**global_login_username** | **str** | Gets or sets             this is only required when globalLoginFlag &#x3D; true. Max length: 50; | [optional] 
**id** | **int** |  | [optional] 
**integrator_login** | [**IntegratorLoginReference**](IntegratorLoginReference.md) |  | [optional] 
**login_by** | **str** |  | 
**management_it_setup_type** | **str** |  | [optional] 
**match_on_serial_number_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 30; | 
**portal_url** | **str** |  Max length: 200; | [optional] 
**solution** | **str** |  Max length: 30; | 

## Example

```python
from connectwise_psa.models.managed_devices_integration import ManagedDevicesIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedDevicesIntegration from a JSON string
managed_devices_integration_instance = ManagedDevicesIntegration.from_json(json)
# print the JSON string representation of the object
print ManagedDevicesIntegration.to_json()

# convert the object into a dict
managed_devices_integration_dict = managed_devices_integration_instance.to_dict()
# create an instance of ManagedDevicesIntegration from a dict
managed_devices_integration_form_dict = managed_devices_integration.from_dict(managed_devices_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


