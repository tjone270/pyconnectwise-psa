# ServiceTicketLink


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**enabled_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**link_text** | **str** |  Max length: 50; | 
**name** | **str** |  Max length: 50; | 
**url** | **str** |  Max length: 1000; | 

## Example

```python
from connectwise_psa.models.service_ticket_link import ServiceTicketLink

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTicketLink from a JSON string
service_ticket_link_instance = ServiceTicketLink.from_json(json)
# print the JSON string representation of the object
print ServiceTicketLink.to_json()

# convert the object into a dict
service_ticket_link_dict = service_ticket_link_instance.to_dict()
# create an instance of ServiceTicketLink from a dict
service_ticket_link_form_dict = service_ticket_link.from_dict(service_ticket_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


