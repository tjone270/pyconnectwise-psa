# AgreementTypeWorkRole


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**effective_date** | **datetime** |  | [optional] 
**ending_date** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**limit_to** | **float** |  | [optional] 
**rate** | **float** |  | [optional] 
**rate_type** | **str** |  | 
**type** | [**AgreementTypeReference**](AgreementTypeReference.md) |  | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_type_work_role import AgreementTypeWorkRole

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementTypeWorkRole from a JSON string
agreement_type_work_role_instance = AgreementTypeWorkRole.from_json(json)
# print the JSON string representation of the object
print AgreementTypeWorkRole.to_json()

# convert the object into a dict
agreement_type_work_role_dict = agreement_type_work_role_instance.to_dict()
# create an instance of AgreementTypeWorkRole from a dict
agreement_type_work_role_form_dict = agreement_type_work_role.from_dict(agreement_type_work_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


