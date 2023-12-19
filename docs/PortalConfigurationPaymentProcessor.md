# PortalConfigurationPaymentProcessor


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**test_url** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.portal_configuration_payment_processor import PortalConfigurationPaymentProcessor

# TODO update the JSON string below
json = "{}"
# create an instance of PortalConfigurationPaymentProcessor from a JSON string
portal_configuration_payment_processor_instance = PortalConfigurationPaymentProcessor.from_json(json)
# print the JSON string representation of the object
print PortalConfigurationPaymentProcessor.to_json()

# convert the object into a dict
portal_configuration_payment_processor_dict = portal_configuration_payment_processor_instance.to_dict()
# create an instance of PortalConfigurationPaymentProcessor from a dict
portal_configuration_payment_processor_form_dict = portal_configuration_payment_processor.from_dict(portal_configuration_payment_processor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


