# AgreementRecap


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustment_amount** | **float** |  | [optional] 
**agreement_status** | **str** |  | [optional] 
**available_amount** | **float** |  | [optional] 
**company_name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**is_unlimited** | **str** |  | [optional] 
**last_invoice_amount** | **str** |  | [optional] 
**last_invoice_date** | **str** |  | [optional] 
**last_invoice_number** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**next_invoice_amount** | **float** |  | [optional] 
**next_invoice_date** | **str** |  | [optional] 
**overrun_amount** | **float** |  | [optional] 
**remaining_amount** | **float** |  | [optional] 
**starting_amount** | **float** |  | [optional] 
**unbilled_overage_amount** | **float** |  | [optional] 
**unbilled_periods** | **int** |  | [optional] 
**used_amount** | **float** |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_recap import AgreementRecap

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementRecap from a JSON string
agreement_recap_instance = AgreementRecap.from_json(json)
# print the JSON string representation of the object
print AgreementRecap.to_json()

# convert the object into a dict
agreement_recap_dict = agreement_recap_instance.to_dict()
# create an instance of AgreementRecap from a dict
agreement_recap_form_dict = agreement_recap.from_dict(agreement_recap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


