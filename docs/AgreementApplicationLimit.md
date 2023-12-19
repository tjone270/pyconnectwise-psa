# AgreementApplicationLimit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_application_limit import AgreementApplicationLimit

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementApplicationLimit from a JSON string
agreement_application_limit_instance = AgreementApplicationLimit.from_json(json)
# print the JSON string representation of the object
print AgreementApplicationLimit.to_json()

# convert the object into a dict
agreement_application_limit_dict = agreement_application_limit_instance.to_dict()
# create an instance of AgreementApplicationLimit from a dict
agreement_application_limit_form_dict = agreement_application_limit.from_dict(agreement_application_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


