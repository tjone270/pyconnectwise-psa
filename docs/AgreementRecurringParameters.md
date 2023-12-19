# AgreementRecurringParameters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_gr_amount** | **float** |  | [optional] 
**a_gr_prorate** | **float** |  | [optional] 
**additions_amount** | **float** |  | [optional] 
**auto_invoice_flag** | **bool** |  | [optional] 
**bill_start_date** | **str** |  | [optional] 
**billing_cycle** | [**GenericNameIdDTO**](GenericNameIdDTO.md) |  | [optional] 
**children_amount** | **float** |  | [optional] 
**currency** | [**GenericNameIdDTO**](GenericNameIdDTO.md) |  | [optional] 
**cycle_base** | [**GenericNameIdDTO**](GenericNameIdDTO.md) |  | [optional] 
**invoice_prorated_additions_flag** | **bool** |  | [optional] 
**prorate_flag** | **bool** |  | [optional] 
**restrict_downpayment** | **bool** |  | [optional] 
**tax_code** | [**GenericNameIdDTO**](GenericNameIdDTO.md) |  | [optional] 
**taxable** | **bool** |  | [optional] 
**terms** | [**GenericNameIdDTO**](GenericNameIdDTO.md) |  | [optional] 
**total_amount** | **float** |  | [optional] 
**user_defined_field_values** | [**List[UserDefinedFieldValueModel]**](UserDefinedFieldValueModel.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_recurring_parameters import AgreementRecurringParameters

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementRecurringParameters from a JSON string
agreement_recurring_parameters_instance = AgreementRecurringParameters.from_json(json)
# print the JSON string representation of the object
print AgreementRecurringParameters.to_json()

# convert the object into a dict
agreement_recurring_parameters_dict = agreement_recurring_parameters_instance.to_dict()
# create an instance of AgreementRecurringParameters from a dict
agreement_recurring_parameters_form_dict = agreement_recurring_parameters.from_dict(agreement_recurring_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


