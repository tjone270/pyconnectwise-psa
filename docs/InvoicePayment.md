# InvoicePayment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**a_r_payment_account** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**applied_by** | **str** |  | [optional] 
**credit** | [**InvoiceReference**](InvoiceReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**invoice** | [**InvoiceReference**](InvoiceReference.md) |  | [optional] 
**payment_account** | **str** |  | [optional] 
**payment_date** | **datetime** |  | [optional] 
**payment_sync_date** | **str** |  | [optional] 
**payment_sync_status** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**wise_pay_payment** | [**WisePayPayment**](WisePayPayment.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.invoice_payment import InvoicePayment

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicePayment from a JSON string
invoice_payment_instance = InvoicePayment.from_json(json)
# print the JSON string representation of the object
print InvoicePayment.to_json()

# convert the object into a dict
invoice_payment_dict = invoice_payment_instance.to_dict()
# create an instance of InvoicePayment from a dict
invoice_payment_form_dict = invoice_payment.from_dict(invoice_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


