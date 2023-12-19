# AgreementWorkTypeExclusion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**work_type** | [**WorkTypeReference**](WorkTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_work_type_exclusion import AgreementWorkTypeExclusion

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementWorkTypeExclusion from a JSON string
agreement_work_type_exclusion_instance = AgreementWorkTypeExclusion.from_json(json)
# print the JSON string representation of the object
print AgreementWorkTypeExclusion.to_json()

# convert the object into a dict
agreement_work_type_exclusion_dict = agreement_work_type_exclusion_instance.to_dict()
# create an instance of AgreementWorkTypeExclusion from a dict
agreement_work_type_exclusion_form_dict = agreement_work_type_exclusion.from_dict(agreement_work_type_exclusion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


