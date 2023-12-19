# BillingTermInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.billing_term_info import BillingTermInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BillingTermInfo from a JSON string
billing_term_info_instance = BillingTermInfo.from_json(json)
# print the JSON string representation of the object
print BillingTermInfo.to_json()

# convert the object into a dict
billing_term_info_dict = billing_term_info_instance.to_dict()
# create an instance of BillingTermInfo from a dict
billing_term_info_form_dict = billing_term_info.from_dict(billing_term_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


