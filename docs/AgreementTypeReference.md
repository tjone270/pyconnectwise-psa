# AgreementTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_type_reference import AgreementTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementTypeReference from a JSON string
agreement_type_reference_instance = AgreementTypeReference.from_json(json)
# print the JSON string representation of the object
print AgreementTypeReference.to_json()

# convert the object into a dict
agreement_type_reference_dict = agreement_type_reference_instance.to_dict()
# create an instance of AgreementTypeReference from a dict
agreement_type_reference_form_dict = agreement_type_reference.from_dict(agreement_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


