# AgreementAdjustment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement_id** | **int** |  | [optional] 
**amount** | **float** |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**description** | **str** |  Max length: 1000; | [optional] 
**effective_date** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_adjustment import AgreementAdjustment

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementAdjustment from a JSON string
agreement_adjustment_instance = AgreementAdjustment.from_json(json)
# print the JSON string representation of the object
print AgreementAdjustment.to_json()

# convert the object into a dict
agreement_adjustment_dict = agreement_adjustment_instance.to_dict()
# create an instance of AgreementAdjustment from a dict
agreement_adjustment_form_dict = agreement_adjustment.from_dict(agreement_adjustment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


