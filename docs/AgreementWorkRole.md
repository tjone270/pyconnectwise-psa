# AgreementWorkRole


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement** | [**AgreementReference**](AgreementReference.md) |  | [optional] 
**agreement_id** | **int** |  | [optional] 
**effective_date** | **datetime** |  | [optional] 
**ending_date** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**limit_to** | **float** |  | [optional] 
**location** | [**OwnerLevelReference**](OwnerLevelReference.md) |  | [optional] 
**location_id** | **int** |  | [optional] 
**rate** | **float** |  | [optional] 
**rate_type** | **str** |  | 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_work_role import AgreementWorkRole

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementWorkRole from a JSON string
agreement_work_role_instance = AgreementWorkRole.from_json(json)
# print the JSON string representation of the object
print AgreementWorkRole.to_json()

# convert the object into a dict
agreement_work_role_dict = agreement_work_role_instance.to_dict()
# create an instance of AgreementWorkRole from a dict
agreement_work_role_form_dict = agreement_work_role.from_dict(agreement_work_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


