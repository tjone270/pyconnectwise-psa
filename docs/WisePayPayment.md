# WisePayPayment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_payment** | [**WisePayBatchPayment**](WisePayBatchPayment.md) |  | [optional] 
**fee_invoice** | [**WisePayFeeInvoice**](WisePayFeeInvoice.md) |  | [optional] 
**payment_date_utc** | **str** |  | [optional] 
**wise_pay_reference** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.wise_pay_payment import WisePayPayment

# TODO update the JSON string below
json = "{}"
# create an instance of WisePayPayment from a JSON string
wise_pay_payment_instance = WisePayPayment.from_json(json)
# print the JSON string representation of the object
print WisePayPayment.to_json()

# convert the object into a dict
wise_pay_payment_dict = wise_pay_payment_instance.to_dict()
# create an instance of WisePayPayment from a dict
wise_pay_payment_form_dict = wise_pay_payment.from_dict(wise_pay_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


