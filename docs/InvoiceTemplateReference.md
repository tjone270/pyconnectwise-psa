# InvoiceTemplateReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** | Gets or sets invoice Template Setup Id. | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.invoice_template_reference import InvoiceTemplateReference

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceTemplateReference from a JSON string
invoice_template_reference_instance = InvoiceTemplateReference.from_json(json)
# print the JSON string representation of the object
print InvoiceTemplateReference.to_json()

# convert the object into a dict
invoice_template_reference_dict = invoice_template_reference_instance.to_dict()
# create an instance of InvoiceTemplateReference from a dict
invoice_template_reference_form_dict = invoice_template_reference.from_dict(invoice_template_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


