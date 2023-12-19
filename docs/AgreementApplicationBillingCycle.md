# AgreementApplicationBillingCycle


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_application_billing_cycle import AgreementApplicationBillingCycle

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementApplicationBillingCycle from a JSON string
agreement_application_billing_cycle_instance = AgreementApplicationBillingCycle.from_json(json)
# print the JSON string representation of the object
print AgreementApplicationBillingCycle.to_json()

# convert the object into a dict
agreement_application_billing_cycle_dict = agreement_application_billing_cycle_instance.to_dict()
# create an instance of AgreementApplicationBillingCycle from a dict
agreement_application_billing_cycle_form_dict = agreement_application_billing_cycle.from_dict(agreement_application_billing_cycle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


