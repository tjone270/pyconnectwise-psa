# BillingSetupRouting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**invoice_rule** | **str** |  | 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**routing_rule** | **str** |  | 
**sequence_number** | **int** |  | 

## Example

```python
from connectwise_psa.models.billing_setup_routing import BillingSetupRouting

# TODO update the JSON string below
json = "{}"
# create an instance of BillingSetupRouting from a JSON string
billing_setup_routing_instance = BillingSetupRouting.from_json(json)
# print the JSON string representation of the object
print BillingSetupRouting.to_json()

# convert the object into a dict
billing_setup_routing_dict = billing_setup_routing_instance.to_dict()
# create an instance of BillingSetupRouting from a dict
billing_setup_routing_form_dict = billing_setup_routing.from_dict(billing_setup_routing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


