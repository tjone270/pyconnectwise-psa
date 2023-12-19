# NotificationRecipient


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement_flag** | **bool** |  | [optional] 
**config_flag** | **bool** |  | [optional] 
**external_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**invoice_flag** | **bool** |  | [optional] 
**knowledge_base_flag** | **bool** |  | [optional] 
**member_flag** | **bool** |  | [optional] 
**msp_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**procurement_flag** | **bool** |  | [optional] 
**project_flag** | **bool** |  | [optional] 
**sales_flag** | **bool** |  | [optional] 
**service_flag** | **bool** |  | [optional] 
**track_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.notification_recipient import NotificationRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationRecipient from a JSON string
notification_recipient_instance = NotificationRecipient.from_json(json)
# print the JSON string representation of the object
print NotificationRecipient.to_json()

# convert the object into a dict
notification_recipient_dict = notification_recipient_instance.to_dict()
# create an instance of NotificationRecipient from a dict
notification_recipient_form_dict = notification_recipient.from_dict(notification_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


