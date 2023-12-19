# PortalConfigurationInvoiceSetup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**add_all_statuses** | **bool** |  | [optional] 
**allow_inv_pmt_flag** | **bool** |  | [optional] 
**billing_status_ids** | **List[int]** |  | [optional] 
**display_inv_pmt_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**login** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**payment_processor** | [**PortalConfigurationPaymentProcessorReference**](PortalConfigurationPaymentProcessorReference.md) |  | [optional] 
**portal_configuration** | [**PortalConfigurationReference**](PortalConfigurationReference.md) |  | [optional] 
**remove_all_statuses** | **bool** |  | [optional] 
**url_override** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.portal_configuration_invoice_setup import PortalConfigurationInvoiceSetup

# TODO update the JSON string below
json = "{}"
# create an instance of PortalConfigurationInvoiceSetup from a JSON string
portal_configuration_invoice_setup_instance = PortalConfigurationInvoiceSetup.from_json(json)
# print the JSON string representation of the object
print PortalConfigurationInvoiceSetup.to_json()

# convert the object into a dict
portal_configuration_invoice_setup_dict = portal_configuration_invoice_setup_instance.to_dict()
# create an instance of PortalConfigurationInvoiceSetup from a dict
portal_configuration_invoice_setup_form_dict = portal_configuration_invoice_setup.from_dict(portal_configuration_invoice_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


