# AgreementWorkType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement** | [**AgreementReference**](AgreementReference.md) |  | [optional] 
**agreement_id** | **int** |  | [optional] 
**agreement_limit** | **float** |  | [optional] 
**bill_time** | **str** |  | 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**effective_date** | **datetime** |  | [optional] 
**ending_date** | **datetime** |  | [optional] 
**hours_max** | **float** |  | [optional] 
**hours_min** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**location** | [**OwnerLevelReference**](OwnerLevelReference.md) |  | [optional] 
**location_id** | **int** |  | [optional] 
**overage_rate** | **float** |  | [optional] 
**overage_rate_type** | **str** |  | [optional] 
**rate** | **float** |  | [optional] 
**rate_type** | **str** |  | 
**round_bill_hours** | **float** |  | [optional] 
**site** | [**SiteReference**](SiteReference.md) |  | [optional] 
**work_type** | [**WorkTypeReference**](WorkTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_work_type import AgreementWorkType

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementWorkType from a JSON string
agreement_work_type_instance = AgreementWorkType.from_json(json)
# print the JSON string representation of the object
print AgreementWorkType.to_json()

# convert the object into a dict
agreement_work_type_dict = agreement_work_type_instance.to_dict()
# create an instance of AgreementWorkType from a dict
agreement_work_type_form_dict = agreement_work_type.from_dict(agreement_work_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


