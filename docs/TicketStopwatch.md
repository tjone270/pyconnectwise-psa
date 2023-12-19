# TicketStopwatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement** | [**AgreementReference**](AgreementReference.md) |  | [optional] 
**billable_option** | **str** |  | [optional] 
**business_unit_id** | **int** |  | [optional] 
**date_entered** | **datetime** |  | [optional] 
**email_notes_to_contact_flag** | **bool** |  | [optional] 
**email_notes_to_resources_flag** | **bool** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**internal_notes** | **str** |  | [optional] 
**location_id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**mobile_guid** | **str** |  | [optional] 
**notes** | **str** |  Max length: 4000; | [optional] 
**service_status** | [**ServiceStatusReference**](ServiceStatusReference.md) |  | [optional] 
**show_notes_in_discussion_flag** | **bool** |  | [optional] 
**show_notes_in_internal_flag** | **bool** |  | [optional] 
**show_notes_in_resolution_flag** | **bool** |  | [optional] 
**start_time** | **datetime** |  | [optional] 
**status** | **str** |  | 
**ticket** | [**TicketReference**](TicketReference.md) |  | [optional] 
**ticket_mobile_guid** | **str** |  | [optional] 
**total_pause_time** | **int** |  | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 
**work_type** | [**WorkTypeReference**](WorkTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.ticket_stopwatch import TicketStopwatch

# TODO update the JSON string below
json = "{}"
# create an instance of TicketStopwatch from a JSON string
ticket_stopwatch_instance = TicketStopwatch.from_json(json)
# print the JSON string representation of the object
print TicketStopwatch.to_json()

# convert the object into a dict
ticket_stopwatch_dict = ticket_stopwatch_instance.to_dict()
# create an instance of TicketStopwatch from a dict
ticket_stopwatch_form_dict = ticket_stopwatch.from_dict(ticket_stopwatch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


