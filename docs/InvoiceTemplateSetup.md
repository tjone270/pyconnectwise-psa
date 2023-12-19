# InvoiceTemplateSetup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**custom_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.invoice_template_setup import InvoiceTemplateSetup

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceTemplateSetup from a JSON string
invoice_template_setup_instance = InvoiceTemplateSetup.from_json(json)
# print the JSON string representation of the object
print InvoiceTemplateSetup.to_json()

# convert the object into a dict
invoice_template_setup_dict = invoice_template_setup_instance.to_dict()
# create an instance of InvoiceTemplateSetup from a dict
invoice_template_setup_form_dict = invoice_template_setup.from_dict(invoice_template_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


