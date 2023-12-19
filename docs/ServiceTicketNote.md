# ServiceTicketNote


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**bundled_flag** | **bool** |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**detail_description_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**internal_analysis_flag** | **bool** |  | [optional] 
**is_markdown_flag** | **bool** |  | [optional] 
**issue_flag** | **bool** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**merged_flag** | **bool** |  | [optional] 
**note_type** | **str** |  | [optional] 
**original_author** | **str** |  | [optional] 
**resolution_flag** | **bool** |  | [optional] 
**text** | **str** |  | [optional] 
**ticket** | [**TicketReference**](TicketReference.md) |  | [optional] 
**time_end** | **str** |  | [optional] 
**time_start** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.service_ticket_note import ServiceTicketNote

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceTicketNote from a JSON string
service_ticket_note_instance = ServiceTicketNote.from_json(json)
# print the JSON string representation of the object
print ServiceTicketNote.to_json()

# convert the object into a dict
service_ticket_note_dict = service_ticket_note_instance.to_dict()
# create an instance of ServiceTicketNote from a dict
service_ticket_note_form_dict = service_ticket_note.from_dict(service_ticket_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


