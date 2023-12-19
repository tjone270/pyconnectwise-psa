# InvoiceEmailTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**attach_invoice_flag** | **bool** |  | [optional] 
**body** | **str** |  | [optional] 
**copy_sender_flag** | **bool** |  | [optional] 
**email_address** | **str** | From fields (first name, last name, email address) are required if useSenderFlag is false. Max length: 100; | [optional] 
**first_name** | **str** | From fields (first name, last name, email address) are required if useSenderFlag is false. Max length: 100; | [optional] 
**id** | **int** |  | [optional] 
**invoice_status** | [**BillingStatusReference**](BillingStatusReference.md) |  | [optional] 
**last_name** | **str** | From fields (first name, last name, email address) are required if useSenderFlag is false. Max length: 100; | [optional] 
**name** | **str** |  Max length: 50; | 
**service_survey** | [**ServiceSurveyReference**](ServiceSurveyReference.md) |  | [optional] 
**subject** | **str** |  Max length: 200; | 
**use_sender_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.invoice_email_template import InvoiceEmailTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceEmailTemplate from a JSON string
invoice_email_template_instance = InvoiceEmailTemplate.from_json(json)
# print the JSON string representation of the object
print InvoiceEmailTemplate.to_json()

# convert the object into a dict
invoice_email_template_dict = invoice_email_template_instance.to_dict()
# create an instance of InvoiceEmailTemplate from a dict
invoice_email_template_form_dict = invoice_email_template.from_dict(invoice_email_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


