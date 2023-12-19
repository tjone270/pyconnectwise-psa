# BillingTerm


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**due_days** | **int** |  | 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**terms_xref** | **str** |  Max length: 50; | [optional] 

## Example

```python
from connectwise_psa.models.billing_term import BillingTerm

# TODO update the JSON string below
json = "{}"
# create an instance of BillingTerm from a JSON string
billing_term_instance = BillingTerm.from_json(json)
# print the JSON string representation of the object
print BillingTerm.to_json()

# convert the object into a dict
billing_term_dict = billing_term_instance.to_dict()
# create an instance of BillingTerm from a dict
billing_term_form_dict = billing_term.from_dict(billing_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


