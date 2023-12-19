# ManagedDevicesIntegrationCrossReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement_type** | [**AgreementTypeReference**](AgreementTypeReference.md) |  | [optional] 
**configuration_type** | [**ConfigurationTypeReference**](ConfigurationTypeReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**managed_devices_integration** | [**ManagedDevicesIntegrationReference**](ManagedDevicesIntegrationReference.md) |  | [optional] 
**product** | [**IvItemReference**](IvItemReference.md) |  | [optional] 
**vendor_level** | **str** |  Max length: 255; | [optional] 
**vendor_type** | **str** |  Max length: 255; | [optional] 

## Example

```python
from connectwise_psa.models.managed_devices_integration_cross_reference import ManagedDevicesIntegrationCrossReference

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedDevicesIntegrationCrossReference from a JSON string
managed_devices_integration_cross_reference_instance = ManagedDevicesIntegrationCrossReference.from_json(json)
# print the JSON string representation of the object
print ManagedDevicesIntegrationCrossReference.to_json()

# convert the object into a dict
managed_devices_integration_cross_reference_dict = managed_devices_integration_cross_reference_instance.to_dict()
# create an instance of ManagedDevicesIntegrationCrossReference from a dict
managed_devices_integration_cross_reference_form_dict = managed_devices_integration_cross_reference.from_dict(managed_devices_integration_cross_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


