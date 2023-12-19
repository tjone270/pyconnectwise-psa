# InvoiceTemplateDetailReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.invoice_template_detail_reference import InvoiceTemplateDetailReference

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceTemplateDetailReference from a JSON string
invoice_template_detail_reference_instance = InvoiceTemplateDetailReference.from_json(json)
# print the JSON string representation of the object
print InvoiceTemplateDetailReference.to_json()

# convert the object into a dict
invoice_template_detail_reference_dict = invoice_template_detail_reference_instance.to_dict()
# create an instance of InvoiceTemplateDetailReference from a dict
invoice_template_detail_reference_form_dict = invoice_template_detail_reference.from_dict(invoice_template_detail_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


