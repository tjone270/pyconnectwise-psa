# WisePayBatchPayment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**wise_pay_href** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.wise_pay_batch_payment import WisePayBatchPayment

# TODO update the JSON string below
json = "{}"
# create an instance of WisePayBatchPayment from a JSON string
wise_pay_batch_payment_instance = WisePayBatchPayment.from_json(json)
# print the JSON string representation of the object
print WisePayBatchPayment.to_json()

# convert the object into a dict
wise_pay_batch_payment_dict = wise_pay_batch_payment_instance.to_dict()
# create an instance of WisePayBatchPayment from a dict
wise_pay_batch_payment_form_dict = wise_pay_batch_payment.from_dict(wise_pay_batch_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


