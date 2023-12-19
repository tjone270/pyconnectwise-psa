# InvoiceEmailTemplateInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.invoice_email_template_info import InvoiceEmailTemplateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceEmailTemplateInfo from a JSON string
invoice_email_template_info_instance = InvoiceEmailTemplateInfo.from_json(json)
# print the JSON string representation of the object
print InvoiceEmailTemplateInfo.to_json()

# convert the object into a dict
invoice_email_template_info_dict = invoice_email_template_info_instance.to_dict()
# create an instance of InvoiceEmailTemplateInfo from a dict
invoice_email_template_info_form_dict = invoice_email_template_info.from_dict(invoice_email_template_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


