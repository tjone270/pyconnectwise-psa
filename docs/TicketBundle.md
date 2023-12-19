# TicketBundle


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_ticket_ids** | **List[int]** |  | [optional] 

## Example

```python
from connectwise_psa.models.ticket_bundle import TicketBundle

# TODO update the JSON string below
json = "{}"
# create an instance of TicketBundle from a JSON string
ticket_bundle_instance = TicketBundle.from_json(json)
# print the JSON string representation of the object
print TicketBundle.to_json()

# convert the object into a dict
ticket_bundle_dict = ticket_bundle_instance.to_dict()
# create an instance of TicketBundle from a dict
ticket_bundle_form_dict = ticket_bundle.from_dict(ticket_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


