# AgreementWorkRoleExclusion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement_id** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_work_role_exclusion import AgreementWorkRoleExclusion

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementWorkRoleExclusion from a JSON string
agreement_work_role_exclusion_instance = AgreementWorkRoleExclusion.from_json(json)
# print the JSON string representation of the object
print AgreementWorkRoleExclusion.to_json()

# convert the object into a dict
agreement_work_role_exclusion_dict = agreement_work_role_exclusion_instance.to_dict()
# create an instance of AgreementWorkRoleExclusion from a dict
agreement_work_role_exclusion_form_dict = agreement_work_role_exclusion.from_dict(agreement_work_role_exclusion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


