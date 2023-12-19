# AgreementApplicationParameters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agr_billing_cycle** | [**AgreementApplicationBillingCycle**](AgreementApplicationBillingCycle.md) |  | [optional] 
**agreement_expires_flag** | **bool** |  | [optional] 
**allow_overruns_flag** | **bool** |  | [optional] 
**application_limit** | [**AgreementApplicationLimit**](AgreementApplicationLimit.md) |  | [optional] 
**application_limit_amount** | **float** |  | [optional] 
**application_unit** | [**AgreementApplicationUnit**](AgreementApplicationUnit.md) |  | [optional] 
**available_per** | [**AgreementApplicationAviablePer**](AgreementApplicationAviablePer.md) |  | [optional] 
**carry_over_days** | **int** |  | [optional] 
**carryover_unused_flag** | **bool** |  | [optional] 
**charge_adjustments_flag** | **bool** |  | [optional] 
**covers_expenses_flag** | **bool** |  | [optional] 
**covers_products_flag** | **bool** |  | [optional] 
**covers_tax_flag** | **bool** |  | [optional] 
**covers_time_flag** | **bool** |  | [optional] 
**overrun_limit** | **int** |  | [optional] 
**prepay_flag** | **bool** |  | [optional] 
**user_defined_field_values** | [**List[UserDefinedFieldValueModel]**](UserDefinedFieldValueModel.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_application_parameters import AgreementApplicationParameters

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementApplicationParameters from a JSON string
agreement_application_parameters_instance = AgreementApplicationParameters.from_json(json)
# print the JSON string representation of the object
print AgreementApplicationParameters.to_json()

# convert the object into a dict
agreement_application_parameters_dict = agreement_application_parameters_instance.to_dict()
# create an instance of AgreementApplicationParameters from a dict
agreement_application_parameters_form_dict = agreement_application_parameters.from_dict(agreement_application_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


