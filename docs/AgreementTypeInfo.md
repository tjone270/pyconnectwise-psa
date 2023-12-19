# AgreementTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**application_units** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_type_info import AgreementTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementTypeInfo from a JSON string
agreement_type_info_instance = AgreementTypeInfo.from_json(json)
# print the JSON string representation of the object
print AgreementTypeInfo.to_json()

# convert the object into a dict
agreement_type_info_dict = agreement_type_info_instance.to_dict()
# create an instance of AgreementTypeInfo from a dict
agreement_type_info_form_dict = agreement_type_info.from_dict(agreement_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


