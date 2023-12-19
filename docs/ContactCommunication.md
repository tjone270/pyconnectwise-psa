# ContactCommunication


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**communication_type** | **str** |  | [optional] 
**contact_id** | **int** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**domain** | **str** |  | [optional] 
**extension** | **str** |  Max length: 15; | [optional] 
**id** | **int** |  | [optional] 
**mobile_guid** | **str** |  | [optional] 
**type** | [**CommunicationTypeReference**](CommunicationTypeReference.md) |  | [optional] 
**value** | **str** |  Max length: 250; | 

## Example

```python
from connectwise_psa.models.contact_communication import ContactCommunication

# TODO update the JSON string below
json = "{}"
# create an instance of ContactCommunication from a JSON string
contact_communication_instance = ContactCommunication.from_json(json)
# print the JSON string representation of the object
print ContactCommunication.to_json()

# convert the object into a dict
contact_communication_dict = contact_communication_instance.to_dict()
# create an instance of ContactCommunication from a dict
contact_communication_form_dict = contact_communication.from_dict(contact_communication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


