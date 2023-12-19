# BillingCycle


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**billing_options** | **str** |  | 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  Max length: 5; | 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.billing_cycle import BillingCycle

# TODO update the JSON string below
json = "{}"
# create an instance of BillingCycle from a JSON string
billing_cycle_instance = BillingCycle.from_json(json)
# print the JSON string representation of the object
print BillingCycle.to_json()

# convert the object into a dict
billing_cycle_dict = billing_cycle_instance.to_dict()
# create an instance of BillingCycle from a dict
billing_cycle_form_dict = billing_cycle.from_dict(billing_cycle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


