# TicketInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.ticket_info import TicketInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TicketInfo from a JSON string
ticket_info_instance = TicketInfo.from_json(json)
# print the JSON string representation of the object
print TicketInfo.to_json()

# convert the object into a dict
ticket_info_dict = ticket_info_instance.to_dict()
# create an instance of TicketInfo from a dict
ticket_info_form_dict = ticket_info.from_dict(ticket_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


