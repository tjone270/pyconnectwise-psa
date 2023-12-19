# AgreementBatchSetup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**days_in_advance** | **int** |  | 
**id** | **int** |  | [optional] 
**next_run_date** | **datetime** |  | 

## Example

```python
from connectwise_psa.models.agreement_batch_setup import AgreementBatchSetup

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementBatchSetup from a JSON string
agreement_batch_setup_instance = AgreementBatchSetup.from_json(json)
# print the JSON string representation of the object
print AgreementBatchSetup.to_json()

# convert the object into a dict
agreement_batch_setup_dict = agreement_batch_setup_instance.to_dict()
# create an instance of AgreementBatchSetup from a dict
agreement_batch_setup_form_dict = agreement_batch_setup.from_dict(agreement_batch_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


