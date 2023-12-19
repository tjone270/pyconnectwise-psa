# NotificationRecipientReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.notification_recipient_reference import NotificationRecipientReference

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationRecipientReference from a JSON string
notification_recipient_reference_instance = NotificationRecipientReference.from_json(json)
# print the JSON string representation of the object
print NotificationRecipientReference.to_json()

# convert the object into a dict
notification_recipient_reference_dict = notification_recipient_reference_instance.to_dict()
# create an instance of NotificationRecipientReference from a dict
notification_recipient_reference_form_dict = notification_recipient_reference.from_dict(notification_recipient_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


