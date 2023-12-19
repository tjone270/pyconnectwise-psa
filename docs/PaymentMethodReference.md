# PaymentMethodReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.payment_method_reference import PaymentMethodReference

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodReference from a JSON string
payment_method_reference_instance = PaymentMethodReference.from_json(json)
# print the JSON string representation of the object
print PaymentMethodReference.to_json()

# convert the object into a dict
payment_method_reference_dict = payment_method_reference_instance.to_dict()
# create an instance of PaymentMethodReference from a dict
payment_method_reference_form_dict = payment_method_reference.from_dict(payment_method_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


