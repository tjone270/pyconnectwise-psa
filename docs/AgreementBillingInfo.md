# AgreementBillingInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agreement_amount** | **float** |  | [optional] 
**agreement_name** | **str** |  | [optional] 
**agreement_rec_id** | **int** |  | [optional] 
**agreement_type** | **str** |  | [optional] 
**parent_rec_id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_billing_info import AgreementBillingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementBillingInfo from a JSON string
agreement_billing_info_instance = AgreementBillingInfo.from_json(json)
# print the JSON string representation of the object
print AgreementBillingInfo.to_json()

# convert the object into a dict
agreement_billing_info_dict = agreement_billing_info_instance.to_dict()
# create an instance of AgreementBillingInfo from a dict
agreement_billing_info_form_dict = agreement_billing_info.from_dict(agreement_billing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


