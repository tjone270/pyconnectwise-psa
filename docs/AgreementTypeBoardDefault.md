# AgreementTypeBoardDefault


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | 
**service_type** | [**ServiceTypeReference**](ServiceTypeReference.md) |  | [optional] 
**type** | [**AgreementTypeReference**](AgreementTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_type_board_default import AgreementTypeBoardDefault

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementTypeBoardDefault from a JSON string
agreement_type_board_default_instance = AgreementTypeBoardDefault.from_json(json)
# print the JSON string representation of the object
print AgreementTypeBoardDefault.to_json()

# convert the object into a dict
agreement_type_board_default_dict = agreement_type_board_default_instance.to_dict()
# create an instance of AgreementTypeBoardDefault from a dict
agreement_type_board_default_form_dict = agreement_type_board_default.from_dict(agreement_type_board_default_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


