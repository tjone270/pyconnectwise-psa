# TicketMerge


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merge_ticket_ids** | **List[int]** |  | 
**status** | [**ServiceStatusReference**](ServiceStatusReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.ticket_merge import TicketMerge

# TODO update the JSON string below
json = "{}"
# create an instance of TicketMerge from a JSON string
ticket_merge_instance = TicketMerge.from_json(json)
# print the JSON string representation of the object
print TicketMerge.to_json()

# convert the object into a dict
ticket_merge_dict = ticket_merge_instance.to_dict()
# create an instance of TicketMerge from a dict
ticket_merge_form_dict = ticket_merge.from_dict(ticket_merge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


