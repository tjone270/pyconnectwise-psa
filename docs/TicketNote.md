# TicketNote


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**contact** | [**ContactReference**](ContactReference.md) |  | [optional] 
**customer_updated_flag** | **bool** |  | [optional] 
**detail_description_flag** | **bool** |  | [optional] 
**external_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**internal_analysis_flag** | **bool** |  | [optional] 
**internal_flag** | **bool** |  | [optional] 
**issue_flag** | **bool** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**process_notifications** | **bool** |  | [optional] 
**resolution_flag** | **bool** |  | [optional] 
**text** | **str** |  | [optional] 
**ticket_id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.ticket_note import TicketNote

# TODO update the JSON string below
json = "{}"
# create an instance of TicketNote from a JSON string
ticket_note_instance = TicketNote.from_json(json)
# print the JSON string representation of the object
print TicketNote.to_json()

# convert the object into a dict
ticket_note_dict = ticket_note_instance.to_dict()
# create an instance of TicketNote from a dict
ticket_note_form_dict = ticket_note.from_dict(ticket_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


