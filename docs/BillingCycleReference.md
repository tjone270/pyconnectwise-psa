# BillingCycleReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.billing_cycle_reference import BillingCycleReference

# TODO update the JSON string below
json = "{}"
# create an instance of BillingCycleReference from a JSON string
billing_cycle_reference_instance = BillingCycleReference.from_json(json)
# print the JSON string representation of the object
print BillingCycleReference.to_json()

# convert the object into a dict
billing_cycle_reference_dict = billing_cycle_reference_instance.to_dict()
# create an instance of BillingCycleReference from a dict
billing_cycle_reference_form_dict = billing_cycle_reference.from_dict(billing_cycle_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


