# ServiceEmailTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**body** | **str** |  | [optional] 
**copy_sender_flag** | **bool** |  | [optional] 
**email_address** | **str** | From fields (first name, last name, email address) are required if useSenderFlag is false. Max length: 100; | [optional] 
**external_contact_notifications** | **bool** |  | [optional] 
**first_name** | **str** | From fields (first name, last name, email address) are required if useSenderFlag is false. Max length: 100; | [optional] 
**id** | **int** |  | [optional] 
**internal_contact_notifications** | **bool** |  | [optional] 
**last_name** | **str** | From fields (first name, last name, email address) are required if useSenderFlag is false. Max length: 100; | [optional] 
**resource_records_flag** | **bool** |  | [optional] 
**service_board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**service_status** | [**ServiceStatusReference**](ServiceStatusReference.md) |  | [optional] 
**service_survey** | [**ServiceSurveyReference**](ServiceSurveyReference.md) |  | [optional] 
**subject** | **str** |  Max length: 200; | [optional] 
**tasks_flag** | **bool** |  | [optional] 
**type** | **str** |  | 
**use_sender_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.service_email_template import ServiceEmailTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceEmailTemplate from a JSON string
service_email_template_instance = ServiceEmailTemplate.from_json(json)
# print the JSON string representation of the object
print ServiceEmailTemplate.to_json()

# convert the object into a dict
service_email_template_dict = service_email_template_instance.to_dict()
# create an instance of ServiceEmailTemplate from a dict
service_email_template_form_dict = service_email_template.from_dict(service_email_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


