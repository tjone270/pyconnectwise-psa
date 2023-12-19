# ContactCommunicationItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communication_type** | **str** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**domain** | **str** |  | [optional] 
**extension** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**type** | [**CommunicationTypeReference**](CommunicationTypeReference.md) |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.contact_communication_item import ContactCommunicationItem

# TODO update the JSON string below
json = "{}"
# create an instance of ContactCommunicationItem from a JSON string
contact_communication_item_instance = ContactCommunicationItem.from_json(json)
# print the JSON string representation of the object
print ContactCommunicationItem.to_json()

# convert the object into a dict
contact_communication_item_dict = contact_communication_item_instance.to_dict()
# create an instance of ContactCommunicationItem from a dict
contact_communication_item_form_dict = contact_communication_item.from_dict(contact_communication_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


