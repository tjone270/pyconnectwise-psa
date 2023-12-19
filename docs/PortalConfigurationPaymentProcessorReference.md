# PortalConfigurationPaymentProcessorReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.portal_configuration_payment_processor_reference import PortalConfigurationPaymentProcessorReference

# TODO update the JSON string below
json = "{}"
# create an instance of PortalConfigurationPaymentProcessorReference from a JSON string
portal_configuration_payment_processor_reference_instance = PortalConfigurationPaymentProcessorReference.from_json(json)
# print the JSON string representation of the object
print PortalConfigurationPaymentProcessorReference.to_json()

# convert the object into a dict
portal_configuration_payment_processor_reference_dict = portal_configuration_payment_processor_reference_instance.to_dict()
# create an instance of PortalConfigurationPaymentProcessorReference from a dict
portal_configuration_payment_processor_reference_form_dict = portal_configuration_payment_processor_reference.from_dict(portal_configuration_payment_processor_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


