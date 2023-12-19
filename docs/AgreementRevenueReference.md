# AgreementRevenueReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**cost** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**margin** | **float** |  | [optional] 
**percentage** | **float** |  | [optional] 
**revenue** | **float** |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_revenue_reference import AgreementRevenueReference

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementRevenueReference from a JSON string
agreement_revenue_reference_instance = AgreementRevenueReference.from_json(json)
# print the JSON string representation of the object
print AgreementRevenueReference.to_json()

# convert the object into a dict
agreement_revenue_reference_dict = agreement_revenue_reference_instance.to_dict()
# create an instance of AgreementRevenueReference from a dict
agreement_revenue_reference_form_dict = agreement_revenue_reference.from_dict(agreement_revenue_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


