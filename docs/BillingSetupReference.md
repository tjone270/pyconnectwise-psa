# BillingSetupReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.billing_setup_reference import BillingSetupReference

# TODO update the JSON string below
json = "{}"
# create an instance of BillingSetupReference from a JSON string
billing_setup_reference_instance = BillingSetupReference.from_json(json)
# print the JSON string representation of the object
print BillingSetupReference.to_json()

# convert the object into a dict
billing_setup_reference_dict = billing_setup_reference_instance.to_dict()
# create an instance of BillingSetupReference from a dict
billing_setup_reference_form_dict = billing_setup_reference.from_dict(billing_setup_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


