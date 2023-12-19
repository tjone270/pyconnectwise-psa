# InvoiceReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**apply_to_type** | **str** |  | [optional] 
**billing_type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.invoice_reference import InvoiceReference

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceReference from a JSON string
invoice_reference_instance = InvoiceReference.from_json(json)
# print the JSON string representation of the object
print InvoiceReference.to_json()

# convert the object into a dict
invoice_reference_dict = invoice_reference_instance.to_dict()
# create an instance of InvoiceReference from a dict
invoice_reference_form_dict = invoice_reference.from_dict(invoice_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


