# AgreementTypeWorkType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**bill_time** | **str** |  | 
**effective_date** | **datetime** |  | [optional] 
**ending_date** | **datetime** |  | [optional] 
**hours_max** | **float** |  | [optional] 
**hours_min** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**limit_to** | **float** |  | [optional] 
**overage_rate** | **float** |  | [optional] 
**overage_rate_type** | **str** |  | 
**rate** | **float** |  | [optional] 
**rate_type** | **str** |  | 
**round_bill_hours** | **float** |  | [optional] 
**type** | [**AgreementTypeReference**](AgreementTypeReference.md) |  | [optional] 
**work_type** | [**WorkTypeReference**](WorkTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_type_work_type import AgreementTypeWorkType

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementTypeWorkType from a JSON string
agreement_type_work_type_instance = AgreementTypeWorkType.from_json(json)
# print the JSON string representation of the object
print AgreementTypeWorkType.to_json()

# convert the object into a dict
agreement_type_work_type_dict = agreement_type_work_type_instance.to_dict()
# create an instance of AgreementTypeWorkType from a dict
agreement_type_work_type_form_dict = agreement_type_work_type.from_dict(agreement_type_work_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


