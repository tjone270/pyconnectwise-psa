# ManagementItSolutionAgreementInterfaceParameter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement_type** | [**AgreementTypeReference**](AgreementTypeReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**managed_devices_integration** | [**ManagedDevicesIntegrationReference**](ManagedDevicesIntegrationReference.md) |  | [optional] 
**server_product** | [**IvItemReference**](IvItemReference.md) |  | [optional] 
**spam_stats_product** | [**IvItemReference**](IvItemReference.md) |  | [optional] 
**workstation_product** | [**IvItemReference**](IvItemReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.management_it_solution_agreement_interface_parameter import ManagementItSolutionAgreementInterfaceParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ManagementItSolutionAgreementInterfaceParameter from a JSON string
management_it_solution_agreement_interface_parameter_instance = ManagementItSolutionAgreementInterfaceParameter.from_json(json)
# print the JSON string representation of the object
print ManagementItSolutionAgreementInterfaceParameter.to_json()

# convert the object into a dict
management_it_solution_agreement_interface_parameter_dict = management_it_solution_agreement_interface_parameter_instance.to_dict()
# create an instance of ManagementItSolutionAgreementInterfaceParameter from a dict
management_it_solution_agreement_interface_parameter_form_dict = management_it_solution_agreement_interface_parameter.from_dict(management_it_solution_agreement_interface_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


