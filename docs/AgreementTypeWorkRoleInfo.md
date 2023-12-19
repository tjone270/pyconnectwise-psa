# AgreementTypeWorkRoleInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**type** | [**AgreementTypeReference**](AgreementTypeReference.md) |  | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_type_work_role_info import AgreementTypeWorkRoleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementTypeWorkRoleInfo from a JSON string
agreement_type_work_role_info_instance = AgreementTypeWorkRoleInfo.from_json(json)
# print the JSON string representation of the object
print AgreementTypeWorkRoleInfo.to_json()

# convert the object into a dict
agreement_type_work_role_info_dict = agreement_type_work_role_info_instance.to_dict()
# create an instance of AgreementTypeWorkRoleInfo from a dict
agreement_type_work_role_info_form_dict = agreement_type_work_role_info.from_dict(agreement_type_work_role_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


