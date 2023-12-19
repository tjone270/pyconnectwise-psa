# AgreementReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_reference import AgreementReference

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementReference from a JSON string
agreement_reference_instance = AgreementReference.from_json(json)
# print the JSON string representation of the object
print AgreementReference.to_json()

# convert the object into a dict
agreement_reference_dict = agreement_reference_instance.to_dict()
# create an instance of AgreementReference from a dict
agreement_reference_form_dict = agreement_reference.from_dict(agreement_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


