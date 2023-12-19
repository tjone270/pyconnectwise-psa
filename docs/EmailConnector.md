# EmailConnector


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**add_cc_flag** | **bool** |  | [optional] 
**asio365_email_setup** | [**Office365EmailSetupReference**](Office365EmailSetupReference.md) |  | [optional] 
**bcc_email_to** | **str** |  Max length: 250; | [optional] 
**create_contact_flag** | **bool** |  | [optional] 
**default_company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**default_member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**discard_duplicates_flag** | **bool** |  | [optional] 
**email_errors_to** | **str** |  Max length: 50; | 
**email_notify_from** | **str** |  Max length: 50; | [optional] 
**email_server_type** | **str** |  | [optional] 
**google_email_setup** | [**GoogleEmailSetupReference**](GoogleEmailSetupReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**imap_setup** | [**ImapSetupReference**](ImapSetupReference.md) |  | [optional] 
**inbound_ticket_mailbox_id** | **str** |  | [optional] 
**item_override** | [**ServiceItemReference**](ServiceItemReference.md) |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**never_respond_flag** | **bool** |  | [optional] 
**no_response_flag** | **bool** |  | [optional] 
**office365_email_setup** | [**Office365EmailSetupReference**](Office365EmailSetupReference.md) |  | [optional] 
**post_replies_to_ticket_flag** | **bool** |  | [optional] 
**priority_override** | [**PriorityReference**](PriorityReference.md) |  | [optional] 
**response_email_for_existing** | **str** |  | [optional] 
**response_email_for_new** | **str** |  | [optional] 
**service_board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**set_email_to_default_contact_flag** | **bool** |  | [optional] 
**source_override** | [**ServiceSourceReference**](ServiceSourceReference.md) |  | [optional] 
**status_override** | [**ServiceStatusReference**](ServiceStatusReference.md) |  | [optional] 
**sub_type_override** | [**ServiceSubTypeReference**](ServiceSubTypeReference.md) |  | [optional] 
**type_override** | [**ServiceTypeReference**](ServiceTypeReference.md) |  | [optional] 
**use_email_message_id_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.email_connector import EmailConnector

# TODO update the JSON string below
json = "{}"
# create an instance of EmailConnector from a JSON string
email_connector_instance = EmailConnector.from_json(json)
# print the JSON string representation of the object
print EmailConnector.to_json()

# convert the object into a dict
email_connector_dict = email_connector_instance.to_dict()
# create an instance of EmailConnector from a dict
email_connector_form_dict = email_connector.from_dict(email_connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


