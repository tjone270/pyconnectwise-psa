# WisePayFeeInvoice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**invoice_href** | **str** |  | [optional] 
**invoice_number** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.wise_pay_fee_invoice import WisePayFeeInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of WisePayFeeInvoice from a JSON string
wise_pay_fee_invoice_instance = WisePayFeeInvoice.from_json(json)
# print the JSON string representation of the object
print WisePayFeeInvoice.to_json()

# convert the object into a dict
wise_pay_fee_invoice_dict = wise_pay_fee_invoice_instance.to_dict()
# create an instance of WisePayFeeInvoice from a dict
wise_pay_fee_invoice_form_dict = wise_pay_fee_invoice.from_dict(wise_pay_fee_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


