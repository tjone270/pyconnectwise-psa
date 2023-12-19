# UnpostedPayments


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**a_r_payment_account** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**applied_by** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**invoice** | [**InvoiceReference**](InvoiceReference.md) |  | [optional] 
**payment_account** | **str** |  | [optional] 
**payment_date** | **str** |  | [optional] 
**payment_sync_date** | **str** |  | [optional] 
**payment_sync_status** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**wise_pay_payment** | [**WisePayPayment**](WisePayPayment.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.unposted_payments import UnpostedPayments

# TODO update the JSON string below
json = "{}"
# create an instance of UnpostedPayments from a JSON string
unposted_payments_instance = UnpostedPayments.from_json(json)
# print the JSON string representation of the object
print UnpostedPayments.to_json()

# convert the object into a dict
unposted_payments_dict = unposted_payments_instance.to_dict()
# create an instance of UnpostedPayments from a dict
unposted_payments_form_dict = unposted_payments.from_dict(unposted_payments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


