# TicketReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.ticket_reference import TicketReference

# TODO update the JSON string below
json = "{}"
# create an instance of TicketReference from a JSON string
ticket_reference_instance = TicketReference.from_json(json)
# print the JSON string representation of the object
print TicketReference.to_json()

# convert the object into a dict
ticket_reference_dict = ticket_reference_instance.to_dict()
# create an instance of TicketReference from a dict
ticket_reference_form_dict = ticket_reference.from_dict(ticket_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


