# ServiceTicketLinkInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**link_text** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.service_ticket_link_info import ServiceTicketLinkInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTicketLinkInfo from a JSON string
service_ticket_link_info_instance = ServiceTicketLinkInfo.from_json(json)
# print the JSON string representation of the object
print ServiceTicketLinkInfo.to_json()

# convert the object into a dict
service_ticket_link_info_dict = service_ticket_link_info_instance.to_dict()
# create an instance of ServiceTicketLinkInfo from a dict
service_ticket_link_info_form_dict = service_ticket_link_info.from_dict(service_ticket_link_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


