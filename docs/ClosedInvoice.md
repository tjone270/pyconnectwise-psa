# ClosedInvoice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**internal_notes** | **str** |  | [optional] 
**status** | [**BillingStatusReference**](BillingStatusReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.closed_invoice import ClosedInvoice

# TODO update the JSON string below
json = "{}"
# create an instance of ClosedInvoice from a JSON string
closed_invoice_instance = ClosedInvoice.from_json(json)
# print the JSON string representation of the object
print ClosedInvoice.to_json()

# convert the object into a dict
closed_invoice_dict = closed_invoice_instance.to_dict()
# create an instance of ClosedInvoice from a dict
closed_invoice_form_dict = closed_invoice.from_dict(closed_invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


