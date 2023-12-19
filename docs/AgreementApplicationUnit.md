# AgreementApplicationUnit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_application_unit import AgreementApplicationUnit

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementApplicationUnit from a JSON string
agreement_application_unit_instance = AgreementApplicationUnit.from_json(json)
# print the JSON string representation of the object
print AgreementApplicationUnit.to_json()

# convert the object into a dict
agreement_application_unit_dict = agreement_application_unit_instance.to_dict()
# create an instance of AgreementApplicationUnit from a dict
agreement_application_unit_form_dict = agreement_application_unit.from_dict(agreement_application_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


